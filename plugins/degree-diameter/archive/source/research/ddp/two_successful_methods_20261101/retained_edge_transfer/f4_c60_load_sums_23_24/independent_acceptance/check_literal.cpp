#include <algorithm>
#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <sys/resource.h>
#include <utility>
#include <vector>

// This checker reads the two literal edge tables only. It has no dependency on
// construction code, owner choices, recipes, matrices, or coverage caches.
using Edge = std::pair<int, int>;
using Histogram = std::map<int, int>;
constexpr int OLD_N = 3840;
constexpr int NEW_N = 4336;
constexpr long long OLD_M = 38400;
constexpr long long NEW_M = 48320;
constexpr int MAX_DEGREE = 23;

const std::string SOURCE =
    "research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/graph_d20_D3_n3840.edges";
const std::string CANDIDATE =
    "research/ddp/two_successful_methods_20261101/retained_edge_transfer/f4_c60_load_sums_23_24/graph_d23_D3_n4336.edges";
const std::string OUTDIR =
    "research/ddp/two_successful_methods_20261101/retained_edge_transfer/f4_c60_load_sums_23_24/independent_acceptance/";

struct Graph {
    int n = 0;
    long long declared_edges = 0;
    std::vector<Edge> edges;
    std::vector<std::vector<int>> adjacency;
};

struct RootResult {
    int root;
    int reached;
    int reached_within_three;
    int eccentricity;
    Histogram distances;
};

struct Report {
    std::string status = "FAIL";
    std::string failure;
    bool source_literal_pass = false;
    bool candidate_literal_pass = false;
    bool undirected = false;
    bool degree_pass = false;
    bool old_edges_exact = false;
    bool new_vertices_pass = false;
    bool connected = false;
    bool new_root_radius_three_pass = false;
    int source_n = 0;
    int candidate_n = 0;
    long long source_m = 0;
    long long candidate_m = 0;
    long long old_old_edges = 0;
    long long retained_source_edges = 0;
    long long missing_source_edges = 0;
    long long extra_old_old_edges = 0;
    long long new_new_edges = 0;
    int candidate_max_degree = 0;
    Histogram source_degrees;
    Histogram candidate_degrees;
    Histogram old_degrees;
    Histogram new_degrees;
    std::vector<RootResult> roots;
    int counterexample_root = -1;
    int counterexample_target = -1;
    int counterexample_distance = -2;
};

std::string json_string(const std::string& s) {
    std::ostringstream out;
    out << '"';
    for (char c : s) {
        if (c == '"' || c == '\\') out << '\\' << c;
        else if (c == '\n') out << "\\n";
        else if (c == '\r') out << "\\r";
        else if (c == '\t') out << "\\t";
        else out << c;
    }
    out << '"';
    return out.str();
}

std::string histogram_json(const Histogram& h) {
    std::ostringstream out;
    out << '{';
    bool first = true;
    for (const auto& [degree, count] : h) {
        if (!first) out << ',';
        first = false;
        out << json_string(std::to_string(degree)) << ':' << count;
    }
    out << '}';
    return out.str();
}

std::pair<long long, long long> parse_pair(const std::string& line,
                                          const std::string& path,
                                          int line_number) {
    std::istringstream in(line);
    long long u, v;
    std::string extra;
    if (!(in >> u >> v) || (in >> extra)) {
        throw std::runtime_error(path + ": malformed pair at line " +
                                 std::to_string(line_number));
    }
    return {u, v};
}

