use ahash::{HashMap, HashMapExt};
use hyper_cube as hc;
use itertools::Itertools;
use rayon::iter::ParallelBridge;
use rayon::prelude::ParallelIterator;
use std::io::BufRead;
use structopt::StructOpt;

use std::error::Error;

pub fn generate_maximal_matchings_up_to_isomorphism(
    dimension: u8,
    omit_zero: bool,
) -> impl Iterator<Item = hc::MatchingByReference> {
    assert!(dimension > 0 && dimension <= 6);

    let mut filter =
        hc::algorithms::automorphisms::AutomorphismFilter::new_for_dimension(dimension);

    if omit_zero {
        hc::algorithms::maximal_matchings::GenerateMaximalMatchings::new_omitting_zero(dimension)
    } else {
        hc::algorithms::maximal_matchings::GenerateMaximalMatchings::new(dimension)
    }
    .flat_map(move |edges| filter.add(&hc::MatchingByReference::from_edges(&edges)))
}

pub fn test_for_hamilton_path(
    path_config: &hc::algorithms::hamilton_path::PathConfig,
    terminals: &Vec<(hc::Vertex, hc::Vertex)>,
    discard_connected: bool,
) -> Vec<(hc::Vertex, hc::Vertex)> {
    let mut result = Vec::new();

    for (start, end) in terminals.iter().cloned() {
        // If either of terminals is forbidden, we can skip this pair
        if path_config.is_forbidden(start) || path_config.is_forbidden(end) {
            continue;
        }

        let mut clone = path_config.clone();

        if clone.are_connected(start, end) {
            if discard_connected {
                continue;
            }

            clone.mark_uncovered(start);
            clone.mark_uncovered(end);
        }

        clone.mark_terminal(start);
        clone.mark_terminal(end);

        match clone.find_path() {
            None => {
                result.push((start, end));
            }
            _ => {}
        }
    }

    return result;
}

pub fn test_for_hamilton_path_and_get_minimal_forced_edge_subset(
    forced_edges: hc::Edges,
    terminals_to_test: &Vec<(hc::Vertex, hc::Vertex)>,
    already_seen: &mut HashMap<hc::Edges, bool>,
) -> bool {
    if let Some(&r) = already_seen.get(&forced_edges) {
        return r;
    }

    let mut all_success = true;

    for edge in forced_edges.edges.iter() {
        assert!(forced_edges.contains(&edge));
        let new_edges = forced_edges.clone().without(&edge);
        let path_config: hc::algorithms::hamilton_path::PathConfig = new_edges.clone().into();
        let failed_terminals = test_for_hamilton_path(&path_config, terminals_to_test, true);

        // Once we get that each two endpoints can be extended, we do not have to check anymore,
        // since all smaller matchings can be extended to this one and thus to a Hamilton path
        // extending that matching
        if failed_terminals.len() == 0 {
            println!("{} 0 0", new_edges.to_string());
            continue;
        }

        all_success = false;

        println!(
            "{} {} {}",
            new_edges.to_string(),
            failed_terminals.len(),
            failed_terminals
                .iter()
                .format_with(" ", |(a, b), f| f(&format_args!("{} {}", a, b)))
        );

        let _ = test_for_hamilton_path_and_get_minimal_forced_edge_subset(
            new_edges.clone(),
            terminals_to_test,
            already_seen,
        );

        // if r {
        // }
    }

    already_seen.insert(forced_edges.clone(), all_success);

    return all_success;
}

pub fn test_for_hamilton_path_at_least_one_vertex_two_possibilities(
    path_config: &hc::algorithms::hamilton_path::PathConfig,
    terminals: &Vec<(hc::Vertex, hc::Vertex)>,
) -> Vec<(hc::Vertex, hc::Vertex)> {
    let mut result = Vec::new();

    for (start, end) in terminals.iter().cloned() {
        // If either of terminals is forbidden, we can skip this pair
        if path_config.is_forbidden(start) || path_config.is_forbidden(end) {
            continue;
        }

        if path_config.are_connected(start, end) {
            continue; // Skip C3
        }

        let mut clone = path_config.clone();

        clone.mark_terminal(start);
        clone.mark_terminal(end);

        if clone.find_path().is_none() {
            result.push((start, end));
            continue;
        }

        let mut counts = vec![0; hc::utils::vertex_count(path_config.dimension) as usize];
        let mut done = false;

        for e_num in 0..hc::utils::edge_count(path_config.dimension) {
            let e = hc::utils::number_to_edge(e_num, path_config.dimension);
            let (a, b) = (e.0, e.1);

            // Skip already connected
            if path_config.are_connected(a, b) {
                continue;
            }

            // Skip terminals
            if a == start || b == start || a == end || b == end {
                continue;
            }

            clone = path_config.clone();
            clone.mark_terminal(start);
            clone.mark_terminal(end);
            clone.join_vertices(a, b);

            if clone.find_path().is_some() {
                counts[a as usize] += 1;
                counts[b as usize] += 1;

                if counts[a as usize] >= 2 {
                    done = true;
                    break;
                }
            }
        }

        if !done {
            result.push((start, end));
        }
    }

    return result;
}

