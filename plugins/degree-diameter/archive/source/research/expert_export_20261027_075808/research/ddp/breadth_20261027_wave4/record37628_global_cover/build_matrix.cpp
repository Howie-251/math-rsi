#include <bits/stdc++.h>
using namespace std;
constexpr int N = 37628;

int main(int argc, char** argv) {
    clock_t began = clock();
    assert(argc == 3);
    string output = argv[2];
    ifstream input(argv[1]);
    vector<vector<int>> adjacency(N);
    vector<bool> present(N, false);
    string line;
    long long twice_edges = 0;
    while (getline(input, line)) {
        if (line.empty() || line[0] == '#') continue;
        stringstream row(line);
        int u, v; row >> u;
        assert(0 <= u && u < N && !present[u]);
        present[u] = true;
        while (row >> v) {
            assert(0 <= v && v < N && u != v);
            adjacency[u].push_back(v);
        }
        sort(adjacency[u].begin(), adjacency[u].end());
        assert(adjacent_find(adjacency[u].begin(), adjacency[u].end()) == adjacency[u].end());
        assert(adjacency[u].size() <= 11);
        twice_edges += adjacency[u].size();
    }
    assert(all_of(present.begin(), present.end(), [](bool x){ return x; }));
    assert(twice_edges == 410592);
    vector<int> eligible;
    for (int u = 0; u < N; ++u) {
        if (adjacency[u].size() < 11) eligible.push_back(u);
        for (int v : adjacency[u]) assert(binary_search(adjacency[v].begin(), adjacency[v].end(), u));
    }
    assert(eligible.size() == 2504);
    ofstream indices(output + "/indices.i32.bin", ios::binary);
    vector<int32_t> pointers(1, 0);
    vector<int> seen(N, 0), queue(N), sizes;
    long long coverage_nnz = 0;
    for (int k = 0; k < (int)eligible.size(); ++k) {
        int head = 0, tail = 1;
        queue[0] = eligible[k]; seen[queue[0]] = k + 1;
        for (int depth = 0; depth < 4; ++depth) {
            int stop = tail;
            while (head < stop) {
                int u = queue[head++];
                for (int v : adjacency[u]) if (seen[v] != k + 1) {
                    seen[v] = k + 1; queue[tail++] = v;
                }
            }
        }
        sort(queue.begin(), queue.begin() + tail);
        for (int t = 0; t < tail; ++t) {
            int32_t value = queue[t];
            indices.write(reinterpret_cast<char*>(&value), sizeof(value));
        }
        int32_t cardinality_row = N;
        indices.write(reinterpret_cast<char*>(&cardinality_row), sizeof(cardinality_row));
        coverage_nnz += tail;
        assert(coverage_nnz + k + 1 < numeric_limits<int32_t>::max());
        pointers.push_back(static_cast<int32_t>(coverage_nnz + k + 1));
        sizes.push_back(tail);
    }
    indices.close();
    ofstream pointer_file(output + "/indptr.i32.bin", ios::binary);
    pointer_file.write(reinterpret_cast<char*>(pointers.data()), sizeof(int32_t) * pointers.size());
    pointer_file.close();
    ofstream metadata(output + "/matrix_metadata.json");
    metadata << "{\"base_vertices\":" << N << ",\"base_edges\":" << twice_edges / 2
             << ",\"eligible_variables\":" << eligible.size()
             << ",\"coverage_rows\":" << N << ",\"cardinality_rows\":1,\"rows\":" << N + 1
             << ",\"radius\":4,\"neighbor_cap\":11,\"coverage_nonzeros\":" << coverage_nnz
             << ",\"total_nonzeros\":" << pointers.back()
             << ",\"CSC_storage_bytes_float64_int32\":" << 12LL * pointers.back() + 4LL * pointers.size()
             << ",\"minimum_R4_ball\":" << *min_element(sizes.begin(), sizes.end())
             << ",\"maximum_R4_ball\":" << *max_element(sizes.begin(), sizes.end())
             << ",\"build_CPU_seconds\":" << double(clock() - began) / CLOCKS_PER_SEC
             << ",\"eligible_vertices\":[";
    for (int i = 0; i < (int)eligible.size(); ++i) { if (i) metadata << ','; metadata << eligible[i]; }
    metadata << "],\"R4_ball_sizes\":[";
    for (int i = 0; i < (int)sizes.size(); ++i) { if (i) metadata << ','; metadata << sizes[i]; }
    metadata << "]}\n";
}
