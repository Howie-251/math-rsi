// Independent acceptance from literal edge files only. No ball caches/selectors.
// This source is prepared only; compile/run only after a real SAT candidate exists.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <optional>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using Vertex = std::uint32_t;
using Edge = std::pair<Vertex, Vertex>;
constexpr Vertex OLD_N = 94186;
constexpr Vertex NEW_N = 94188;
constexpr std::uint64_t OLD_M = 657452;

struct GraphFile {
    std::vector<Edge> edges;
    bool header_present = false;
    bool header_count_matches = true;
    bool simple = true;
    std::uint64_t self_loops = 0;
    std::uint64_t duplicate_edges = 0;
};

static std::string quoted(const std::string& s) {
    std::string out = "\"";
    for (unsigned char c : s) {
        if (c == '\\' || c == '"') { out += '\\'; out += char(c); }
        else if (c == '\n') out += "\\n";
        else if (c == '\r') out += "\\r";
        else if (c == '\t') out += "\\t";
        else if (c < 32) out += '?';
        else out += char(c);
    }
    return out + '"';
}

// Accept plain u v rows, with optional first numeric row n m and # comments.
// Header recognition is unambiguous: a valid endpoint is always strictly below n.
static GraphFile read_edges(const std::string& path, Vertex n) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("cannot open " + path);
    GraphFile g;
    bool first_data = true;
    std::optional<std::uint64_t> declared_m;
    std::string line;
    std::uint64_t line_no = 0;
    while (std::getline(in, line)) {
        ++line_no;
        const auto comment = line.find('#');
        if (comment != std::string::npos) line.resize(comment);
        std::istringstream row(line);
        row >> std::ws;
        if (row.eof()) continue;
        std::uint64_t a, b;
        std::string extra;
        if (!(row >> a >> b) || (row >> extra))
            throw std::runtime_error("expected two unsigned integers at " + path + ":" + std::to_string(line_no));
        if (first_data && a == n) {
            g.header_present = true;
            declared_m = b;
            first_data = false;
            continue;
        }
        first_data = false;
        if (a >= n || b >= n)
            throw std::runtime_error("endpoint outside literal vertex range at " + path + ":" + std::to_string(line_no));
        Vertex u = static_cast<Vertex>(a), v = static_cast<Vertex>(b);
        if (u == v) ++g.self_loops;
        if (u > v) std::swap(u, v);
        g.edges.emplace_back(u, v);
    }
    if (in.bad()) throw std::runtime_error("read error in " + path);
    if (declared_m) g.header_count_matches = *declared_m == g.edges.size();
    std::sort(g.edges.begin(), g.edges.end());
    for (std::size_t i = 1; i < g.edges.size(); ++i)
        if (g.edges[i] == g.edges[i - 1]) ++g.duplicate_edges;
    g.simple = g.self_loops == 0 && g.duplicate_edges == 0;
    return g;
}

static std::vector<std::uint32_t> degrees(const std::vector<Edge>& edges, Vertex n) {
    std::vector<std::uint32_t> d(n, 0);
    for (const auto& e : edges) { ++d[e.first]; ++d[e.second]; }
    return d;
}

static std::vector<std::uint64_t> histogram(const std::vector<std::uint32_t>& d) {
    const std::uint32_t max_d = *std::max_element(d.begin(), d.end());
    std::vector<std::uint64_t> h(max_d + 1, 0);
    for (const auto x : d) ++h[x];
    return h;
}

template<class T> static void array_json(const std::vector<T>& xs) {
    std::cout << '[';
    for (std::size_t i = 0; i < xs.size(); ++i) { if (i) std::cout << ','; std::cout << xs[i]; }
    std::cout << ']';
}

struct BFSResult {
    Vertex root = 0;
    std::uint64_t reached = 0;
    std::uint64_t unreachable = 0;
    std::uint64_t old_targets_beyond5_or_unreachable = 0;
    std::uint64_t all_targets_beyond5_or_unreachable = 0;
    int max_finite_distance = 0;
    std::vector<std::uint64_t> distance_histogram;
};

static BFSResult bfs(const std::vector<std::vector<Vertex>>& adj, Vertex root) {
    std::vector<int> d(adj.size(), -1);
    std::vector<Vertex> queue;
    queue.reserve(adj.size());
    d[root] = 0;
    queue.push_back(root);
    for (std::size_t head = 0; head < queue.size(); ++head) {
        const Vertex v = queue[head];
        for (const Vertex w : adj[v]) if (d[w] < 0) {
            d[w] = d[v] + 1;
            queue.push_back(w);
        }
    }
    BFSResult r;
    r.root = root;
    r.reached = queue.size();
    r.unreachable = adj.size() - queue.size();
    for (const int x : d) if (x >= 0) r.max_finite_distance = std::max(r.max_finite_distance, x);
    r.distance_histogram.assign(static_cast<std::size_t>(r.max_finite_distance) + 1, 0);
    for (Vertex v = 0; v < adj.size(); ++v) {
        if (d[v] >= 0) ++r.distance_histogram[static_cast<std::size_t>(d[v])];
        if (d[v] < 0 || d[v] > 5) {
            ++r.all_targets_beyond5_or_unreachable;
            if (v < OLD_N) ++r.old_targets_beyond5_or_unreachable;
        }
    }
    return r;
}

