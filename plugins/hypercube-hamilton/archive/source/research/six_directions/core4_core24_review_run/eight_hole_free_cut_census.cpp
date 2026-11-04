#include <array>
#include <iostream>
#include <vector>
using namespace std;
int pc(int x) { return __builtin_popcount((unsigned)x); }
bool good(int a, int b) {
    return (a == 0 && (b == 1 || b == 2)) ||
           (a == 1 && b >= 1 && b <= 3) ||
           (a == 2 && b >= 2 && b <= 4) || (a == 3 && b == 3);
}
int main() {
    bool success = true;
    // Root is 0. Free target distance 1 was settled before this census.
    // Coordinate permutations normalize distances 3 and 5 to 7 and 31.
    for (int v : {7, 31}) {
        long long total = 0, bad = 0;
        vector<int> even;
        for (int z = 1; z < 64; ++z)
            if (pc(z) % 2 == 0 && pc(z ^ v) != 1) even.push_back(z);
        for (int p = 0; p < (int)even.size(); ++p)
        for (int q = p + 1; q < (int)even.size(); ++q)
        for (int r = q + 1; r < (int)even.size(); ++r) {
            array<int, 3> z = {even[p], even[q], even[r]};
            vector<int> odd;
            for (int w = 0; w < 64; ++w) if (pc(w) % 2 && w != v) {
                bool admissible = true;
                for (int x : z) if (pc(x ^ w) == 1) admissible = false;
                if (admissible) odd.push_back(w);
            }
            for (int j = 0; j < (int)odd.size(); ++j)
            for (int k = j + 1; k < (int)odd.size(); ++k)
            for (int l = k + 1; l < (int)odd.size(); ++l) {
                array<int, 4> w = {v, odd[j], odd[k], odd[l]};
                bool found = false;
                for (int i = 0; i < 6; ++i) {
                    int a = 0, b = 0;
                    for (int x : z) a += ((x >> i & 1) == (v >> i & 1));
                    for (int x : w) b += ((x >> i & 1) == (v >> i & 1));
                    found |= good(a, b);
                }
                ++total;
                if (!found) ++bad;
            }
        }
        cout << "v=" << v << " total=" << total << " bad=" << bad << "\n";
        success &= (bad == 0);
    }
    return success ? 0 : 1;
}
