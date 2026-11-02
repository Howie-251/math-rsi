#include <algorithm>
#include <array>
#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <sys/resource.h>
#include <utility>
#include <vector>

// Standalone literal reader and ordinary queue BFS. No producer inputs or
// previous source graph are consulted.
constexpr int N = 6160;
constexpr long long M = 73920;
constexpr int DEGREE_BOUND = 24;
const std::string INPUT =
    "research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq35_spread24/graph_d24_D3_n6160.edges";
const std::string OUTDIR =
    "research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq35_spread24/independent_acceptance/";
using Edge = std::pair<int, int>;
using Histogram = std::map<int, int>;

struct RootResult {
    int root;
    int reached;
    int within_three;
    int eccentricity;
    std::array<int, 4> first_four_distance_counts;
};

struct Report {
    std::string status = "FAIL";
    std::string failure;
    bool header_pass = false;
    bool literal_count_pass = false;
    bool simple = false;
    bool undirected = false;
    bool degree_pass = false;
    bool connected = false;
    int n = 0;
    long long declared_m = 0;
    long long literal_m = 0;
    int max_degree = 0;
    Histogram degrees;
    Histogram eccentricities;
    std::vector<RootResult> roots;
    int bad_root = -1;
    int bad_target = -1;
    int bad_distance = -2;
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
    for (const auto& [value, count] : h) {
        if (!first) out << ',';
        first = false;
        out << json_string(std::to_string(value)) << ':' << count;
    }
    out << '}';
    return out.str();
}

std::pair<long long, long long> parse_pair(const std::string& line, int number) {
    std::istringstream in(line);
    long long u, v;
    std::string extra;
    if (!(in >> u >> v) || (in >> extra))
        throw std::runtime_error("malformed literal pair at line " + std::to_string(number));
    return {u, v};
}

void verify(Report& r) {
    std::ifstream in(INPUT);
    if (!in) throw std::runtime_error("cannot open candidate literal edge table");
    std::string line;
    if (!std::getline(in, line)) throw std::runtime_error("empty candidate literal file");
    const auto [n, m] = parse_pair(line, 1);
    if (n != N || m != M)
        throw std::runtime_error("literal header " + std::to_string(n) + " " +
            std::to_string(m) + "; expected 6160 73920");
    r.n = static_cast<int>(n);
    r.declared_m = m;
    r.header_pass = true;
    std::vector<Edge> edges;
    edges.reserve(M);
    int number = 1;
    while (std::getline(in, line)) {
        ++number;
        if (line.find_first_not_of(" \t\r") == std::string::npos) continue;
        auto [u, v] = parse_pair(line, number);
        if (u < 0 || v < 0 || u >= N || v >= N)
            throw std::runtime_error("out-of-range edge (" + std::to_string(u) +
                "," + std::to_string(v) + ") at line " + std::to_string(number));
        if (u == v)
            throw std::runtime_error("self-loop at vertex " + std::to_string(u) +
                " on line " + std::to_string(number));
        if (u > v) std::swap(u, v);
        edges.emplace_back(static_cast<int>(u), static_cast<int>(v));
    }
    if (in.bad()) throw std::runtime_error("literal file read error");
    r.literal_m = edges.size();
    if (r.literal_m != M)
        throw std::runtime_error("literal edge count " + std::to_string(r.literal_m) +
            "; expected 73920");
    r.literal_count_pass = true;
    std::sort(edges.begin(), edges.end());
    const auto duplicate = std::adjacent_find(edges.begin(), edges.end());
    if (duplicate != edges.end())
        throw std::runtime_error("repeated unordered edge (" +
            std::to_string(duplicate->first) + "," +
            std::to_string(duplicate->second) + ")");
    r.simple = true;
    std::vector<std::vector<int>> adjacency(N);
    for (const auto& [u, v] : edges) {
        adjacency[u].push_back(v);
        adjacency[v].push_back(u);
    }
    for (int v = 0; v < N; ++v) {
        ++r.degrees[adjacency[v].size()];
        for (int u : adjacency[v]) {
            if (std::count(adjacency[u].begin(), adjacency[u].end(), v) != 1)
                throw std::runtime_error("nonreciprocal adjacency at (" +
                    std::to_string(v) + "," + std::to_string(u) + ")");
        }
    }
    r.undirected = true;
    r.max_degree = r.degrees.rbegin()->first;
    for (int v = 0; v < N; ++v) {
        if (adjacency[v].size() > DEGREE_BOUND)
            throw std::runtime_error("degree bound exceeded at vertex " +
                std::to_string(v) + ": degree " +
                std::to_string(adjacency[v].size()));
    }
    r.degree_pass = true;

    std::vector<int> distance(N), queue(N);
    r.roots.reserve(N);
    // All labels are roots, including every old and new label. Every BFS uses
    // only adjacency reconstructed directly from this one candidate edge file.
    for (int root = 0; root < N; ++root) {
        std::fill(distance.begin(), distance.end(), -1);
        int head = 0, tail = 0;
        queue[tail++] = root;
        distance[root] = 0;
        while (head < tail) {
            const int v = queue[head++];
            for (const int u : adjacency[v]) {
                if (distance[u] == -1) {
                    distance[u] = distance[v] + 1;
                    queue[tail++] = u;
                }
            }
        }
        RootResult rr{root, tail, 0, 0, {0, 0, 0, 0}};
        int bad_target = -1;
        for (int v = 0; v < N; ++v) {
            if (distance[v] >= 0) rr.eccentricity = std::max(rr.eccentricity, distance[v]);
            if (distance[v] >= 0 && distance[v] <= 3) {
                ++rr.within_three;
                ++rr.first_four_distance_counts[distance[v]];
            } else if (bad_target < 0) bad_target = v;
        }
        r.roots.push_back(rr);
        ++r.eccentricities[rr.eccentricity];
        if (tail == N) r.connected = true;
        if (bad_target >= 0) {
            r.bad_root = root;
            r.bad_target = bad_target;
            r.bad_distance = distance[bad_target];
            throw std::runtime_error("radius-3 failure: root=" + std::to_string(root) +
                ", target=" + std::to_string(bad_target) + ", exact BFS distance=" +
                std::to_string(distance[bad_target]) + " (-1 means unreachable); reached within 3=" +
                std::to_string(rr.within_three));
        }
    }
    r.status = "PASS";
}

