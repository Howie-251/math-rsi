use std::collections::BTreeSet;

use ahash::AHashSet;
use itertools::Itertools;

pub type Dimension = u8;
pub type Vertex = u8;

pub mod utils {
    use crate::*;

    pub mod bits {
        use crate::*;

        /// Return the bit mask set at index `ix`.
        ///
        /// # Examples
        /// ```
        /// # use hyper_cube::utils::bits::*;
        /// assert_eq!(mask_ix(1), 0b10);
        /// assert_eq!(mask_ix(3), 0b1000);
        /// ```
        pub fn mask_ix(ix: Dimension) -> Vertex {
            return 1 << ix;
        }

        /// Get mask of 1s to specified index (exclusive)
        ///
        /// # Examples
        /// ```
        /// # use hyper_cube::utils::bits::*;
        /// assert_eq!(mask_to(0), 0b0);
        /// assert_eq!(mask_to(3), 0b111);
        /// ```
        pub fn mask_to(index: Dimension) -> Vertex {
            return (1 << index) - 1;
        }

        /// Get mask of 1s from specified index (inclusive)
        ///
        /// # Examples
        /// ```
        /// # use hyper_cube::utils::bits::*;
        /// assert_eq!(mask_from(0), 0b11111111);
        /// assert_eq!(mask_from(5), 0b11100000);
        /// ```
        pub fn mask_from(index: Dimension) -> Vertex {
            return !mask_to(index);
        }

        /// Get bit at `index` position
        pub fn get_bit(num: Vertex, index: Dimension) -> bool {
            return (num & mask_ix(index)) != 0;
        }

        /// Set bit at `index` position
        pub fn set_bit(num: Vertex, index: Dimension) -> Vertex {
            return num | mask_ix(index);
        }

        /// Flip bit at `index` position
        pub fn flip_bit(num: Vertex, index: Dimension) -> Vertex {
            return num ^ mask_ix(index);
        }

        /// Insert a zero bit in the binary representation of a number
        ///
        /// # Examples
        /// ```
        /// # use hyper_cube::utils::bits::*;
        /// assert_eq!(insert_zero_bit(0b1111, 0), 0b11110);
        /// assert_eq!(insert_zero_bit(0b1111, 2), 0b11011);
        /// ```
        pub fn insert_zero_bit(num: Vertex, index: Dimension) -> Vertex {
            return ((num & mask_from(index)) << 1) | (num & mask_to(index));
        }

        /// Insert a one bit in the binary representation of a number
        ///
        /// # Examples
        /// ```
        /// # use hyper_cube::utils::bits::*;
        /// assert_eq!(insert_one_bit(0b111000, 0), 0b1110001);
        /// assert_eq!(insert_one_bit(0b111000, 2), 0b1110100);
        /// ```
        pub fn insert_one_bit(num: Vertex, index: Dimension) -> Vertex {
            return set_bit(
                ((num & mask_from(index)) << 1) | (num & mask_to(index)),
                index,
            );
        }

        /// Remove a bit from the binary representation of a number
        ///
        /// # Examples
        /// ```
        /// # use hyper_cube::utils::bits::*;
        /// assert_eq!(remove_bit(0b110100, 0), 0b11010);
        /// assert_eq!(remove_bit(0b110100, 2), 0b11000);
        /// ```
        pub fn remove_bit(num: Vertex, index: Dimension) -> Vertex {
            return ((num & mask_from(index + 1)) >> 1) | (num & mask_to(index));
        }
    }

    /// Get the direction of edge that is determined by two vertices, this will work only correctly
    /// of both of these vertices are neighbours (their Hamming distance is one).
    ///
    /// # Examples
    /// ```
    /// # use hyper_cube::utils::*;
    /// assert_eq!(edge_direction(0b00101, 0b00001), 2);
    /// assert_eq!(edge_direction(0b01101, 0b00101), 3);
    /// ```
    pub fn edge_direction(a: Vertex, b: Vertex) -> Dimension {
        return (a ^ b).trailing_zeros() as Dimension;
    }

    /// Transform a number to an edge, that is done taking the number modulo dimension, which
    /// results in a direction of an edge and the number divided by the dimension results in a base
    /// vertex in dimension - 1. Now in this vertex at direction position insert one and zero.
    pub fn number_to_edge(number: Vertex, dimension: Dimension) -> Edge {
        let base_vertex = number / (dimension as Vertex);
        let direction = number % (dimension as Vertex);

        return Edge::new(
            utils::bits::insert_zero_bit(base_vertex, direction),
            utils::bits::insert_one_bit(base_vertex, direction),
        );
    }

    /// Similar process as described in `number_to_edge`
    pub fn edge_to_number(a: Vertex, b: Vertex, dimension: Dimension) -> Vertex {
        let direction = edge_direction(a, b);
        let base_vertex = utils::bits::remove_bit(a, direction);

        return base_vertex * (dimension as Vertex) + (direction as Vertex);
    }

    /// Get vertex count of hypercube in a dimension
    pub fn vertex_count(dimension: Dimension) -> Vertex {
        (2 as Vertex).pow(dimension as u32)
    }

    /// Get edge count of hypercube in a dimension
    pub fn edge_count(dimension: Dimension) -> Vertex {
        dimension as Vertex * vertex_count(dimension - 1)
    }

    /// Get vertex neighbor in hypercube in a direction
    pub fn vertex_neighbour(vertex: Vertex, direction: Dimension) -> Vertex {
        return utils::bits::flip_bit(vertex, direction);
    }

    #[derive(PartialEq, Eq, Debug)]
    pub enum Parity {
        Odd,
        Even,
    }

    /// Get the vertex weight, determined by number of ones
    pub fn vertex_weight(vertex: Vertex) -> u32 {
        vertex.count_ones()
    }

    /// Get vertex parity, based on the vertex weight
    pub fn vertex_parity(vertex: Vertex) -> Parity {
        if vertex_weight(vertex) % 2 == 0 {
            Parity::Even
        } else {
            Parity::Odd
        }
    }

    /// Get all of the start and end vertices of opposite parity combinations.
    pub fn start_end_vertices(dimension: Dimension) -> Vec<(Vertex, Vertex)> {
        (0..vertex_count(dimension))
            .tuple_combinations()
            .filter(|(a, b)| vertex_parity(*a) != vertex_parity(*b))
            .collect()
    }

    /// Get all of the start and end vertices of opposite parity combinations, such that at least
    /// one of the vertices is zero.
    pub fn start_end_vertices_including_zero(dimension: Dimension) -> Vec<(Vertex, Vertex)> {
        (0..vertex_count(dimension))
            .tuple_combinations()
            .filter(|(a, b)| (*a == 0 || *b == 0) && vertex_parity(*a) != vertex_parity(*b))
            .collect()
    }
}