Graph read_literal(const std::string& path, int expected_n,
                   long long expected_m) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("cannot open literal edge table: " + path);
    std::string line;
    if (!std::getline(in, line)) throw std::runtime_error("empty file: " + path);
    const auto [n, m] = parse_pair(line, path, 1);
    if (n != expected_n || m != expected_m) {
        throw std::runtime_error(path + ": header is " + std::to_string(n) +
            " " + std::to_string(m) + "; expected " +
            std::to_string(expected_n) + " " + std::to_string(expected_m));
    }
    Graph g;
    g.n = expected_n;
    g.declared_edges = m;
    g.edges.reserve(expected_m);
    int line_number = 1;
    while (std::getline(in, line)) {
        ++line_number;
        if (line.find_first_not_of(" \t\r") == std::string::npos) continue;
        auto [a, b] = parse_pair(line, path, line_number);
        if (a < 0 || b < 0 || a >= n || b >= n) {
            throw std::runtime_error(path + ": out-of-range edge (" +
                std::to_string(a) + "," + std::to_string(b) + ") at line " +
                std::to_string(line_number));
        }
        if (a == b) {
            throw std::runtime_error(path + ": self-loop at vertex " +
                std::to_string(a) + " on line " + std::to_string(line_number));
        }
        if (a > b) std::swap(a, b);
        g.edges.emplace_back(static_cast<int>(a), static_cast<int>(b));
    }
    if (in.bad()) throw std::runtime_error("read error: " + path);
    if (static_cast<long long>(g.edges.size()) != m) {
        throw std::runtime_error(path + ": literal edge count " +
            std::to_string(g.edges.size()) + " differs from header " +
            std::to_string(m));
    }
    std::sort(g.edges.begin(), g.edges.end());
    auto duplicate = std::adjacent_find(g.edges.begin(), g.edges.end());
    if (duplicate != g.edges.end()) {
        throw std::runtime_error(path + ": repeated undirected edge (" +
            std::to_string(duplicate->first) + "," +
            std::to_string(duplicate->second) + ")");
    }
    g.adjacency.resize(g.n);
    for (auto [u, v] : g.edges) {
        g.adjacency[u].push_back(v);
        g.adjacency[v].push_back(u);
    }
    return g;
}

Histogram degrees(const Graph& g, int first, int last) {
    Histogram result;
    for (int v = first; v < last; ++v) ++result[g.adjacency[v].size()];
    return result;
}