static void bfs_json(const BFSResult& r) {
    std::cout << "{\"root\":" << r.root
              << ",\"reached\":" << r.reached
              << ",\"unreachable\":" << r.unreachable
              << ",\"eccentricity\":";
    if (r.unreachable) std::cout << "null"; else std::cout << r.max_finite_distance;
    std::cout << ",\"max_finite_distance\":" << r.max_finite_distance
              << ",\"distance_histogram_by_distance\":";
    array_json(r.distance_histogram);
    std::cout << ",\"old_targets_beyond5_or_unreachable\":" << r.old_targets_beyond5_or_unreachable
              << ",\"all_targets_beyond5_or_unreachable\":" << r.all_targets_beyond5_or_unreachable
              << '}';
}

int main(int argc, char** argv) {
    std::cout << std::boolalpha;
    try {
        if (argc != 3)
            throw std::runtime_error("usage: check_candidate SOURCE94186.edges CANDIDATE94188.edges");
        const GraphFile source = read_edges(argv[1], OLD_N);
        const GraphFile candidate = read_edges(argv[2], NEW_N);
        std::vector<Edge> old_old;
        old_old.reserve(source.edges.size());
        for (const auto& e : candidate.edges)
            if (e.second < OLD_N) old_old.push_back(e);
        // Candidate edges are sorted canonical unsigned pairs, so old_old is sorted too.
        const bool old_edges_equal = old_old == source.edges;
        const auto source_degree = degrees(source.edges, OLD_N);
        const auto candidate_degree = degrees(candidate.edges, NEW_N);
        const auto source_max = *std::max_element(source_degree.begin(), source_degree.end());
        const auto candidate_max = *std::max_element(candidate_degree.begin(), candidate_degree.end());
        const bool helper_edge = std::binary_search(candidate.edges.begin(), candidate.edges.end(), Edge{OLD_N, OLD_N + 1});
        const bool source_contract = source.edges.size() == OLD_M && source.simple && source.header_count_matches && source_max <= 14;
        const bool structure_ok = source_contract && candidate.simple && candidate.header_count_matches &&
                                  candidate_max <= 14 && old_edges_equal && helper_edge;
        std::vector<BFSResult> checks;
        if (structure_ok) {
            std::vector<std::vector<Vertex>> adj(NEW_N);
            for (Vertex v = 0; v < NEW_N; ++v) adj[v].reserve(candidate_degree[v]);
            for (const auto& e : candidate.edges) {
                adj[e.first].push_back(e.second);
                adj[e.second].push_back(e.first);
            }
            // Exactly two BFS roots. Connectivity is obtained from the first traversal.
            checks.push_back(bfs(adj, OLD_N));
            checks.push_back(bfs(adj, OLD_N + 1));
        }
        const bool connected = checks.size() == 2 && checks[0].reached == NEW_N;
        const bool both_new_roots_D5 = checks.size() == 2 &&
            checks[0].all_targets_beyond5_or_unreachable == 0 &&
            checks[1].all_targets_beyond5_or_unreachable == 0;
        const bool accepted = structure_ok && connected && both_new_roots_D5;
        std::cout << "{\"status\":" << quoted(accepted ? "ACCEPTED" : "REJECTED")
                  << ",\"source_n\":" << OLD_N << ",\"source_edges\":" << source.edges.size()
                  << ",\"source_expected_edges\":" << OLD_M
                  << ",\"source_literal_contract_pass\":" << source_contract
                  << ",\"source_simple\":" << source.simple
                  << ",\"source_max_degree\":" << source_max
                  << ",\"source_D5_assumed_prevalidated\":true,\"source_D5_reverified\":false"
                  << ",\"candidate_n\":" << NEW_N << ",\"candidate_edges\":" << candidate.edges.size()
                  << ",\"candidate_simple\":" << candidate.simple
                  << ",\"candidate_self_loops\":" << candidate.self_loops
                  << ",\"candidate_duplicate_edges\":" << candidate.duplicate_edges
                  << ",\"candidate_header_count_matches\":" << candidate.header_count_matches
                  << ",\"candidate_max_degree\":" << candidate_max
                  << ",\"candidate_degree_histogram_by_degree\":";
        array_json(histogram(candidate_degree));
        std::cout << ",\"helper_degrees\":[" << candidate_degree[OLD_N] << ',' << candidate_degree[OLD_N + 1] << ']'
                  << ",\"helpers_adjacent\":" << helper_edge
                  << ",\"candidate_old_old_edges\":" << old_old.size()
                  << ",\"old_old_edge_set_exactly_preserved\":" << old_edges_equal
                  << ",\"old_old_D5_inherited_from_prevalidated_source\":" << (source_contract && old_edges_equal)
                  << ",\"structure_pass\":" << structure_ok
                  << ",\"connected\":" << connected
                  << ",\"new_root_BFS_runs\":" << checks.size()
                  << ",\"old_root_BFS_runs\":0,\"new_root_checks\":[";
        for (std::size_t i = 0; i < checks.size(); ++i) { if (i) std::cout << ','; bfs_json(checks[i]); }
        std::cout << "],\"both_new_roots_eccentricity_at_most5\":" << both_new_roots_D5
                  << ",\"diameter_at_most5_by_inheritance_and_two_new_roots\":" << accepted
                  << "}\n";
        return accepted ? 0 : 1;
    } catch (const std::exception& e) {
        std::cout << "{\"status\":\"INPUT_ERROR\",\"error\":" << quoted(e.what())
                  << ",\"accepted\":false,\"old_root_BFS_runs\":0}\n";
        return 2;
    }
}