/// Edge representation. It is done as separate structure since we do want to enforce that when
/// constructed than the vertices in the edge are going to be ordered. That is important mainly if
/// we will want to hash the edge.
#[derive(Eq, PartialEq, Hash, Debug, Clone, PartialOrd, Ord)]
pub struct Edge(pub Vertex, pub Vertex);

impl Edge {
    /// Check whether an edge contains a vertex
    ///
    /// # Examples
    /// ```
    /// # use hyper_cube::*;
    /// assert_eq!(Edge::new(0b00101, 0b00001).contains(0b00101), true);
    /// assert_eq!(Edge::new(0b00101, 0b00001).contains(0b00111), false);
    /// ```
    pub fn contains(&self, vertex: Vertex) -> bool {
        self.0 == vertex || self.1 == vertex
    }

    /// Return the other vertex of an edge. If the edge is not present this will return an
    /// arbitrary vertex, it is your responsibility to check that the vertex is really present on
    /// this edge.
    ///
    /// # Examples
    /// ```
    /// # use hyper_cube::*;
    /// assert_eq!(Edge::new(0b00101, 0b00001).other(0b00101), 0b00001);
    /// ```
    pub fn other(&self, vertex: Vertex) -> Vertex {
        if self.0 == vertex {
            self.1
        } else {
            self.0
        }
    }

    /// The direction of the edge
    pub fn direction(&self) -> Dimension {
        return utils::edge_direction(self.0, self.1);
    }

    /// The parity of the edge
    pub fn parity(&self) -> utils::Parity {
        return utils::vertex_parity(self.0);
    }

    /// The edge represented as one number
    pub fn to_number(&self, dimension: Dimension) -> Vertex {
        return utils::edge_to_number(self.0, self.1, dimension);
    }

    /// Create edge from two vertices and create the correctly ordered version
    pub fn new(a: Vertex, b: Vertex) -> Self {
        if a < b {
            Self(a, b)
        } else {
            Self(b, a)
        }
    }
}

impl From<(Vertex, Vertex)> for Edge {
    fn from(value: (Vertex, Vertex)) -> Self {
        Self::new(value.0, value.1)
    }
}

/// Represent edges directly via pair of edges (where the pair is ordered, so we have unique
/// representation for edge connecting vertex a and b).
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct Edges {
    /// The dimension of the hypercube
    pub dimension: Dimension,
    /// The actual edges
    pub edges: BTreeSet<Edge>,
}

impl Edges {
    pub fn new(dimension: Dimension) -> Self {
        Self {
            dimension,
            edges: BTreeSet::new(),
        }
    }

    pub fn new_with_edges(dimension: Dimension, edges: BTreeSet<Edge>) -> Self {
        Self { dimension, edges }
    }

    /// Check if contains an edge
    pub fn contains(&self, edge: &Edge) -> bool {
        self.edges.contains(edge)
    }

    /// Return self without an edge
    pub fn without(mut self, edge: &Edge) -> Edges {
        self.edges.remove(edge);
        self
    }

    /// Return self with new edge
    pub fn with(mut self, edge: Edge) -> Edges {
        self.edges.insert(edge);
        self
    }

    /// Return the number of edges contained
    pub fn len(&self) -> usize {
        self.edges.len()
    }

    /// Return representation by number of edges and start and end vertices (so we can represent
    /// long edges)
    pub fn vertex_ends_to_string(&self) -> String {
        format!(
            "{} {}",
            self.edges.len(),
            self.edges
                .iter()
                .format_with(" ", |edge, f| f(&format_args!("{} {}", edge.0, edge.1)))
        )
    }
}

/// Create edges from a Vec
impl From<(Dimension, Vec<Edge>)> for Edges {
    fn from(t: (Dimension, Vec<Edge>)) -> Self {
        let (dimension, edges) = t;
        let mut result = BTreeSet::new();

        for edge in edges {
            result.insert(edge);
        }

        Self {
            dimension,
            edges: result,
        }
    }
}

/// Create edges from matching
impl From<MatchingByReference> for Edges {
    fn from(edges: MatchingByReference) -> Self {
        let mut seen = vec![false; utils::vertex_count(edges.dimension) as usize];
        let mut result = BTreeSet::new();

        for (index, reference) in edges.items.iter().enumerate() {
            if seen[index] {
                continue;
            }

            match reference {
                MatchingVertexReference::Vertex(vertex) => {
                    seen[index] = true;
                    seen[*vertex as usize] = true;

                    result.insert(Edge::new(index as Vertex, *vertex));
                }
                _ => {}
            }
        }

        Self {
            dimension: edges.dimension,
            edges: result,
        }
    }
}

/// Implement to string for short edges only!
impl ToString for Edges {
    fn to_string(&self) -> String {
        format!(
            "{} {}",
            self.edges.len(),
            self.edges
                .iter()
                .format_with(" ", |edge, f| f(&edge.to_number(self.dimension)))
        )
    }
}

#[derive(Debug, Clone, PartialOrd, Ord, Eq, PartialEq, Hash, Copy)]
pub enum MatchingVertexReference {
    Uncovered,
    Vertex(Vertex),
}

/// Matching representation. Each vertex can be either uncovered or it can be matched with another
/// vertex.
#[derive(Debug, Eq, PartialEq, Hash, Clone, PartialOrd, Ord)]
pub struct MatchingByReference {
    pub dimension: Dimension,
    pub items: Vec<MatchingVertexReference>,
}

impl MatchingByReference {
    pub fn new(dimension: Dimension) -> Self {
        Self {
            dimension,
            items: vec![
                MatchingVertexReference::Uncovered;
                utils::vertex_count(dimension) as usize
            ],
        }
    }

    /// Check whether matching contains an edge
    pub fn contains(&self, edge: &Edge) -> bool {
        self.items[edge.0 as usize] == MatchingVertexReference::Vertex(edge.1)
            && self.items[edge.1 as usize] == MatchingVertexReference::Vertex(edge.0)
    }

    /// Construct matching from edges
    pub fn from_edges(edges: &Edges) -> Self {
        let mut result =
            vec![MatchingVertexReference::Uncovered; utils::vertex_count(edges.dimension) as usize];

        for edge in edges.edges.iter() {
            result[edge.0 as usize] = MatchingVertexReference::Vertex(edge.1);
            result[edge.1 as usize] = MatchingVertexReference::Vertex(edge.0);
        }

        Self {
            dimension: edges.dimension,
            items: result,
        }
    }

