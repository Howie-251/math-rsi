// Bounded construction search. A nonzero score is NOT a diameter-two graph.
// Input: Brown57 (hub added at degree-7 points), or an explicit regular58 seed.
// Moves preserve simplicity and degree 8. Objective: uncovered unordered pairs.
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <string>

using Graph = std::array<uint64_t, 58>;
constexpr uint64_t all_vertices = (uint64_t(1) << 58) - 1;

int score(const Graph& g, Graph& missing) {
    int count = 0;
    for (int u = 0; u < 58; ++u) {
        uint64_t cover = g[u] | (uint64_t(1) << u), neighbors = g[u];
        while (neighbors) {
            int v = __builtin_ctzll(neighbors);
            neighbors &= neighbors - 1;
            cover |= g[v];
        }
        missing[u] = all_vertices & ~cover;
        count += __builtin_popcountll(missing[u]);
    }
    return count / 2;
}

int sample_bit(uint64_t bits, std::mt19937_64& rng) {
    unsigned index = rng() % __builtin_popcountll(bits);
    while (index--) bits &= bits - 1;
    return __builtin_ctzll(bits);
}

void toggle(Graph& g, int u, int v) {
    g[u] ^= uint64_t(1) << v;
    g[v] ^= uint64_t(1) << u;
}

void write_graph(const Graph& g, const std::string& path) {
    std::ofstream out(path);
    out << "58 232\n";
    for (int u = 0; u < 58; ++u)
        for (int v = u + 1; v < 58; ++v)
            if ((g[u] >> v) & 1) out << u << ' ' << v << '\n';
}

int main(int argc, char** argv) {
    if (argc != 5) {
        std::cerr << "usage: search58_switches input.edges seconds seed output_prefix\n";
        return 2;
    }
    double seconds = std::stod(argv[2]);
    uint64_t seed = std::stoull(argv[3]);
    std::string prefix = argv[4];
    std::ifstream in(argv[1]);
    int n, m;
    if (!(in >> n >> m) || !((n == 57 && m == 224) || (n == 58 && m == 232))) return 3;
    Graph start{};
    for (int e = 0, u, v; e < m; ++e) {
        if (!(in >> u >> v) || u < 0 || u >= n || v < 0 || v >= n || u == v
            || ((start[u] >> v) & 1)) return 4;
        toggle(start, u, v);
    }
    if (n == 57)
        for (int v = 0; v < 57; ++v)
            if (__builtin_popcountll(start[v]) == 7) toggle(start, v, 57);
    for (int v = 0; v < 58; ++v)
        if (__builtin_popcountll(start[v]) != 8) return 5;
    Graph g = start, missing{}, next_missing{}, best_graph = start;
    int current = score(g, missing), best = current, initial = current;
    std::mt19937_64 rng(seed);
    auto begin = std::chrono::steady_clock::now();
    double elapsed = 0;
    uint64_t proposals = 0, legal = 0, accepted = 0, resets = 0;
    // A cycle reheats then cools; each restart uses the best actual full graph.
    constexpr uint64_t cycle = 2000000;
    write_graph(best_graph, prefix + ".best.edges");
    while (best > 0) {
        if ((proposals & 1023) == 0) {
            elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now() - begin).count();
            if (elapsed >= seconds) break;
        }
        if (proposals && proposals % cycle == 0) {
            g = best_graph;
            current = score(g, missing);
            ++resets;
        }
        double phase = double(proposals % cycle) / cycle;
        double temperature = 1.3 * std::pow(0.06 / 1.3, phase);
        ++proposals;
        int x, a, v, b;
        if ((rng() & 3) != 0) {
            int u = rng() % 58;
            for (int i = 0; i < 58 && !missing[u]; ++i) u = (u + 1) % 58;
            if (!missing[u]) break;
            v = sample_bit(missing[u], rng);
            x = sample_bit(g[u], rng);
            a = sample_bit(g[x] & ~(uint64_t(1) << u), rng);
            b = sample_bit(g[v], rng);
        } else {
            x = rng() % 58;
            v = rng() % 58;
            a = sample_bit(g[x], rng);
            b = sample_bit(g[v], rng);
        }
        if (x == v || x == b || a == v || a == b || ((g[x] >> v) & 1)
            || ((g[a] >> b) & 1)) continue;
        ++legal;
        toggle(g, x, a); toggle(g, v, b); toggle(g, x, v); toggle(g, a, b);
        int candidate = score(g, next_missing), delta = candidate - current;
        bool take = delta <= 0 || std::generate_canonical<double, 53>(rng) < std::exp(-delta / temperature);
        if (take) {
            ++accepted;
            current = candidate;
            missing = next_missing;
            if (current < best) {
                best = current; best_graph = g;
                write_graph(best_graph, prefix + ".best.edges");
                std::cout << "improvement " << best << " proposal " << proposals << '\n' << std::flush;
            }
        } else {
            toggle(g, x, a); toggle(g, v, b); toggle(g, x, v); toggle(g, a, b);
        }
    }
    elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now() - begin).count();
    std::ofstream summary(prefix + ".json");
    summary << "{\"n\":58,\"degree\":8,\"seed\":" << seed
            << ",\"wall_limit_seconds\":" << seconds << ",\"elapsed_seconds\":" << elapsed
            << ",\"proposals\":" << proposals << ",\"legal_moves\":" << legal
            << ",\"accepted\":" << accepted << ",\"restarts\":" << resets
            << ",\"initial_uncovered_pairs\":" << initial << ",\"best_uncovered_pairs\":" << best
            << ",\"status\":\"" << (best == 0 ? "candidate_requires_independent_verification" : "diagnostic_not_a_target_graph")
            << "\"}\n";
    std::cout << "finished best=" << best << " legal_moves=" << legal << " elapsed=" << elapsed << '\n';
    return 0;
}