void verify(Report& r) {
    const Graph source = read_literal(SOURCE, OLD_N, OLD_M);
    r.source_n = source.n;
    r.source_m = source.edges.size();
    r.source_degrees = degrees(source, 0, OLD_N);
    if (r.source_degrees != Histogram{{20, OLD_N}}) {
        throw std::runtime_error("source literal is not 20-regular: " +
                                 histogram_json(r.source_degrees));
    }
    r.source_literal_pass = true;

    const Graph g = read_literal(CANDIDATE, NEW_N, NEW_M);
    r.candidate_n = g.n;
    r.candidate_m = g.edges.size();
    r.candidate_literal_pass = true;
    // Each literal pair denotes one unordered edge; reciprocal adjacency is
    // constructed explicitly and independently verified below.
    for (int v = 0; v < g.n; ++v) {
        for (int u : g.adjacency[v]) {
            if (std::count(g.adjacency[u].begin(), g.adjacency[u].end(), v) != 1)
                throw std::runtime_error("asymmetric literal adjacency at (" +
                    std::to_string(v) + "," + std::to_string(u) + ")");
        }
    }
    r.undirected = true;
    r.candidate_degrees = degrees(g, 0, NEW_N);
    r.old_degrees = degrees(g, 0, OLD_N);
    r.new_degrees = degrees(g, OLD_N, NEW_N);
    r.candidate_max_degree = r.candidate_degrees.rbegin()->first;
    for (int v = 0; v < g.n; ++v) {
        if (g.adjacency[v].size() > MAX_DEGREE) {
            throw std::runtime_error("degree bound fails at vertex " +
                std::to_string(v) + ": degree " +
                std::to_string(g.adjacency[v].size()));
        }
    }
    r.degree_pass = true;

    std::vector<Edge> old_old;
    for (auto e : g.edges) {
        if (e.second < OLD_N) old_old.push_back(e);
        else if (e.first >= OLD_N) ++r.new_new_edges;
    }
    r.old_old_edges = old_old.size();
    std::vector<Edge> missing, extra, retained;
    std::set_difference(source.edges.begin(), source.edges.end(),
        old_old.begin(), old_old.end(), std::back_inserter(missing));
    std::set_difference(old_old.begin(), old_old.end(),
        source.edges.begin(), source.edges.end(), std::back_inserter(extra));
    std::set_intersection(source.edges.begin(), source.edges.end(),
        old_old.begin(), old_old.end(), std::back_inserter(retained));
    r.retained_source_edges = retained.size();
    r.missing_source_edges = missing.size();
    r.extra_old_old_edges = extra.size();
    if (!missing.empty() || !extra.empty()) {
        const Edge e = !missing.empty() ? missing.front() : extra.front();
        throw std::runtime_error(std::string(!missing.empty() ?
            "missing source edge (" : "extra old-old edge (") +
            std::to_string(e.first) + "," + std::to_string(e.second) +
            "); missing=" + std::to_string(missing.size()) +
            ", extra=" + std::to_string(extra.size()));
    }
    r.old_edges_exact = true;
    if (r.new_new_edges != 0) {
        for (auto [u, v] : g.edges) {
            if (u >= OLD_N) throw std::runtime_error("new-new edge (" +
                std::to_string(u) + "," + std::to_string(v) + ")");
        }
    }
    for (int v = OLD_N; v < NEW_N; ++v) {
        if (g.adjacency[v].size() != 20) {
            throw std::runtime_error("new vertex " + std::to_string(v) +
                " has degree " + std::to_string(g.adjacency[v].size()) +
                ", expected 20");
        }
    }
    r.new_vertices_pass = true;

    // Ordinary queue BFS in the full candidate adjacency, with exactly the new
    // labels as roots. It is not a clone-owner or source-radius computation.
    std::vector<int> distance(NEW_N), queue(NEW_N);
    for (int root = OLD_N; root < NEW_N; ++root) {
        std::fill(distance.begin(), distance.end(), -1);
        int head = 0, tail = 0;
        queue[tail++] = root;
        distance[root] = 0;
        while (head < tail) {
            int v = queue[head++];
            for (int u : g.adjacency[v]) {
                if (distance[u] == -1) {
                    distance[u] = distance[v] + 1;
                    queue[tail++] = u;
                }
            }
        }
        RootResult rr{root, tail, 0, 0, {}};
        int bad_target = -1;
        for (int v = 0; v < NEW_N; ++v) {
            ++rr.distances[distance[v]];
            if (distance[v] >= 0) rr.eccentricity = std::max(rr.eccentricity, distance[v]);
            if (distance[v] >= 0 && distance[v] <= 3) ++rr.reached_within_three;
            else if (bad_target < 0) bad_target = v;
        }
        r.roots.push_back(rr);
        if (tail == NEW_N) r.connected = true;
        if (bad_target >= 0) {
            r.counterexample_root = root;
            r.counterexample_target = bad_target;
            r.counterexample_distance = distance[bad_target];
            throw std::runtime_error("new-root radius-3 failure: root=" +
                std::to_string(root) + ", target=" + std::to_string(bad_target) +
                ", full-BFS distance=" + std::to_string(distance[bad_target]) +
                " (-1 means unreachable), covered_within_three=" +
                std::to_string(rr.reached_within_three));
        }
    }
    r.new_root_radius_three_pass = true;
    r.status = "PASS";
}

