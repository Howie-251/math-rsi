#include <algorithm>
#include <array>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using Edge = std::pair<int, int>;
struct LiteralGraph {
    int n;
    long long m;
    std::vector<Edge> edges;
};

LiteralGraph read_literal(const std::string& path, int expected_n, long long expected_m) {
    std::ifstream input(path);
    if (!input) throw std::runtime_error("cannot open literal input: " + path);
    std::string line, extra;
    if (!std::getline(input, line)) throw std::runtime_error("missing literal header");
    LiteralGraph g{0, 0, {}};
    std::istringstream header(line);
    if (!(header >> g.n >> g.m) || (header >> extra))
        throw std::runtime_error("literal header must contain exactly n and m");
    if (g.n != expected_n || g.m != expected_m)
        throw std::runtime_error("literal header differs from frozen expected n/m");
    g.edges.reserve(static_cast<std::size_t>(g.m));
    long long line_number = 1;
    while (std::getline(input, line)) {
        ++line_number;
        if (line.find_first_not_of(" \t\r\n") == std::string::npos) continue;
        std::istringstream row(line);
        int u = -1, v = -1;
        if (!(row >> u >> v) || (row >> extra))
            throw std::runtime_error("malformed literal edge at line " + std::to_string(line_number));
        if (u < 0 || u >= g.n || v < 0 || v >= g.n)
            throw std::runtime_error("out-of-range endpoint at line " + std::to_string(line_number));
        if (u == v) throw std::runtime_error("literal loop at line " + std::to_string(line_number));
        if (u > v) std::swap(u, v);
        g.edges.emplace_back(u, v);
    }
    if (!input.eof()) throw std::runtime_error("literal read error");
    if (static_cast<long long>(g.edges.size()) != g.m)
        throw std::runtime_error("actual literal edge count differs from header");
    std::sort(g.edges.begin(), g.edges.end());
    if (std::adjacent_find(g.edges.begin(), g.edges.end()) != g.edges.end())
        throw std::runtime_error("repeated unordered literal edge");
    return g;
}