pub fn test_all_matchings_for_simple_hamilton_path(dimension: u8, stdin: bool, omit_zero: bool) {
    let terminals = if omit_zero {
        hc::utils::start_end_vertices_including_zero(dimension)
    } else {
        hc::utils::start_end_vertices(dimension)
    };

    if stdin {
        let stdin = std::io::stdin();

        for line in stdin.lock().lines() {
            let line = line.unwrap();
            let mut data = line.split_whitespace();

            let edges_num = data.next().unwrap().parse::<usize>().unwrap();
            let edges = hc::Edges::new_with_edges(
                dimension,
                data.take(edges_num)
                    .map(|x| hc::utils::number_to_edge(x.parse().unwrap(), dimension))
                    .collect(),
            );
            let matching = hc::MatchingByReference::from_edges(&edges);
            let result = test_for_hamilton_path(&matching.clone().into(), &terminals, true);

            println!(
                "{} {} {}",
                matching.to_string(),
                result.len(),
                result
                    .iter()
                    .format_with(" ", |elt, f| f(&format_args!("{} {}", elt.0, elt.1)))
            );
        }
    } else {
        generate_maximal_matchings_up_to_isomorphism(dimension, omit_zero)
            .par_bridge()
            .for_each(|matching| {
                let result = test_for_hamilton_path(&matching.clone().into(), &terminals, true);
                println!(
                    "{} {} {}",
                    matching.to_string(),
                    result.len(),
                    result
                        .iter()
                        .format_with(" ", |elt, f| f(&format_args!("{} {}", elt.0, elt.1)))
                );
            });
    }
}

pub fn test_all_matchings_for_hamilton_path_with_one_vertex_at_least_two_possibilities(
    dimension: u8,
    stdin: bool,
) {
    let terminals = hc::utils::start_end_vertices(dimension);

    if stdin {
        let stdin = std::io::stdin();

        for line in stdin.lock().lines() {
            let line = line.unwrap();
            let mut data = line.split_whitespace();

            let edges_num = data.next().unwrap().parse::<usize>().unwrap();
            let edges = hc::Edges::new_with_edges(
                dimension,
                data.take(edges_num)
                    .map(|x| hc::utils::number_to_edge(x.parse().unwrap(), dimension))
                    .collect(),
            );
            let matching = hc::MatchingByReference::from_edges(&edges);
            let result = test_for_hamilton_path_at_least_one_vertex_two_possibilities(
                &matching.clone().into(),
                &terminals,
            );

            println!(
                "{} {} {}",
                matching.to_string(),
                result.len(),
                result
                    .iter()
                    .format_with(" ", |elt, f| f(&format_args!("{} {}", elt.0, elt.1)))
            );
        }
    } else {
        generate_maximal_matchings_up_to_isomorphism(dimension, false)
            .par_bridge()
            .for_each(|matching| {
                let result = test_for_hamilton_path_at_least_one_vertex_two_possibilities(
                    &matching.clone().into(),
                    &terminals,
                );
                println!(
                    "{} {} {}",
                    matching.to_string(),
                    result.len(),
                    result
                        .iter()
                        .format_with(" ", |elt, f| f(&format_args!("{} {}", elt.0, elt.1)))
                );
            });
    }
}

#[derive(StructOpt)]
enum Command {
    /// Generate all maximal matchings of given dimension up to an isomorphism. The generated
    /// matchings are one per line in the following format, `n e_1 e_2 ... e_n`, where n is the
    /// number of edges in the matching and e_1, e_2, ... e_n are the edges in the matching.
    GenerateMaximalMatchingsUpToIsomorphism {
        #[structopt(short, long)]
        dimension: u8,
    },
    /// Generate all maximal matchings of given dimension up to an isomorphism and test them if
    /// they are extendable to a Hamilton path. The output is in the following format, `n e_1 e_2
    /// ... e_n m a_1 b_1 a_2 b_2 ... a_m b_m`, where n is the number of edges in the matching and
    /// e_1, e_2, ... e_n are the edges in the matching, m is the number of terminal pairs that are
    /// not connected by a Hamilton path and a_1 b_1 a_2 b_2 ... a_m b_m are the terminal pairs.
    TestAllMatchingsForSimpleHamiltonPath {
        #[structopt(short, long)]
        dimension: u8,
        #[structopt(short, long)]
        stdin: bool,
        #[structopt(short, long)]
        omit_zero: bool,
    },
    /// Generate all maximal matchings of given dimension up to an isomorphism and test them if
    /// they are extendable to a Hamilton path. If they are for some combination of end vertices
    /// then try if one of other vertices (except the endpoints), has two neighbors to which this
    /// Hamilton path can be routed.
    TestAllMatchingsForHamiltonPathAndOneVertexWithAtLeastTwoPossibilities {
        #[structopt(short, long)]
        dimension: u8,
        #[structopt(short, long)]
        stdin: bool,
    },
    FindPath {
        matching: String,
        start: u8,
        end: u8,
        #[structopt(short, long)]
        dimension: u8,
    },
    SquashIsomorphisms {
        #[structopt(short, long)]
        dimension: u8,
    },
    TestMatchingsForFirstSubsetAllowingAll {
        #[structopt(short, long)]
        dimension: u8,
    },
}