    /// Check if the matching is valid
    pub fn valid(&self) -> bool {
        for (index, reference) in self.items.iter().enumerate() {
            match reference {
                MatchingVertexReference::Vertex(vertex) => match self.items[*vertex as usize] {
                    MatchingVertexReference::Vertex(other_vertex) => {
                        if other_vertex != (index as Vertex) {
                            return false;
                        }
                    }
                    _ => return false,
                },
                _ => {}
            }
        }

        return true;
    }

    /// Return self without an edge
    pub fn without(mut self, edge: &Edge) -> MatchingByReference {
        if self.contains(&edge) {
            self.items[edge.0 as usize] = MatchingVertexReference::Uncovered;
            self.items[edge.1 as usize] = MatchingVertexReference::Uncovered;
        }

        self
    }

    /// Join vertices in the matching
    pub fn join_vertices(&mut self, edge: &Edge) {
        assert!(self.items[edge.0 as usize] == MatchingVertexReference::Uncovered);
        assert!(self.items[edge.1 as usize] == MatchingVertexReference::Uncovered);

        self.items[edge.0 as usize] = MatchingVertexReference::Vertex(edge.1);
        self.items[edge.1 as usize] = MatchingVertexReference::Vertex(edge.0);
    }
}

/// Print the matching (consisting of short edges!) as string
impl ToString for MatchingByReference {
    fn to_string(&self) -> String {
        Edges::from(self.clone()).to_string()
    }
}

pub mod algorithms {
    /// Algorithm mirroring https://arxiv.org/abs/2401.01769, with a few improvements and
    /// adjustments
    pub mod hamilton_path {
        use crate::*;

        /// The possible states of vertex in the path
        #[derive(Debug, Clone, Copy, PartialEq, Eq)]
        pub enum VertexConfig {
            /// It is not covered yet by any edge
            Uncovered,
            /// It is forbidden to use this vertex, this may be either plan from the beginning that
            /// we do not want to use this vertex, or it may become forbidden during path
            /// construction
            Forbidden,
            /// Symbolizes that this vertex is terminal in the path, there may be multiple
            /// terminals in the path
            Terminal,
            /// The vertex is covered by an edge/shortcut.
            Vertex(Vertex),
        }

        impl From<MatchingVertexReference> for VertexConfig {
            fn from(value: MatchingVertexReference) -> Self {
                match value {
                    MatchingVertexReference::Uncovered => VertexConfig::Uncovered,
                    MatchingVertexReference::Vertex(vertex) => VertexConfig::Vertex(vertex),
                }
            }
        }

        /// Representation of the final path (of vertices that have been joined together)
        #[derive(Debug, Clone, PartialEq, Eq)]
        pub enum JoinedState {
            None,
            One(Vertex),
            Two(Vertex, Vertex),
        }

        impl JoinedState {
            pub fn extend(&self, vertex: Vertex) -> Self {
                match self {
                    JoinedState::None => JoinedState::One(vertex),
                    JoinedState::One(previous) => JoinedState::Two(*previous, vertex),
                    _ => panic!("Should not happen"),
                }
            }

            /// Get the next vertex from the joined pair
            pub fn next(&self, curr: Option<Vertex>) -> Option<Vertex> {
                match curr {
                    None => match self {
                        JoinedState::One(a) => Some(*a),
                        _ => None,
                    },
                    Some(curr) => match self {
                        JoinedState::Two(a, b) => {
                            if *a == curr {
                                Some(*b)
                            } else {
                                Some(*a)
                            }
                        }
                        _ => None,
                    },
                }
            }
        }

        /// The path configuration in hypercube
        #[derive(Debug, Clone, PartialEq, Eq)]
        pub struct PathConfig {
            pub dimension: Dimension,
            /// The current vertex states for each vertex, there must be a few valid invariants
            /// - the vertices that have edge/shortcut between them must point to each other
            /// - the number of terminals must be even
            pub path: Vec<VertexConfig>,
            joined: Vec<JoinedState>,
            forbidden_edges: AHashSet<Edge>,
            free_degrees: Vec<i32>,
            number_of_forbidden: usize,
            number_of_terminals: usize,
            number_of_uncovered: usize,
            number_of_connected: usize,
        }

        /// Convert the path configuration from edges
        impl From<Edges> for PathConfig {
            fn from(value: Edges) -> Self {
                let mut path_config = PathConfig::new_uncovered(value.dimension);

                for edge in value.edges.iter() {
                    path_config.join_vertices(edge.0, edge.1);
                }

                path_config
            }
        }

        /// Convert the path configuration from matching
        impl From<MatchingByReference> for PathConfig {
            fn from(edges: MatchingByReference) -> Self {
                let mut visited = vec![false; utils::vertex_count(edges.dimension) as usize];
                let mut path_config = PathConfig::new_uncovered(edges.dimension);

                for (index, reference) in edges.items.iter().enumerate() {
                    match reference {
                        MatchingVertexReference::Vertex(vertex) => {
                            if visited[index] || visited[*vertex as usize] {
                                continue;
                            }

                            path_config.join_vertices(index as Vertex, *vertex);

                            visited[index] = true;
                            visited[*vertex as usize] = true;
                        }
                        _ => {}
                    }
                }

                path_config
            }
        }

        impl PathConfig {
            pub fn new_uncovered(dimension: Dimension) -> Self {
                Self {
                    dimension,
                    path: vec![VertexConfig::Uncovered; utils::vertex_count(dimension) as usize],
                    joined: vec![JoinedState::None; utils::vertex_count(dimension) as usize],
                    forbidden_edges: AHashSet::new(),
                    number_of_forbidden: 0,
                    number_of_terminals: 0,
                    number_of_uncovered: utils::vertex_count(dimension) as usize,
                    number_of_connected: 0,
                    free_degrees: vec![dimension as i32; utils::vertex_count(dimension) as usize],
                }
            }

            /// Get current path length
            fn len(&self) -> usize {
                self.path.len()
            }

            /// All vertices are forbidden
            pub fn are_all_forbidden(&self) -> bool {
                self.number_of_forbidden == self.len()
            }

            /// Get neighbors that may be joined to a vertex
            pub fn count_available_neighbours(&self, vertex: Vertex) -> usize {
                (0..self.dimension)
                    .filter(
                        |d| match self.path[utils::vertex_neighbour(vertex, *d) as usize] {
                            VertexConfig::Forbidden => false,
                            //VertexConfig::Vertex(v) => v != vertex,
                            _ => true,
                        },
                    )
                    .count()
            }

            /// Return the vertex with the smallest number of available neighbours
            pub fn most_restricted_vertex(&self) -> Option<Vertex> {
                self.free_degrees
                    .iter()
                    .cloned()
                    .enumerate()
                    .filter(|(_, degree)| *degree != 0)
                    .min_by_key(|(_, degree)| *degree)
                    .map(|(vertex, _)| vertex as Vertex)
            }