int main() {
    const auto started = std::chrono::steady_clock::now();
    struct rlimit budget {20, 20};
    if (setrlimit(RLIMIT_CPU, &budget) != 0) {
        std::cerr << "could not set the 20 CPU-second budget\n";
        return 2;
    }
    Report r;
    try {
        verify(r);
    } catch (const std::exception& e) {
        r.failure = e.what();
    }
    struct rusage usage {};
    getrusage(RUSAGE_SELF, &usage);
    const double user_cpu = usage.ru_utime.tv_sec + usage.ru_utime.tv_usec / 1e6;
    const double system_cpu = usage.ru_stime.tv_sec + usage.ru_stime.tv_usec / 1e6;
    const double wall = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started).count();
    std::ofstream json(OUTDIR + "INDEPENDENT_ACCEPTANCE.json");
    json << std::boolalpha << std::fixed << std::setprecision(6)
         << "{\n  \"status\": " << json_string(r.status)
         << ",\n  \"scope\": \"independent literal graph acceptance, inherited old-old diameter bound\""
         << ",\n  \"source_literal\": " << json_string(SOURCE)
         << ",\n  \"candidate_literal\": " << json_string(CANDIDATE)
         << ",\n  \"source_order\": " << r.source_n
         << ",\n  \"source_edge_count\": " << r.source_m
         << ",\n  \"source_degree_histogram\": " << histogram_json(r.source_degrees)
         << ",\n  \"candidate_order\": " << r.candidate_n
         << ",\n  \"candidate_edge_count\": " << r.candidate_m
         << ",\n  \"candidate_degree_histogram\": " << histogram_json(r.candidate_degrees)
         << ",\n  \"candidate_old_degree_histogram\": " << histogram_json(r.old_degrees)
         << ",\n  \"candidate_new_degree_histogram\": " << histogram_json(r.new_degrees)
         << ",\n  \"candidate_max_degree\": " << r.candidate_max_degree
         << ",\n  \"source_literal_header_count_simple_pass\": " << r.source_literal_pass
         << ",\n  \"candidate_literal_header_count_simple_pass\": " << r.candidate_literal_pass
         << ",\n  \"candidate_undirected_reciprocal_adjacency_pass\": " << r.undirected
         << ",\n  \"degree_bound_pass\": " << r.degree_pass
         << ",\n  \"candidate_old_old_edge_count\": " << r.old_old_edges
         << ",\n  \"retained_source_edge_count\": " << r.retained_source_edges
         << ",\n  \"missing_source_edge_count\": " << r.missing_source_edges
         << ",\n  \"extra_old_old_edge_count\": " << r.extra_old_old_edges
         << ",\n  \"old_old_edges_exactly_source_pass\": " << r.old_edges_exact
         << ",\n  \"new_new_edge_count\": " << r.new_new_edges
         << ",\n  \"new_vertices_all_degree_twenty_only_old_neighbors_pass\": " << r.new_vertices_pass
         << ",\n  \"connected\": " << r.connected
         << ",\n  \"new_root_bfs_count\": " << r.roots.size()
         << ",\n  \"old_root_bfs_count\": 0"
         << ",\n  \"bfs_graph_order\": " << r.candidate_n
         << ",\n  \"all_new_root_radius_three_pass\": " << r.new_root_radius_three_pass
         << ",\n  \"old_old_distance_bound\": \"inherited from supplied accepted source D3 and literal preservation of all 38400 source edges; zero old-root BFS\""
         << ",\n  \"diameter_upper_bound\": " << (r.status == "PASS" ? "3" : "null")
         << ",\n  \"diameter_two_order_bound_at_degree_23\": 530"
         << ",\n  \"exact_diameter\": " << (r.status == "PASS" ? "3" : "null")
         << ",\n  \"failure\": " << (r.failure.empty() ? "null" : json_string(r.failure))
         << ",\n  \"counterexample_root\": " << r.counterexample_root
         << ",\n  \"counterexample_target\": " << r.counterexample_target
         << ",\n  \"counterexample_full_bfs_distance\": " << r.counterexample_distance
         << ",\n  \"worker_count\": 1"
         << ",\n  \"cpu_budget_seconds\": 20"
         << ",\n  \"actual_cpu_seconds\": " << user_cpu + system_cpu
         << ",\n  \"actual_user_cpu_seconds\": " << user_cpu
         << ",\n  \"actual_system_cpu_seconds\": " << system_cpu
         << ",\n  \"actual_wall_seconds\": " << wall
         << ",\n  \"producer_inputs_not_read\": [\"generator/code\",\"recipe\",\"owner\",\"coverage cache\",\"matrix certificate\",\"GRAPH_RESULT\",\"RECIPE\",\"TERMINAL\"]"
         << ",\n  \"solver_used\": false,\n  \"lean_run\": false,\n  \"public_record_claim\": false"
         << ",\n  \"new_root_results\": [\n";
    for (std::size_t i = 0; i < r.roots.size(); ++i) {
        const auto& rr = r.roots[i];
        json << "    {\"root\":" << rr.root << ",\"reached\":" << rr.reached
             << ",\"reached_within_three\":" << rr.reached_within_three
             << ",\"eccentricity\":" << rr.eccentricity
             << ",\"distance_histogram\":" << histogram_json(rr.distances) << '}';
        if (i + 1 != r.roots.size()) json << ',';
        json << '\n';
    }
    json << "  ]\n}\n";
    std::ofstream summary(OUTDIR + "SUMMARY.md");
    summary << std::fixed << std::setprecision(6)
        << "# Independent literal acceptance: " << r.status << "\n\n"
        << "Candidate: order " << r.candidate_n << ", " << r.candidate_m
        << " edges, maximum degree " << r.candidate_max_degree << ".\n\n"
        << "Degree histogram: `" << histogram_json(r.candidate_degrees)
        << "`; old: `" << histogram_json(r.old_degrees) << "`; new: `"
        << histogram_json(r.new_degrees) << "`.\n\n"
        << "Literal old-old edges: " << r.old_old_edges << "; retained source edges: "
        << r.retained_source_edges << "; missing source edges: " << r.missing_source_edges
        << "; extra old-old edges: " << r.extra_old_old_edges
        << "; new-new edges: " << r.new_new_edges << ".\n\n"
        << "Ordinary complete-graph BFS roots: " << r.roots.size()
        << " new roots, 0 old roots; candidate labels 0..4335.\n\n";
    if (r.status == "PASS") {
        summary << "All 496 new roots reached all 4336 vertices within 3 steps; this also proves connectedness. "
            << "Both files passed literal header/count/range/simplicity checks. Reciprocal adjacency passed. "
            << "Every new vertex has degree 20, and every neighbor is old.\n\n"
            << "The previously accepted source diameter bound and exact preservation of all 38400 old edges "
            << "give old-old distance at most 3 without rerunning old roots. Combined with the new-root BFS "
            << "this proves diameter at most 3. Since 4336 > 23^2+1 = 530, degree-23 radius-2 counting "
            << "excludes diameter at most 2. Therefore the candidate has diameter exactly 3.\n\n";
    } else {
        summary << "Concrete failure: " << r.failure << "\n\n";
    }
    summary << "One worker; acceptance CPU " << user_cpu + system_cpu
        << " seconds (user " << user_cpu << ", system " << system_cpu << "); wall "
        << wall << " seconds; CPU budget 20 seconds.\n\n"
        << "Graph data read: only the two literal edge tables named in PRED.md. "
        << "Producer generator/code, recipe, owner, coverage cache, matrix certificate, GRAPH_RESULT, "
        << "RECIPE, and TERMINAL were not read. No solver, Lean, installation, hashes, checksums, "
        << "or artifact manifest. No public record claim.\n";
    if (!json || !summary) {
        std::cerr << "could not write independent reports\n";
        return 2;
    }
    std::cout << r.status << " n=" << r.candidate_n << " m=" << r.candidate_m
        << " maxdeg=" << r.candidate_max_degree << " newroots=" << r.roots.size()
        << " oldroots=0 retained=" << r.retained_source_edges
        << " cpu=" << std::fixed << std::setprecision(6) << user_cpu + system_cpu << '\n';
    if (!r.failure.empty()) std::cout << r.failure << '\n';
    return r.status == "PASS" ? 0 : 1;
}
