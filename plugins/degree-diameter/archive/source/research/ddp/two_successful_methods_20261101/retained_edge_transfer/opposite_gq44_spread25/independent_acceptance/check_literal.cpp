#include <algorithm>
#include <array>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

// Independent checker. Its sole graph input is the supplied literal edge list.
// Each root uses a fresh ordinary queue BFS, scanning all vertices at depth < 3.
int main(int argc, char** argv) {
    const std::clock_t cpu_start = std::clock();
    const auto wall_start = std::chrono::steady_clock::now();
    if (argc != 3) {
        std::cerr << "usage: check_literal EDGE_FILE OUTPUT_DIRECTORY\n";
        return 2;
    }
    const std::string output = argv[2];
    try {
        std::ifstream input(argv[1]);
        if (!input) throw std::runtime_error("cannot open literal input");
        std::string line, extra;
        if (!std::getline(input, line)) throw std::runtime_error("missing header");
        std::istringstream header(line);
        int n = 0;
        long long header_m = 0;
        if (!(header >> n >> header_m) || (header >> extra))
            throw std::runtime_error("header must contain exactly n and m");
        if (n != 7242 || header_m != 90525)
            throw std::runtime_error("header differs from frozen expected 7242/90525");
        std::vector<std::pair<int, int>> edges;
        edges.reserve(static_cast<std::size_t>(header_m));
        long long line_number = 1;
        while (std::getline(input, line)) {
            ++line_number;
            if (line.find_first_not_of(" \t\r\n") == std::string::npos) continue;
            std::istringstream row(line);
            int u = -1, v = -1;
            if (!(row >> u >> v) || (row >> extra))
                throw std::runtime_error("malformed edge at line " + std::to_string(line_number));
            if (u < 0 || u >= n || v < 0 || v >= n)
                throw std::runtime_error("out-of-range endpoint at line " + std::to_string(line_number));
            if (u == v)
                throw std::runtime_error("loop at line " + std::to_string(line_number));
            if (u > v) std::swap(u, v);
            edges.emplace_back(u, v);
        }
        if (!input.eof()) throw std::runtime_error("literal input read error");
        if (static_cast<long long>(edges.size()) != header_m)
            throw std::runtime_error("actual edge count differs from header");
        std::sort(edges.begin(), edges.end());
        if (std::adjacent_find(edges.begin(), edges.end()) != edges.end())
            throw std::runtime_error("repeated unordered edge");

        std::vector<std::vector<int>> adjacency(n);
        for (const auto& edge : edges) {
            adjacency[edge.first].push_back(edge.second);
            adjacency[edge.second].push_back(edge.first);
        }
        int min_degree = n, max_degree = 0;
        long long degree_sum = 0;
        for (auto& row : adjacency) {
            std::sort(row.begin(), row.end());
            const int degree = static_cast<int>(row.size());
            min_degree = std::min(min_degree, degree);
            max_degree = std::max(max_degree, degree);
            degree_sum += degree;
        }
        bool reciprocal = true;
        for (int u = 0; u < n; ++u)
            for (int v : adjacency[u])
                reciprocal = reciprocal && std::binary_search(adjacency[v].begin(), adjacency[v].end(), u);
        if (!reciprocal || degree_sum != 2 * header_m)
            throw std::runtime_error("undirected adjacency check failed");

        std::vector<int> distance(n, -1), queue(n);
        int head = 0, tail = 0;
        queue[tail++] = 0;
        distance[0] = 0;
        while (head < tail) {
            const int u = queue[head++];
            for (int v : adjacency[u]) {
                if (distance[v] == -1) {
                    distance[v] = distance[u] + 1;
                    queue[tail++] = v;
                }
            }
        }
        const int connected_reached = tail;
        const bool connected = connected_reached == n;
        const std::clock_t setup_end = std::clock();

        std::ofstream roots(output + "/roots.tsv");
        if (!roots) throw std::runtime_error("cannot create root records");
        roots << "root\tshell0\tshell1\tshell2\tshell3\treached_R3\tmissing_R3\tfirst_missing\teccentricity_if_covered\n";
        int roots_passed = 0, first_bad_root = -1, first_bad_target = -1;
        int min_reached = n, max_reached = 0;
        int min_shell2 = n, max_shell2 = 0, min_shell3 = n, max_shell3 = 0;
        for (int root = 0; root < n; ++root) {
            std::fill(distance.begin(), distance.end(), -1);
            head = tail = 0;
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
            int first_missing = -1;
            if (tail == n) {
                ++roots_passed;
            } else {
                first_missing = static_cast<int>(std::find(distance.begin(), distance.end(), -1) - distance.begin());
                if (first_bad_root == -1) {
                    first_bad_root = root;
                    first_bad_target = first_missing;
                }
            }
            int eccentricity = -1;
            if (tail == n) {
                eccentricity = 3;
                while (eccentricity > 0 && shells[eccentricity] == 0) --eccentricity;
            }
            roots << root << '\t' << shells[0] << '\t' << shells[1] << '\t'
                  << shells[2] << '\t' << shells[3] << '\t' << tail << '\t'
                  << n - tail << '\t' << first_missing << '\t' << eccentricity << '\n';
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
        const bool radius3_pass = roots_passed == n;
        const bool pass = connected && max_degree <= 25 && radius3_pass;
        const int diameter2_moore_bound = 1 + 25 + 25 * 24;
        const bool diameter3_exact = pass && n > diameter2_moore_bound;
        const double setup_cpu = static_cast<double>(setup_end - cpu_start) / CLOCKS_PER_SEC;
        const double bfs_cpu = static_cast<double>(bfs_end - setup_end) / CLOCKS_PER_SEC;
        const double total_cpu = static_cast<double>(bfs_end - cpu_start) / CLOCKS_PER_SEC;
        const double wall_seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - wall_start).count();

        std::ofstream result(output + "/INDEPENDENT_ACCEPTANCE.json");
        if (!result) throw std::runtime_error("cannot create acceptance result");
        result << std::boolalpha << std::fixed << std::setprecision(9)
               << "{\n"
               << "  \"status\": \"" << (pass ? "PASS" : "FAIL") << "\",\n"
               << "  \"input\": \"graph_d25_D3_n7242.edges\",\n"
               << "  \"input_scope\": \"literal edge list only; no producer metadata or old graph\",\n"
               << "  \"header_n\": " << n << ",\n"
               << "  \"header_m\": " << header_m << ",\n"
               << "  \"actual_n\": " << adjacency.size() << ",\n"
               << "  \"actual_m\": " << edges.size() << ",\n"
               << "  \"header_matches_actual\": true,\n"
               << "  \"endpoint_labels\": \"0..7241\",\n"
               << "  \"simple\": true,\n"
               << "  \"loops\": 0,\n"
               << "  \"duplicate_unordered_edges\": 0,\n"
               << "  \"undirected_reciprocity\": " << reciprocal << ",\n"
               << "  \"degree_sum\": " << degree_sum << ",\n"
               << "  \"min_degree\": " << min_degree << ",\n"
               << "  \"max_degree\": " << max_degree << ",\n"
               << "  \"degree_bound\": 25,\n"
               << "  \"regular_25\": " << (min_degree == 25 && max_degree == 25) << ",\n"
               << "  \"connected\": " << connected << ",\n"
               << "  \"connectivity_root\": 0,\n"
               << "  \"connectivity_reached\": " << connected_reached << ",\n"
               << "  \"algorithm\": \"fresh ordinary queue BFS from each root, scanning depths 0,1,2\",\n"
               << "  \"radius\": 3,\n"
               << "  \"roots_checked\": " << n << ",\n"
               << "  \"roots_passed\": " << roots_passed << ",\n"
               << "  \"all_roots_R3_cover\": " << radius3_pass << ",\n"
               << "  \"min_reached_R3\": " << min_reached << ",\n"
               << "  \"max_reached_R3\": " << max_reached << ",\n"
               << "  \"min_shell2\": " << min_shell2 << ",\n"
               << "  \"max_shell2\": " << max_shell2 << ",\n"
               << "  \"min_shell3\": " << min_shell3 << ",\n"
               << "  \"max_shell3\": " << max_shell3 << ",\n"
               << "  \"first_failing_root\": " << first_bad_root << ",\n"
               << "  \"first_failing_target\": " << first_bad_target << ",\n"
               << "  \"diameter2_maxdegree25_Moore_bound\": " << diameter2_moore_bound << ",\n"
               << "  \"exact_diameter\": " << (diameter3_exact ? 3 : -1) << ",\n"
               << "  \"root_records\": \"roots.tsv\",\n"
               << "  \"cpu_seconds\": " << total_cpu << ",\n"
               << "  \"public_record_claim\": false\n"
               << "}\n";
        result.close();
        if (!result) throw std::runtime_error("acceptance result write failed");
        std::ofstream cpu(output + "/ACTUAL_CPU.json");
        cpu << std::fixed << std::setprecision(9)
            << "{\n  \"measurement\": \"C++ std::clock process CPU; setup and all-root BFS separately measured\",\n"
            << "  \"workers\": 1,\n  \"cpu_hard_limit_seconds\": 30,\n"
            << "  \"setup_cpu_seconds\": " << setup_cpu << ",\n"
            << "  \"all_roots_bfs_cpu_seconds\": " << bfs_cpu << ",\n"
            << "  \"checker_cpu_seconds\": " << total_cpu << ",\n"
            << "  \"checker_wall_seconds\": " << wall_seconds << "\n}\n";
        cpu.close();
        if (!cpu) throw std::runtime_error("CPU result write failed");
        std::cout << (pass ? "PASS" : "FAIL") << " n=" << n << " m=" << edges.size()
                  << " degree=" << min_degree << ".." << max_degree
                  << " roots=" << roots_passed << '/' << n
                  << " exactD=" << (diameter3_exact ? 3 : -1)
                  << " cpu=" << std::fixed << std::setprecision(9) << total_cpu << '\n';
        if (first_bad_root != -1)
            std::cout << "counterexample root=" << first_bad_root << " target=" << first_bad_target << '\n';
        return pass ? 0 : 1;
    } catch (const std::exception& error) {
        std::cerr << "FAIL: " << error.what() << '\n';
        return 2;
    }
}