            /// Check whether the path configuration is valid
            pub fn is_valid(&self) -> bool {
                // That joined vertices ends really corresponds to each other
                for (index, vertex) in self.path.iter().enumerate() {
                    match vertex {
                        VertexConfig::Vertex(v) => {
                            if self.path[*v as usize] != VertexConfig::Vertex(index as Vertex) {
                                return false;
                            }
                        }
                        _ => {}
                    }
                }

                // That the number of forbidden vertices really corresponds to the forbidden
                // vertices
                if self.number_of_forbidden
                    != self
                        .path
                        .iter()
                        .filter(|x| **x == VertexConfig::Forbidden)
                        .count()
                {
                    return false;
                }

                // That the number of terminal vertices really corresponds to the terminal
                // vertices
                if self.number_of_terminals
                    != self
                        .path
                        .iter()
                        .filter(|x| **x == VertexConfig::Terminal)
                        .count()
                {
                    return false;
                }

                // That the number of uncovered vertices really corresponds to the uncovered
                // vertices
                if self.number_of_uncovered
                    != self
                        .path
                        .iter()
                        .filter(|x| **x == VertexConfig::Uncovered)
                        .count()
                {
                    return false;
                }

                // That the number of vertices in all states corresponds to the length
                if self.number_of_connected
                    + self.number_of_forbidden
                    + self.number_of_terminals
                    + self.number_of_uncovered
                    != self.len()
                {
                    return false;
                }

                // That the number of free degrees of vertex corresponds to the available
                // neighbors
                for (vertex, value) in self.path.iter().enumerate() {
                    match value {
                        VertexConfig::Forbidden => {
                            if self.free_degrees[vertex] != 0 {
                                return false;
                            }
                        }
                        _ => {
                            if self.free_degrees[vertex]
                                != self.count_available_neighbours(vertex as Vertex) as i32
                            {
                                return false;
                            }
                        }
                    }
                }

                return true;
            }

            /// Check if vertex is forbidden in path
            pub fn is_forbidden(&self, vertex: Vertex) -> bool {
                match self.path[vertex as usize] {
                    VertexConfig::Forbidden => true,
                    _ => false,
                }
            }

            /// Check whether edges is forbidden
            pub fn is_forbidden_edge(&self, a: Vertex, b: Vertex) -> bool {
                self.forbidden_edges.contains(&Edge::new(a, b))
            }

            /// Check whether we can connect the vertices
            pub fn is_forbidden_connection(&self, a: Vertex, b: Vertex) -> bool {
                return self.path[a as usize] == VertexConfig::Forbidden
                    || self.path[b as usize] == VertexConfig::Forbidden
                    || self.is_forbidden_edge(a, b);
            }

            /// Check whether vertices are connected
            pub fn are_connected(&self, a: Vertex, b: Vertex) -> bool {
                match (self.path[a as usize], self.path[b as usize]) {
                    (VertexConfig::Vertex(va), VertexConfig::Vertex(vb)) => va == b && vb == a,
                    _ => false,
                }
            }

            /// Update the free degrees of a neighbor
            fn update_neighbours(&mut self, vertex: Vertex, value: i32) {
                for d in 0..self.dimension {
                    let neighbour = utils::vertex_neighbour(vertex, d);

                    if self.is_forbidden_connection(vertex, neighbour) {
                        continue;
                    }

                    self.free_degrees[neighbour as usize] += value;
                    self.free_degrees[vertex as usize] += value;
                }
            }

            /// Mark vertex as uncovered updating all of the corresponding numbers and potentially
            /// neighbors free degrees / state
            pub fn mark_uncovered(&mut self, vertex: Vertex) {
                match self.path[vertex as usize] {
                    VertexConfig::Terminal => {
                        self.number_of_terminals -= 1;
                        self.number_of_uncovered += 1;

                        self.path[vertex as usize] = VertexConfig::Uncovered;
                    }
                    VertexConfig::Forbidden => {
                        self.number_of_forbidden -= 1;
                        self.number_of_uncovered += 1;

                        self.path[vertex as usize] = VertexConfig::Uncovered;
                        self.update_neighbours(vertex, 1);
                    }
                    VertexConfig::Vertex(v) => {
                        self.number_of_connected -= 2;
                        self.number_of_uncovered += 2;

                        self.path[vertex as usize] = VertexConfig::Uncovered;
                        self.path[v as usize] = VertexConfig::Uncovered;
                    }
                    VertexConfig::Uncovered => {}
                }
            }

            /// Mark vertex as forbidden updating all of the corresponding numbers and potentially
            /// neighbors free degrees / state
            pub fn mark_forbidden(&mut self, vertex: Vertex) {
                match self.path[vertex as usize] {
                    VertexConfig::Uncovered => {
                        self.number_of_uncovered -= 1;
                        self.number_of_forbidden += 1;

                        self.update_neighbours(vertex, -1);
                        self.path[vertex as usize] = VertexConfig::Forbidden;
                    }
                    VertexConfig::Forbidden => {}
                    VertexConfig::Terminal => {
                        self.number_of_terminals -= 1;
                        self.number_of_forbidden += 1;

                        self.update_neighbours(vertex, -1);
                        self.path[vertex as usize] = VertexConfig::Forbidden;
                    }
                    VertexConfig::Vertex(v) => {
                        self.number_of_connected -= 2;
                        self.number_of_forbidden += 1;
                        self.number_of_uncovered += 1;

                        self.update_neighbours(vertex, -1);
                        self.path[vertex as usize] = VertexConfig::Forbidden;

                        self.path[v as usize] = VertexConfig::Uncovered;
                    }
                }
            }

            /// Mark edge as forbidden
            pub fn make_forbidden_edge(&mut self, a: Vertex, b: Vertex) {
                self.forbidden_edges.insert(Edge::new(a, b));

                self.free_degrees[a as usize] -= 1;
                self.free_degrees[b as usize] -= 1;
            }

            /// Mark vertex as terminal and if it is part of an edge or shortcut, move the terminal
            /// to correct place. Meaning if we have a shortcut a <-> b and we mark a as terminal,
            /// then we actually want to mark b as terminal and a as forbidden.
            pub fn mark_terminal(&mut self, vertex: Vertex) {
                match self.path[vertex as usize] {
                    VertexConfig::Uncovered => {
                        self.number_of_uncovered -= 1;
                        self.number_of_terminals += 1;

                        self.path[vertex as usize] = VertexConfig::Terminal;
                    }
                    VertexConfig::Vertex(v) => {
                        self.number_of_forbidden += 1;
                        self.number_of_terminals += 1;
                        self.number_of_connected -= 2;

                        self.update_neighbours(vertex, -1);
                        self.path[vertex as usize] = VertexConfig::Forbidden;

                        self.path[v as usize] = VertexConfig::Terminal;
                    }
                    VertexConfig::Terminal => {}
                    VertexConfig::Forbidden => {
                        self.number_of_forbidden -= 1;
                        self.number_of_terminals += 1;

                        self.path[vertex as usize] = VertexConfig::Terminal;
                        self.update_neighbours(vertex, 1);
                    }
                }
            }