// Its two graph inputs are literal edge lists only. No old root is searched.
int main(int argc, char** argv) {
    const std::clock_t cpu_start = std::clock();
    const auto wall_start = std::chrono::steady_clock::now();
    if (argc != 4) {
        std::cerr << "usage: check_literal SOURCE_EDGES CANDIDATE_EDGES OUTPUT_DIRECTORY\n";
        return 2;
    }
    const std::string output = argv[3];
    try {
        const LiteralGraph source = read_literal(argv[1], 7242, 90525);
        const LiteralGraph graph = read_literal(argv[2], 7531, 97750);
        std::vector<Edge> old_old;
        old_old.reserve(source.edges.size());
        long long old_new = 0, new_new = 0;
        std::vector<std::vector<int>> adjacency(graph.n);
        for (const Edge& edge : graph.edges) {
            if (edge.second < source.n) old_old.push_back(edge);
            else if (edge.first < source.n) ++old_new;
            else ++new_new;
            adjacency[edge.first].push_back(edge.second);
            adjacency[edge.second].push_back(edge.first);
        }
        long long missing_old_edges = 0, extra_old_edges = 0;
        Edge first_missing{-1, -1}, first_extra{-1, -1};
        std::size_t i = 0, j = 0;
        while (i < source.edges.size() || j < old_old.size()) {
            if (j == old_old.size() || (i < source.edges.size() && source.edges[i] < old_old[j])) {
                if (missing_old_edges++ == 0) first_missing = source.edges[i];
                ++i;
            } else if (i == source.edges.size() || old_old[j] < source.edges[i]) {
                if (extra_old_edges++ == 0) first_extra = old_old[j];
                ++j;
            } else {
                ++i;
                ++j;
            }
        }
        const bool old_old_exact = missing_old_edges == 0 && extra_old_edges == 0;
        int min_degree = graph.n, max_degree = 0;
        int new_min_degree = graph.n, new_max_degree = 0;
        long long degree_sum = 0;
        std::map<int, int> degree_histogram;
        bool new_only_old_neighbors = true;
        for (int u = 0; u < graph.n; ++u) {
            auto& row = adjacency[u];
            std::sort(row.begin(), row.end());
            const int degree = static_cast<int>(row.size());
            min_degree = std::min(min_degree, degree);
            max_degree = std::max(max_degree, degree);
            degree_sum += degree;
            ++degree_histogram[degree];
            if (u >= source.n) {
                new_min_degree = std::min(new_min_degree, degree);
                new_max_degree = std::max(new_max_degree, degree);
                for (int v : row) new_only_old_neighbors = new_only_old_neighbors && v < source.n;
            }
        }
        bool reciprocal = true;
        for (int u = 0; u < graph.n; ++u)
            for (int v : adjacency[u])
                reciprocal = reciprocal && std::binary_search(adjacency[v].begin(), adjacency[v].end(), u);
        if (!reciprocal || degree_sum != 2 * graph.m)
            throw std::runtime_error("undirected adjacency check failed");
        const std::clock_t setup_end = std::clock();

        std::ofstream roots(output + "/roots.tsv");
        if (!roots) throw std::runtime_error("cannot create root records");
        roots << "root\tshell0\tshell1\tshell2\tshell3\treached_R3\tmissing_R3\tfirst_missing\teccentricity_if_covered\n";
        std::vector<int> distance(graph.n, -1), queue(graph.n);
        int roots_checked = 0, roots_passed = 0;
        int first_bad_root = -1, first_bad_target = -1;
        int min_reached = graph.n, max_reached = 0;
        int min_shell2 = graph.n, max_shell2 = 0, min_shell3 = graph.n, max_shell3 = 0;
        for (int root = source.n; root < graph.n; ++root) {
            ++roots_checked;
            std::fill(distance.begin(), distance.end(), -1);
            int head = 0, tail = 0;
            queue[tail++] = root;
            distance[root] = 0;
            std::array<int, 4> shells{1, 0, 0, 0};
            while (head < tail && distance[queue[head]] < 3) {
                const int u = queue[head++];
                for (int v : adjacency[u]) {
                    if (distance[v] == -1) {
                        distance[v] = distance[u] + 1;
                        ++shells[distance[v]];
                        queue[tail++] = v;
                    }
                }
            }
            int first_missing_target = -1, eccentricity = -1;
            if (tail == graph.n) {
                ++roots_passed;
                eccentricity = 3;
                while (eccentricity > 0 && shells[eccentricity] == 0) --eccentricity;
            } else {
                first_missing_target = static_cast<int>(std::find(distance.begin(), distance.end(), -1) - distance.begin());
                if (first_bad_root == -1) {
                    first_bad_root = root;
                    first_bad_target = first_missing_target;
                }
            }
            roots << root << '\t' << shells[0] << '\t' << shells[1] << '\t'
                  << shells[2] << '\t' << shells[3] << '\t' << tail << '\t'
                  << graph.n - tail << '\t' << first_missing_target << '\t' << eccentricity << '\n';
            min_reached = std::min(min_reached, tail);
            max_reached = std::max(max_reached, tail);
            min_shell2 = std::min(min_shell2, shells[2]);
            max_shell2 = std::max(max_shell2, shells[2]);
            min_shell3 = std::min(min_shell3, shells[3]);
            max_shell3 = std::max(max_shell3, shells[3]);
        }
        roots.close();
        if (!roots) throw std::runtime_error("root record write failed");
        const std::clock_t bfs_end = std::clock();
        const bool new_degrees_25 = new_min_degree == 25 && new_max_degree == 25;
        const bool new_roots_pass = roots_checked == 289 && roots_passed == 289;
        const bool pass = max_degree <= 26 && old_old_exact && new_new == 0
            && new_degrees_25 && new_only_old_neighbors && new_roots_pass;
        const bool inherited_old_old_bound = old_old_exact;
        const int diameter2_moore_bound = 1 + 26 + 26 * 25;
        const bool exact_diameter3 = pass && graph.n > diameter2_moore_bound;
        const double setup_cpu = static_cast<double>(setup_end - cpu_start) / CLOCKS_PER_SEC;
        const double bfs_cpu = static_cast<double>(bfs_end - setup_end) / CLOCKS_PER_SEC;
        const double total_cpu = static_cast<double>(bfs_end - cpu_start) / CLOCKS_PER_SEC;
        const double wall_seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - wall_start).count();
        std::ofstream result(output + "/INDEPENDENT_ACCEPTANCE.json");
        if (!result) throw std::runtime_error("cannot create acceptance result");
        result << std::boolalpha << std::fixed << std::setprecision(9)
               << "{\n  \"status\": \"" << (pass ? "PASS" : "FAIL") << "\",\n"
               << "  \"input_scope\": \"two literal edge lists only\",\n"
               << "  \"source_n\": " << source.n << ",\n  \"source_m\": " << source.m << ",\n"
               << "  \"actual_n\": " << graph.n << ",\n  \"actual_m\": " << graph.edges.size() << ",\n"
               << "  \"header_matches_actual\": true,\n  \"simple\": true,\n"
               << "  \"loops\": 0,\n  \"duplicate_unordered_edges\": 0,\n"
               << "  \"undirected_reciprocity\": " << reciprocal << ",\n"
               << "  \"degree_sum\": " << degree_sum << ",\n"
               << "  \"min_degree\": " << min_degree << ",\n  \"max_degree\": " << max_degree << ",\n"
               << "  \"degree_histogram\": {";
        bool first_histogram_entry = true;
        for (const auto& item : degree_histogram) {
            if (!first_histogram_entry) result << ", ";
            result << '"' << item.first << "\": " << item.second;
            first_histogram_entry = false;
        }
        result << "},\n  \"old_old_edges\": " << old_old.size() << ",\n"
               << "  \"missing_source_edges\": " << missing_old_edges << ",\n"
               << "  \"extra_old_old_edges\": " << extra_old_edges << ",\n"
               << "  \"first_missing_source_edge\": [" << first_missing.first << ", " << first_missing.second << "],\n"
               << "  \"first_extra_old_old_edge\": [" << first_extra.first << ", " << first_extra.second << "],\n"
               << "  \"old_old_edge_set_equals_source\": " << old_old_exact << ",\n"
               << "  \"old_new_edges\": " << old_new << ",\n  \"new_new_edges\": " << new_new << ",\n"
               << "  \"new_vertex_count\": " << graph.n - source.n << ",\n"
               << "  \"new_vertex_labels\": \"7242..7530\",\n"
               << "  \"new_min_degree\": " << new_min_degree << ",\n  \"new_max_degree\": " << new_max_degree << ",\n"
               << "  \"new_vertices_only_have_old_neighbors\": " << new_only_old_neighbors << ",\n"
               << "  \"inherited_source_diameter_bound\": 3,\n"
               << "  \"old_old_diameter_bound_inherited\": " << inherited_old_old_bound << ",\n"
               << "  \"old_roots_bfs_checked\": 0,\n"
               << "  \"algorithm\": \"fresh ordinary queue BFS through radius 3 from every new vertex\",\n"
               << "  \"roots_checked\": " << roots_checked << ",\n  \"roots_passed\": " << roots_passed << ",\n"
               << "  \"all_new_roots_R3_cover\": " << new_roots_pass << ",\n"
               << "  \"min_reached_R3\": " << min_reached << ",\n  \"max_reached_R3\": " << max_reached << ",\n"
               << "  \"min_shell2\": " << min_shell2 << ",\n  \"max_shell2\": " << max_shell2 << ",\n"
               << "  \"min_shell3\": " << min_shell3 << ",\n  \"max_shell3\": " << max_shell3 << ",\n"
               << "  \"first_failing_root\": " << first_bad_root << ",\n  \"first_failing_target\": " << first_bad_target << ",\n"
               << "  \"connected\": " << (inherited_old_old_bound && new_roots_pass) << ",\n"
               << "  \"diameter2_maxdegree26_Moore_bound\": " << diameter2_moore_bound << ",\n"
               << "  \"exact_diameter\": " << (exact_diameter3 ? 3 : -1) << ",\n"
               << "  \"root_records\": \"roots.tsv\",\n  \"cpu_seconds\": " << total_cpu << ",\n"
               << "  \"public_record_claim\": false\n}\n";
        result.close();
        if (!result) throw std::runtime_error("acceptance result write failed");
        std::ofstream cpu(output + "/ACTUAL_CPU.json");
        cpu << std::fixed << std::setprecision(9)
            << "{\n  \"measurement\": \"C++ std::clock process CPU\",\n"
            << "  \"workers\": 1,\n  \"cpu_hard_limit_seconds\": 30,\n"
            << "  \"literal_parse_comparison_setup_cpu_seconds\": " << setup_cpu << ",\n"
            << "  \"new_roots_bfs_cpu_seconds\": " << bfs_cpu << ",\n"
            << "  \"checker_cpu_seconds\": " << total_cpu << ",\n"
            << "  \"checker_wall_seconds\": " << wall_seconds << "\n}\n";
        cpu.close();
        if (!cpu) throw std::runtime_error("CPU result write failed");
        std::cout << (pass ? "PASS" : "FAIL") << " n=" << graph.n << " m=" << graph.m
                  << " degree=" << min_degree << ".." << max_degree
                  << " old_missing=" << missing_old_edges << " old_extra=" << extra_old_edges
                  << " new_new=" << new_new << " new_roots=" << roots_passed << '/' << roots_checked
                  << " old_roots=0 exactD=" << (exact_diameter3 ? 3 : -1)
                  << " cpu=" << std::fixed << std::setprecision(9) << total_cpu << '\n';
        if (first_bad_root != -1)
            std::cout << "counterexample root=" << first_bad_root << " target=" << first_bad_target << '\n';
        return pass ? 0 : 1;
    } catch (const std::exception& error) {
        std::cerr << "FAIL: " << error.what() << '\n';
        return 2;
    }
}