pub fn main() -> Result<(), Box<dyn Error>> {
    match Command::from_args() {
        Command::GenerateMaximalMatchingsUpToIsomorphism { dimension } => {
            for matching in generate_maximal_matchings_up_to_isomorphism(dimension, false) {
                println!("{}", matching.to_string(),);
            }
        }
        Command::TestAllMatchingsForSimpleHamiltonPath {
            dimension,
            stdin,
            omit_zero,
        } => {
            test_all_matchings_for_simple_hamilton_path(dimension, stdin, omit_zero);
        }
        Command::TestAllMatchingsForHamiltonPathAndOneVertexWithAtLeastTwoPossibilities {
            dimension,
            stdin,
        } => {
            test_all_matchings_for_hamilton_path_with_one_vertex_at_least_two_possibilities(
                dimension, stdin,
            );
        }
        Command::TestMatchingsForFirstSubsetAllowingAll { dimension } => {
            let stdin = std::io::stdin();

            for line in stdin.lock().lines() {
                let line = line.unwrap();
                let mut data = line.split_whitespace();
                let edges_num = data.next().unwrap().parse::<usize>().unwrap();
                let edges = hc::Edges::new_with_edges(
                    dimension,
                    data.by_ref()
                        .take(edges_num)
                        .map(|x| hc::utils::number_to_edge(x.parse().unwrap(), dimension))
                        .collect(),
                );

                let terminals_num = data.next().unwrap().parse::<usize>().unwrap();
                let terminals = data
                    .by_ref()
                    .take(terminals_num * 2)
                    .map(|x| x.parse::<hc::Vertex>().unwrap())
                    .tuples()
                    .collect::<Vec<(hc::Vertex, hc::Vertex)>>();

                test_for_hamilton_path_and_get_minimal_forced_edge_subset(
                    edges,
                    &terminals,
                    &mut HashMap::new(),
                );
            }
        }
        Command::FindPath {
            matching,
            start,
            end,
            dimension,
        } => {
            let mut data = matching.split_whitespace();
            let edges_num = data.next().unwrap().parse::<usize>().unwrap();
            let edges = hc::Edges::new_with_edges(
                dimension,
                data.take(edges_num)
                    .map(|x| hc::utils::number_to_edge(x.parse().unwrap(), dimension))
                    .collect(),
            );

            for edge in edges.edges.iter() {
                println!("{:?} {:?} {:?}", edge, edge.parity(), edge.direction());
            }

            println!(
                "{:?} {:?} {:?}",
                hc::Edge(start, end),
                hc::Edge(start, end).parity(),
                hc::Edge(start, end).direction()
            );

            let mut path_config: hc::algorithms::hamilton_path::PathConfig = edges.clone().into();

            println!("{:?}", path_config.path);
            path_config.mark_terminal(start);
            path_config.mark_terminal(end);

            println!("{:?}", path_config.path);

            match path_config.find_path() {
                Some(path) => println!(
                    "{} {}",
                    path.len(),
                    path.iter()
                        .format_with(" ", |vertex, f| f(&format_args!("{}", vertex)))
                ),
                None => println!("0"),
            }
        }
        Command::SquashIsomorphisms { dimension } => {
            let mut filter =
                hc::algorithms::automorphisms::AutomorphismFilter::new_for_dimension(dimension);

            for line in std::io::stdin().lock().lines() {
                let line = line.unwrap();
                let mut data = line.split_whitespace();
                let edges_num = data.next().unwrap().parse::<usize>().unwrap();
                let edges = hc::Edges::new_with_edges(
                    dimension,
                    data.by_ref()
                        .take(edges_num)
                        .map(|x| hc::utils::number_to_edge(x.parse().unwrap(), dimension))
                        .collect(),
                );

                let terminals_num = data.next().unwrap().parse::<usize>().unwrap();
                let terminals = data
                    .by_ref()
                    .take(terminals_num * 2)
                    .map(|x| x.parse::<hc::Vertex>().unwrap())
                    .tuples()
                    .collect::<Vec<(hc::Vertex, hc::Vertex)>>();
                // let new_terminals = Vec::new();

                for (start, end) in terminals {
                    let start_edge = edges.edges.iter().find(|e| e.contains(start));
                    let end_edge = edges.edges.iter().find(|e| e.contains(end));

                    let edges_to_use =
                        if let (Some(start_edge), Some(end_edge)) = (start_edge, end_edge) {
                            edges
                                .clone()
                                .without(start_edge)
                                .without(end_edge)
                                .with(hc::Edge::new(start_edge.other(start), end_edge.other(end)))
                        } else {
                            edges.clone()
                        };

                    let Some(added) =
                        filter.add(&hc::MatchingByReference::from_edges(&edges_to_use))
                    else {
                        continue;
                    };

                    let edges: hc::Edges = added.into();

                    println!("{}", edges.vertex_ends_to_string());
                }
            }
        }
    }

    Ok(())
}