            /// Join two vertices together while keeping all of the invariants that should hold for
            /// PathConfig.
            pub fn join_vertices(&mut self, a: Vertex, b: Vertex) -> bool {
                if self.is_forbidden_edge(a, b) {
                    return false;
                }

                match (self.path[a as usize], self.path[b as usize]) {
                    (VertexConfig::Uncovered, VertexConfig::Uncovered) => {
                        self.number_of_uncovered -= 2;
                        self.number_of_connected += 2;

                        self.path[a as usize] = VertexConfig::Vertex(b);
                        self.path[b as usize] = VertexConfig::Vertex(a);
                    }
                    (VertexConfig::Uncovered, VertexConfig::Terminal) => {
                        self.number_of_uncovered -= 1;
                        self.number_of_forbidden += 1;

                        self.update_neighbours(b, -1);
                        self.path[b as usize] = VertexConfig::Forbidden;

                        self.path[a as usize] = VertexConfig::Terminal;
                    }
                    (VertexConfig::Terminal, VertexConfig::Uncovered) => {
                        self.number_of_uncovered -= 1;
                        self.number_of_forbidden += 1;

                        self.update_neighbours(a, -1);
                        self.path[a as usize] = VertexConfig::Forbidden;

                        self.path[b as usize] = VertexConfig::Terminal;
                    }
                    (VertexConfig::Uncovered, VertexConfig::Vertex(v)) => {
                        self.number_of_uncovered -= 1;
                        self.number_of_forbidden += 1;

                        self.update_neighbours(b, -1);
                        self.path[b as usize] = VertexConfig::Forbidden;

                        self.path[a as usize] = VertexConfig::Vertex(v);
                        self.path[v as usize] = VertexConfig::Vertex(a);
                    }
                    (VertexConfig::Vertex(v), VertexConfig::Uncovered) => {
                        self.number_of_uncovered -= 1;
                        self.number_of_forbidden += 1;

                        self.update_neighbours(a, -1);
                        self.path[a as usize] = VertexConfig::Forbidden;

                        self.path[v as usize] = VertexConfig::Vertex(b);
                        self.path[b as usize] = VertexConfig::Vertex(v);
                    }
                    (VertexConfig::Vertex(v), VertexConfig::Terminal) => {
                        self.number_of_connected -= 2;
                        self.number_of_forbidden += 2;

                        self.update_neighbours(a, -1);
                        self.path[a as usize] = VertexConfig::Forbidden;
                        self.update_neighbours(b, -1);
                        self.path[b as usize] = VertexConfig::Forbidden;

                        self.path[v as usize] = VertexConfig::Terminal;
                    }
                    (VertexConfig::Terminal, VertexConfig::Vertex(v)) => {
                        self.number_of_connected -= 2;
                        self.number_of_forbidden += 2;

                        self.update_neighbours(a, -1);
                        self.path[a as usize] = VertexConfig::Forbidden;
                        self.update_neighbours(b, -1);
                        self.path[b as usize] = VertexConfig::Forbidden;

                        self.path[v as usize] = VertexConfig::Terminal;
                    }
                    (VertexConfig::Terminal, VertexConfig::Terminal) => {
                        self.update_neighbours(a, -1);
                        self.path[a as usize] = VertexConfig::Forbidden;
                        self.update_neighbours(b, -1);
                        self.path[b as usize] = VertexConfig::Forbidden;

                        self.number_of_terminals -= 2;
                        self.number_of_forbidden += 2;
                    }
                    (VertexConfig::Vertex(u), VertexConfig::Vertex(v)) => {
                        if u == b && v == a {
                            return false;
                        }

                        self.path[u as usize] = VertexConfig::Vertex(v);
                        self.path[v as usize] = VertexConfig::Vertex(u);

                        self.update_neighbours(a, -1);
                        self.path[a as usize] = VertexConfig::Forbidden;
                        self.update_neighbours(b, -1);
                        self.path[b as usize] = VertexConfig::Forbidden;

                        self.number_of_connected -= 2;
                        self.number_of_forbidden += 2;
                    }
                    (_, VertexConfig::Forbidden) | (VertexConfig::Forbidden, _) => {
                        return false;
                    }
                }

                self.joined[a as usize] = self.joined[a as usize].extend(b);
                self.joined[b as usize] = self.joined[b as usize].extend(a);

                return true;
            }

            /// Get the final path
            pub fn get_path(&self) -> Option<Vec<Vertex>> {
                if !self.are_all_forbidden() {
                    return None;
                }

                let first = self.joined.iter().enumerate().find_map(|(ix, x)| match x {
                    JoinedState::One(a) => Some((ix, *a)),
                    _ => None,
                });

                let Some((first_ix, first_vertex)) = first else {
                    return None;
                };

                let mut path = Vec::with_capacity(utils::vertex_count(self.dimension) as usize);
                path.push(first_ix as Vertex);
                let mut prev = Some(first_ix as Vertex);
                let mut curr = Some(first_vertex);

                while let Some(curr_vertex) = curr {
                    path.push(curr_vertex);

                    let next = self.joined[curr_vertex as usize].next(prev);
                    prev = curr;
                    curr = next;
                }

                return Some(path);
            }

            /// Recursively find the path by adding edges iteratively
            pub fn find_path(&self) -> Option<Vec<Vertex>> {
                let vertex_to_process = match self.most_restricted_vertex() {
                    Some(v) => v,
                    None => {
                        if self.are_all_forbidden() {
                            return Some(self.get_path().unwrap());
                        } else {
                            return None;
                        }
                    }
                };

                // For each of the neighbours
                for d in 0..self.dimension {
                    let neighbour = utils::vertex_neighbour(vertex_to_process, d);
                    let mut state = self.clone();

                    if !state.join_vertices(vertex_to_process, neighbour) {
                        continue;
                    }

                    match state.find_path() {
                        Some(path) => {
                            return Some(path);
                        }
                        _ => {}
                    }
                }

                None
            }
        }

        #[cfg(test)]
        mod tests {
            use std::error::Error;

            use super::*;