int main() {
    const auto start = std::chrono::steady_clock::now();
    struct rlimit budget {30, 30};
    if (setrlimit(RLIMIT_CPU, &budget) != 0) {
        std::cerr << "could not set the 30 CPU-second budget\n";
        return 2;
    }
    Report r;
    try { verify(r); }
    catch (const std::exception& e) { r.failure = e.what(); }
    std::ofstream all_roots(OUTDIR + "ALL_ROOTS.tsv");
    all_roots << "root\treached\treached_within_three\teccentricity\td0\td1\td2\td3\n";
    for (const auto& rr : r.roots) {
        all_roots << rr.root << '\t' << rr.reached << '\t' << rr.within_three
            << '\t' << rr.eccentricity;
        for (int count : rr.first_four_distance_counts) all_roots << '\t' << count;
        all_roots << '\n';
    }
    all_roots.close();
    struct rusage usage {};
    getrusage(RUSAGE_SELF, &usage);
    const double user_cpu = usage.ru_utime.tv_sec + usage.ru_utime.tv_usec / 1e6;
    const double system_cpu = usage.ru_stime.tv_sec + usage.ru_stime.tv_usec / 1e6;
    const double wall = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - start).count();
    int min_coverage = N;
    for (const auto& rr : r.roots) min_coverage = std::min(min_coverage, rr.within_three);
    if (r.roots.empty()) min_coverage = 0;

    std::ofstream json(OUTDIR + "INDEPENDENT_ACCEPTANCE.json");
    json << std::boolalpha << std::fixed << std::setprecision(6)
        << "{\n  \"status\": " << json_string(r.status)
        << ",\n  \"scope\": \"one literal candidate; all 6160 roots; no inherited source diameter bound\""
        << ",\n  \"graph_data_inputs\": [" << json_string(INPUT) << ']'
        << ",\n  \"order\": " << r.n
        << ",\n  \"declared_edge_count\": " << r.declared_m
        << ",\n  \"literal_edge_count\": " << r.literal_m
        << ",\n  \"header_pass\": " << r.header_pass
        << ",\n  \"literal_count_pass\": " << r.literal_count_pass
        << ",\n  \"simple\": " << r.simple
        << ",\n  \"undirected_reciprocal_adjacency\": " << r.undirected
        << ",\n  \"degree_histogram\": " << histogram_json(r.degrees)
        << ",\n  \"max_degree\": " << r.max_degree
        << ",\n  \"degree_bound_pass\": " << r.degree_pass
        << ",\n  \"connected\": " << r.connected
        << ",\n  \"roots_expected\": 6160"
        << ",\n  \"roots_actually_checked\": " << r.roots.size()
        << ",\n  \"root_labels\": \"all labels 0 through 6159\""
        << ",\n  \"minimum_radius_three_coverage\": " << min_coverage
        << ",\n  \"eccentricity_histogram\": " << histogram_json(r.eccentricities)
        << ",\n  \"all_root_results_file\": \"ALL_ROOTS.tsv\""
        << ",\n  \"diameter_upper_bound\": " << (r.status == "PASS" ? "3" : "null")
        << ",\n  \"degree_24_diameter_two_order_bound\": 577"
        << ",\n  \"exact_diameter\": " << (r.status == "PASS" ? "3" : "null")
        << ",\n  \"counterexample_root\": " << r.bad_root
        << ",\n  \"counterexample_target\": " << r.bad_target
        << ",\n  \"counterexample_exact_bfs_distance\": " << r.bad_distance
        << ",\n  \"failure\": " << (r.failure.empty() ? "null" : json_string(r.failure))
        << ",\n  \"worker_count\": 1,\n  \"cpu_budget_seconds\": 30"
        << ",\n  \"actual_cpu_seconds\": " << user_cpu + system_cpu
        << ",\n  \"actual_user_cpu_seconds\": " << user_cpu
        << ",\n  \"actual_system_cpu_seconds\": " << system_cpu
        << ",\n  \"actual_wall_seconds\": " << wall
        << ",\n  \"producer_inputs_not_read\": [\"PARAMETERS\",\"SOURCE_CHECK\",\"EXTENSION_STEPS\",\"RESULT\",\"generator/code\",\"proof\",\"coverage cache\",\"old source 6144 materials\"]"
        << ",\n  \"old_source_6144_run\": false,\n  \"graph_4336_rerun\": false"
        << ",\n  \"solver_used\": false,\n  \"lean_run\": false,\n  \"public_record_claim\": false\n}\n";
    std::ofstream summary(OUTDIR + "SUMMARY.md");
    summary << std::fixed << std::setprecision(6)
        << "# Independent literal acceptance: " << r.status << "\n\n"
        << "Order " << r.n << ", literal edges " << r.literal_m << ", maximum degree "
        << r.max_degree << "; degree histogram `" << histogram_json(r.degrees) << "`.\n\n"
        << "Checked " << r.roots.size() << " roots by ordinary queue BFS in this candidate's complete literal adjacency. "
        << "Minimum radius-three coverage: " << min_coverage << ". Eccentricity histogram: `"
        << histogram_json(r.eccentricities) << "`. Per-root counts are saved in ALL_ROOTS.tsv.\n\n";
    if (r.status == "PASS") {
        summary << "The header, edge count, endpoint ranges, simplicity, reciprocal undirected adjacency, "
            << "and degree bound all passed. Every one of the 6160 roots reached every one of the 6160 vertices "
            << "within three steps, proving connectedness and diameter at most 3. "
            << "Since 6160 > 24^2+1 = 577, the degree-24 diameter-two counting bound excludes diameter at most 2. "
            << "The graph therefore has exact diameter 3. No source diameter was inherited.\n\n";
    } else summary << "Concrete failure: " << r.failure << "\n\n";
    summary << "One worker; acceptance CPU " << user_cpu + system_cpu << " seconds (user "
        << user_cpu << ", system " << system_cpu << "); wall " << wall
        << " seconds; CPU budget 30 seconds.\n\n"
        << "Graph data read: only graph_d24_D3_n6160.edges. No producer PARAMETERS, SOURCE_CHECK, "
        << "EXTENSION_STEPS, RESULT, generator/code, proof, coverage cache, or old-source-6144 materials "
        << "were read. The 6144 source and 4336 graph were not rerun. No solver, Lean, install, hashes, "
        << "checksums, manifests, or public record claim.\n";
    if (!all_roots || !json || !summary) {
        std::cerr << "independent report output failed\n";
        return 2;
    }
    std::cout << r.status << " n=" << r.n << " m=" << r.literal_m << " maxdeg="
        << r.max_degree << " roots=" << r.roots.size() << " minR3=" << min_coverage
        << " cpu=" << std::fixed << std::setprecision(6) << user_cpu + system_cpu << '\n';
    if (!r.failure.empty()) std::cout << r.failure << '\n';
    return r.status == "PASS" ? 0 : 1;
}