            #[test]
            fn test_join_vertices_and_mark_terminals() -> Result<(), Box<dyn Error>> {
                let mut path_config = PathConfig::new_uncovered(2);

                assert!(path_config.is_valid());

                assert!(path_config.join_vertices(0b00, 0b01));
                assert!(path_config.is_valid());
                assert!(path_config.join_vertices(0b10, 0b11));
                assert!(path_config.is_valid());

                assert_eq!(
                    path_config.path,
                    vec![
                        VertexConfig::Vertex(0b01),
                        VertexConfig::Vertex(0b00),
                        VertexConfig::Vertex(0b11),
                        VertexConfig::Vertex(0b10)
                    ]
                );

                path_config.mark_terminal(0b00);
                assert!(path_config.is_valid());

                assert_eq!(
                    path_config.path,
                    vec![
                        VertexConfig::Forbidden,
                        VertexConfig::Terminal,
                        VertexConfig::Vertex(0b11),
                        VertexConfig::Vertex(0b10)
                    ]
                );

                path_config.mark_terminal(0b10);
                assert!(path_config.is_valid());

                assert_eq!(
                    path_config.path,
                    vec![
                        VertexConfig::Forbidden,
                        VertexConfig::Terminal,
                        VertexConfig::Forbidden,
                        VertexConfig::Terminal,
                    ]
                );

                assert!(
                    path_config.most_restricted_vertex() == Some(0b10)
                        || path_config.most_restricted_vertex() == Some(0b01)
                );

                assert!(path_config.join_vertices(0b01, 0b11));
                assert!(path_config.is_valid());

                assert_eq!(
                    path_config.path,
                    vec![
                        VertexConfig::Forbidden,
                        VertexConfig::Forbidden,
                        VertexConfig::Forbidden,
                        VertexConfig::Forbidden,
                    ]
                );

                let mut path_config = PathConfig::new_uncovered(2);

                path_config.mark_terminal(0b00);
                path_config.mark_terminal(0b10);
                assert!(path_config.join_vertices(0b00, 0b01));
                assert!(path_config.is_valid());
                assert!(path_config.join_vertices(0b10, 0b11));
                assert!(path_config.is_valid());

                assert_eq!(
                    path_config.path,
                    vec![
                        VertexConfig::Forbidden,
                        VertexConfig::Terminal,
                        VertexConfig::Forbidden,
                        VertexConfig::Terminal,
                    ]
                );

                Ok(())
            }

            #[test]
            fn test_path_is_found_in_simple_restricted_case() -> Result<(), Box<dyn Error>> {
                let mut path_config = PathConfig::new_uncovered(2);

                assert!(path_config.join_vertices(0b00, 0b01));
                assert!(path_config.join_vertices(0b10, 0b11));
                path_config.mark_terminal(0b00);
                path_config.mark_terminal(0b10);

                assert_eq!(path_config.find_path(), Some(()));

                Ok(())
            }

            #[test]
            fn test_path_is_found_in_simple_unrestricted_case() -> Result<(), Box<dyn Error>> {
                let mut path_config = PathConfig::new_uncovered(2);

                path_config.mark_terminal(0b00);
                path_config.mark_terminal(0b10);
                assert!(path_config.is_valid());

                assert_eq!(path_config.find_path(), Some(()));

                let mut path_config = PathConfig::new_uncovered(3);

                path_config.mark_terminal(0b000);
                path_config.mark_terminal(0b100);

                assert_eq!(path_config.find_path(), Some(()));

                Ok(())
            }

            #[test]
            fn test_path_is_found_with_multiple_terminals() -> Result<(), Box<dyn Error>> {
                let mut path_config = PathConfig::new_uncovered(2);

                path_config.mark_terminal(0b00);
                path_config.mark_terminal(0b10);
                path_config.mark_terminal(0b01);
                path_config.mark_terminal(0b11);

                assert_eq!(path_config.find_path(), Some(()));

                let mut path_config = PathConfig::new_uncovered(3);

                assert!(path_config.join_vertices(0b000, 0b100));
                path_config.mark_terminal(0b000);
                path_config.mark_terminal(0b010);

                assert!(path_config.join_vertices(0b101, 0b001));
                path_config.mark_terminal(0b001);
                path_config.mark_terminal(0b011);

                assert_eq!(path_config.find_path(), Some(()));

                Ok(())
            }
        }
    }

    pub mod automorphisms {
        use crate::*;

        use itertools::*;
        use std::hash::Hash;

        #[derive(Clone, Debug, PartialEq, Eq)]
        pub struct Automorphism(Vec<Vertex>);

        impl Automorphism {
            pub fn new(vec: Vec<Vertex>) -> Self {
                Self(vec)
            }

            pub fn transform(&self, vertex: Vertex) -> Vertex {
                self.0[vertex as usize]
            }
        }

        /// Permutate the directions of a vertex, that corresponds to permutating the bits in the
        /// bit representation of the vertex
        ///
        /// # Examples
        ///
        /// ```
        /// # use hyper_cube::algorithms::automorphisms::*;
        /// assert_eq!(permutate_directions(0b10101, &vec![0, 1, 2, 3, 4]), 0b10101);
        /// assert_eq!(permutate_directions(0b10101, &vec![4, 2, 0, 1, 3]), 0b00111);
        /// assert_eq!(permutate_directions(0b10101, &vec![4, 2, 1, 3, 0]), 0b10011);
        /// ```
        pub fn permutate_directions(vertex: Vertex, permutation: &Vec<Dimension>) -> Vertex {
            let mut result: Vertex = 0;

            for (index, direction) in permutation.iter().enumerate() {
                if utils::bits::get_bit(vertex, *direction as Dimension) {
                    result = utils::bits::set_bit(result, index as Dimension);
                }
            }

            result
        }

        /// Generate all automorphisms stemming from permutation of directions, which corresponds
        /// to the rotations of the hypercube of the specified dimension.
        ///
        /// # Examples
        /// For dimension two we have two permutations `(1, 2)` (identity) and `(2, 1)` (changing
        /// first coordinate to second and vice versa).
        ///
        /// ```
        /// # use hyper_cube::algorithms::automorphisms::*;
        /// assert_eq!(
        ///     generate_all_permutations_of_directions_automorphisms(2),
        ///     vec![
        ///         Automorphism::from_vec(vec![0b00, 0b01, 0b10, 0b11]),
        ///         Automorphism::from_vec(vec![0b00, 0b10, 0b01, 0b11]),
        ///     ],
        /// );
        /// ```
        pub fn generate_all_permutations_of_directions_automorphisms(
            dimension: Dimension,
        ) -> Vec<Automorphism> {
            let mut result = Vec::new();

            for permutation in (0..dimension).permutations(dimension.into()) {
                let mut automorphism = Vec::with_capacity(utils::vertex_count(dimension) as usize);

                for vertex in 0..utils::vertex_count(dimension) {
                    automorphism.push(permutate_directions(vertex, &permutation));
                }

                result.push(Automorphism(automorphism));
            }

            result
        }

        /// Generate all automorphisms stemming from flipping bits, which correspond to the
        /// reflections of the specified hypercube of the specified dimension.
        ///
        /// # Examples
        /// For dimension two we have four possible bit flips corresponding to the actual vertices
        /// of the square.
        ///
        /// ```
        /// # use hyper_cube::algorithms::automorphisms::*;
        /// assert_eq!(
        ///     generate_all_flipping_bits_automorphisms(2),
        ///     vec![
        ///         Automorphism::from_vec(vec![0b00, 0b01, 0b10, 0b11]), // not flipping any bits
        ///         Automorphism::from_vec(vec![0b01, 0b00, 0b11, 0b10]), // flipping first bit
        ///         Automorphism::from_vec(vec![0b10, 0b11, 0b00, 0b01]), // flipping second bit
        ///         Automorphism::from_vec(vec![0b11, 0b10, 0b01, 0b00]), // flipping both bits
        ///     ]
        /// )
        /// ```
        pub fn generate_all_flipping_bits_automorphisms(dimension: Dimension) -> Vec<Automorphism> {
            let mut result = Vec::new();

            for flip in 0..utils::vertex_count(dimension) {
                let mut automorphism = Vec::with_capacity(utils::vertex_count(dimension) as usize);

                for vertex in 0..utils::vertex_count(dimension) {
                    automorphism.push(flip ^ vertex);
                }

                result.push(Automorphism(automorphism));
            }

            result
        }

        /// Generate all of the automorphisms that are present on the hyper cube of specified
        /// dimension including rotations and reflections.
        ///
        /// # Examples
        /// For the hypercube of dimension two we should have 4 * 2 of automorphisms (n! * 2^n,
        /// where n corresponds to the dimension of the hypercube, note that there are (2^n)! of
        /// isomorphisms).
        /// ```
        /// # use hyper_cube::algorithms::automorphisms::*;
        /// assert_eq!(
        ///     generate_all_automorphisms(2),
        ///     vec![
        ///         // no rotation
        ///         Automorphism::from_vec(vec![0b00, 0b01, 0b10, 0b11]), // not flipping any bits,
        ///         Automorphism::from_vec(vec![0b01, 0b00, 0b11, 0b10]), // flipping first bit
        ///         Automorphism::from_vec(vec![0b10, 0b11, 0b00, 0b01]), // flipping second bit
        ///         Automorphism::from_vec(vec![0b11, 0b10, 0b01, 0b00]), // flipping both bits
        ///         // rotation
        ///         Automorphism::from_vec(vec![0b00, 0b10, 0b01, 0b11]), // not flipping any bits,
        ///         Automorphism::from_vec(vec![0b01, 0b11, 0b00, 0b10]), // flipping second bit
        ///         Automorphism::from_vec(vec![0b10, 0b00, 0b11, 0b01]), // flipping first bit
        ///         Automorphism::from_vec(vec![0b11, 0b01, 0b10, 0b00]), // flipping both bits
        ///     ]
        /// )
        /// ```
        pub fn generate_all_automorphisms(dimension: Dimension) -> Vec<Automorphism> {
            let mut result = Vec::new();

            for (a, b) in iproduct!(
                generate_all_permutations_of_directions_automorphisms(dimension),
                generate_all_flipping_bits_automorphisms(dimension)
            ) {
                result.push(b.apply_automorphism(&a));
            }

            result
        }

        impl Automorphism {
            pub fn from_vec(vec: Vec<Vertex>) -> Self {
                Self(vec)
            }

            pub fn identity(size: usize) -> Self {
                Self((0..size).map(|x| (x as Vertex)).collect())
            }

            pub fn valid_isomorphism(&self) -> bool {
                let mut seen_vertices = vec![false; self.0.len()];

                for vertex in self.0.iter() {
                    if seen_vertices[*vertex as usize] {
                        return false;
                    }

                    seen_vertices[*vertex as usize] = true;
                }

                true
            }
        }

        pub trait Transform: Sized {
            fn apply_automorphism(&self, automorphism: &Automorphism) -> Self;
        }

        /// Combine two automorphisms together
        impl Transform for Automorphism {
            fn apply_automorphism(&self, automorphism: &Automorphism) -> Self {
                assert!(
                    self.0.len() == automorphism.0.len(),
                    "The automorphisms have different sizes"
                );

                let mut result = vec![0; self.0.len()];

                for (index, vertex) in automorphism.0.iter().enumerate() {
                    result[index] = self.transform(*vertex);
                }

                Self(result)
            }
        }

        /// Apply the automorphism to edges
        impl Transform for Edges {
            fn apply_automorphism(&self, automorphism: &Automorphism) -> Edges {
                let mut result = BTreeSet::new();

                for edge in self.edges.iter() {
                    result.insert(Edge::new(
                        automorphism.transform(edge.0),
                        automorphism.transform(edge.1),
                    ));
                }

                Edges {
                    dimension: self.dimension,
                    edges: result,
                }
            }
        }

        /// Apply the automorphism to matching
        impl Transform for MatchingByReference {
            fn apply_automorphism(&self, automorphism: &Automorphism) -> MatchingByReference {
                debug_assert!(self.valid(), "The edges are not valid");
                assert!(
                    self.items.len() == automorphism.0.len(),
                    "The edges and the automorphism have different sizes"
                );

                let mut result = vec![MatchingVertexReference::Uncovered; self.items.len()];

                for (index, vertex) in automorphism.0.iter().enumerate() {
                    result[*vertex as usize] = match self.items[index] {
                        MatchingVertexReference::Vertex(v) => {
                            MatchingVertexReference::Vertex(automorphism.0[v as usize])
                        }
                        _ => MatchingVertexReference::Uncovered,
                    }
                }

                MatchingByReference {
                    dimension: self.dimension,
                    items: result,
                }
            }
        }

        /// Apply the automorphism to veector of vertices
        impl Transform for Vec<Vertex> {
            fn apply_automorphism(&self, automorphism: &Automorphism) -> Vec<Vertex> {
                let mut result = vec![0; self.len()];

                for (index, vertex) in self.iter().enumerate() {
                    result[index] = automorphism.transform(*vertex);
                }

                result
            }
        }

        /// A filter that checks matchings for automorphisms. If the added matching is already in
        /// the set do nothing, otherwise add all of its automorphisms
        #[derive(Debug)]
        pub struct AutomorphismFilter<T> {
            automorphisms: Vec<Automorphism>,
            already_seen: AHashSet<T>,
        }

        impl<T: Transform + Ord + Hash + Clone> AutomorphismFilter<T> {
            pub fn new(automorphisms: Vec<Automorphism>) -> Self {
                return Self {
                    automorphisms,
                    already_seen: AHashSet::new(),
                };
            }

            pub fn already_seen_count(&self) -> usize {
                self.already_seen.len()
            }

            /// Create a new filter for a specific dimension containing all of the possible
            /// automorphisms there are.
            pub fn new_for_dimension(dimension: Dimension) -> Self {
                return Self::new(generate_all_automorphisms(dimension));
            }

            /// Add the edges to the filter and return the minimal representation of the edges. If
            /// it is already present, return None.
            pub fn add(&mut self, item: &T) -> Option<T> {
                if self.already_seen.contains(item) {
                    return None;
                }

                self.automorphisms
                    .iter()
                    .map(|automorphism| item.apply_automorphism(automorphism))
                    .inspect(|transformed| {
                        self.already_seen.insert(transformed.clone());
                    })
                    .min()
            }
        }

        /// A filter that checks matchings for automorphisms
        #[derive(Debug)]
        pub struct MinimalAutomorphismFilter<T> {
            automorphisms: Vec<Automorphism>,
            already_seen: AHashSet<T>,
        }

        impl<T: Transform + Ord + Hash + Clone> MinimalAutomorphismFilter<T> {
            pub fn new(automorphisms: Vec<Automorphism>) -> Self {
                return Self {
                    automorphisms,
                    already_seen: AHashSet::new(),
                };
            }

            pub fn already_seen_count(&self) -> usize {
                self.already_seen.len()
            }

            /// Create a new filter for a specific dimension containing all of the possible
            /// automorphisms there are.
            pub fn new_for_dimension(dimension: Dimension) -> Self {
                return Self::new(generate_all_automorphisms(dimension));
            }

            /// Add the edges to the filter and return the minimal representation of the edges. If
            /// it is already present, return None.
            pub fn add(&mut self, item: &T) -> Option<T> {
                let mut minimal = None;

                for automorphism in self.automorphisms.iter() {
                    let transformed = item.apply_automorphism(automorphism);

                    if self.already_seen.contains(&transformed) {
                        return None;
                    }

                    if minimal.is_none() || &transformed < minimal.as_ref().unwrap() {
                        minimal = Some(transformed);
                    }
                }

                self.already_seen.insert(minimal.clone().unwrap());

                return minimal;
            }
        }
    }

    pub mod maximal_matchings {
        use crate::*;

        /// Each vertex in a matching must be either matched with another vertex or be uncovered,
        /// but surrounded by vertices that are matched.
        ///
        /// The forbidden state is used to indicate that the vertex is not going to be matched and
        /// it must be surrounded by vertices that will be matched, denoted by teh ToMatch state.
        #[derive(Clone, Debug)]
        enum MatchingVertexType {
            // Vertex was not yet processed
            Uncovered,
            // Vertex is in the current configuration forbidden
            Forbidden,
            // Vertex must be matched in future
            ToMatch,
            // Vertex is matched with another vertex
            Matched(Vertex),
        }

        /// The state of the matching to be.
        #[derive(Debug, Clone)]
        struct MatchingState {
            dimension: Dimension,
            items: Vec<MatchingVertexType>,
        }

        impl From<MatchingState> for Edges {
            fn from(state: MatchingState) -> Self {
                let mut already_used = vec![false; state.items.len()];
                let mut result = BTreeSet::new();

                for (index, value) in state.items.iter().enumerate() {
                    match value {
                        MatchingVertexType::Matched(vertex) if !already_used[index] => {
                            already_used[*vertex as usize] = true;
                            already_used[index] = true;
                            result.insert(Edge::new(index as Vertex, *vertex));
                        }
                        _ => {}
                    }
                }

                Edges {
                    dimension: state.dimension,
                    edges: result,
                }
            }
        }

        // If there is a vertex that needs to be matched, return it, otherwise return the first
        // uncovered vertex.
        fn find_vertex_to_process(state: &MatchingState) -> Option<Vertex> {
            let mut result: Option<Vertex> = None;

            for (index, value) in state.items.iter().enumerate() {
                match value {
                    MatchingVertexType::ToMatch => {
                        return Some(index as Vertex);
                    }
                    MatchingVertexType::Uncovered => {
                        result = Some(index as Vertex);
                    }
                    _ => {}
                }
            }

            result
        }

        pub struct GenerateMaximalMatchings {
            dimension: Dimension,
            stack: Vec<MatchingState>,
        }

        impl GenerateMaximalMatchings {
            pub fn new(dimension: Dimension) -> Self {
                Self {
                    dimension,
                    stack: vec![MatchingState {
                        dimension,
                        items: vec![
                            MatchingVertexType::Uncovered;
                            utils::vertex_count(dimension) as usize
                        ],
                    }],
                }
            }

            pub fn new_omitting_zero(dimension: Dimension) -> Self {
                let mut items =
                    vec![MatchingVertexType::Uncovered; utils::vertex_count(dimension) as usize];

                items[0] = MatchingVertexType::Forbidden;

                for d in 0..dimension {
                    let neighbour = utils::vertex_neighbour(0, d);

                    items[neighbour as usize] = MatchingVertexType::ToMatch;
                }

                Self {
                    dimension,
                    stack: vec![MatchingState {
                        dimension,
                        items: items,
                    }],
                }
            }
        }

        impl Iterator for GenerateMaximalMatchings {
            type Item = Edges;

            fn next(&mut self) -> Option<Self::Item> {
                let mut current = self.stack.pop()?;
                // If there is no vertex to process, we have found a maximal matching
                let to_process = match find_vertex_to_process(&current) {
                    Some(v) => v,
                    None => return Some(current.into()),
                };

                // Try to match with all of the neighbours
                for d in 0..self.dimension {
                    let neighbour = utils::vertex_neighbour(to_process, d);

                    match current.items[neighbour as usize] {
                        MatchingVertexType::Uncovered | MatchingVertexType::ToMatch => {
                            let mut new_state = current.clone();

                            new_state.items[to_process as usize] =
                                MatchingVertexType::Matched(neighbour);
                            new_state.items[neighbour as usize] =
                                MatchingVertexType::Matched(to_process);

                            self.stack.push(new_state);
                        }
                        _ => {}
                    }
                }

                // If the current vertex is marked as that it needs to be part of a matching, just
                // end here and do not consider the case when it is not part of the matching.
                if let MatchingVertexType::ToMatch = current.items[to_process as usize] {
                    return self.next();
                }

                current.items[to_process as usize] = MatchingVertexType::Forbidden;

                for d in 0..self.dimension {
                    let neighbour = utils::vertex_neighbour(to_process, d);

                    match current.items[neighbour as usize] {
                        MatchingVertexType::Uncovered => {
                            current.items[neighbour as usize] = MatchingVertexType::ToMatch;
                        }
                        _ => {}
                    }
                }

                self.stack.push(current);

                self.next()
            }
        }
    }
}
