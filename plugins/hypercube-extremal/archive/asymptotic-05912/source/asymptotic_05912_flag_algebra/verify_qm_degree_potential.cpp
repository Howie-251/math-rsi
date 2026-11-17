// Standalone exact 128-bit integer verifier for the general-m Q_m Vertex-Degree Incidence Potential
// on any fixed 62-bit Q4 certificate (e.g. edge_cubic_v2 or certificate_track1_v1).
#include <algorithm>
#include <array>
#include <bit>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
using I128 = __int128_t;

inline int popcount(uint32_t x) { return __builtin_popcount(x); }

template<class T> vector<T> load(const string& p) {
    ifstream f(p, ios::binary | ios::ate);
    if (!f) throw runtime_error("Cannot read " + p);
    auto n = f.tellg();
    assert(n % sizeof(T) == 0);
    vector<T> a(n / sizeof(T));
    f.seekg(0);
    f.read(reinterpret_cast<char*>(a.data()), n);
    assert(f.good());
    return a;
}

string decimal(I128 n) {
    if (n == 0) return "0";
    bool neg = n < 0;
    if (neg) n = -n;
    string s;
    while (n) { s.push_back(char('0' + n % 10)); n /= 10; }
    if (neg) s.push_back('-');
    reverse(s.begin(), s.end());
    return s;
}

I128 parse_i128(const string& s) {
    I128 res = 0;
    bool neg = false;
    size_t i = 0;
    if (!s.empty() && s[0] == '-') { neg = true; i = 1; }
    for (; i < s.size(); i++) {
        assert(s[i] >= '0' && s[i] <= '9');
        res = res * 10 + (s[i] - '0');
    }
    return neg ? -res : res;
}

I128 choose_i128(int n, int k) {
    if (k < 0 || k > n) return 0;
    I128 res = 1;
    for (int i = 1; i <= k; i++) {
        res = res * (n - i + 1) / i;
    }
    return res;
}

int main(int argc, char** argv) {
    if (argc < 11) {
        cerr << "Usage: data_dir q_int64.bin exp U_str m S_str a_str b0 b1 b2 b3 b4\n";
        return 2;
    }
    string dir = argv[1];
    int exponent = stoi(argv[3]);
    assert(exponent >= 0 && exponent <= 90);
    I128 den = I128(1) << exponent, total_den = 192 * den;
    I128 reference = parse_i128(argv[4]);
    int m = stoi(argv[5]);
    assert(m >= 5 && m <= 4096);
    I128 S = parse_i128(argv[6]);
    I128 potential_a = parse_i128(argv[7]);
    array<I128, 5> b_coeff{};
    for (int k = 0; k < 5; k++) b_coeff[k] = parse_i128(argv[8 + k]);

    auto masks = load<uint32_t>(dir + "/full_masks.bin");
    assert(masks.size() == 3212821);
    auto q = load<int64_t>(argv[2]);
    auto dims = load<uint32_t>(dir + "/flag_dims.bin");
    auto sub = load<uint16_t>(dir + "/sub_lookup.bin"), tr = load<uint16_t>(dir + "/layer_trans.bin");
    auto fs = load<uint8_t>(dir + "/face_samples.bin"), ft = load<uint8_t>(dir + "/flag_type.bin");
    auto fi = load<uint8_t>(dir + "/flag_id.bin"), w = load<uint8_t>(dir + "/face_weights.bin");
    auto vl = load<uint8_t>(dir + "/vertex_lookup.bin"), vf = load<uint8_t>(dir + "/vertex_flag.bin");
    auto vs = load<uint8_t>(dir + "/vertex_samples.bin");

    array<int, 7> off{};
    for (int t = 0; t < 6; t++) off[t + 1] = off[t] + dims[t] * dims[t];
    assert(q.size() == size_t(off[6]));

    vector<pair<int, int>> e3, e4;
    for (int axis = 0; axis < 3; axis++)
        for (int v = 0; v < 8; v++)
            if (!(v & (1 << axis))) e3.push_back({v, v ^ (1 << axis)});
    for (int v = 0; v < 8; v++) e4.push_back({2 * v, 2 * v + 1});
    for (auto [a, b] : e3) e4.push_back({2 * a + 1, 2 * b + 1});
    for (auto [a, b] : e3) e4.push_back({2 * a, 2 * b});
    assert(e4.size() == 32);
    array<uint32_t, 16> incident{};
    for (int j = 0; j < 32; j++) {
        auto [a, b] = e4[j];
        incident[a] |= uint32_t(1) << j;
        incident[b] |= uint32_t(1) << j;
    }

    I128 minimum_slack = I128(1) << 125;
    uint32_t slack_mask = 0;
    I128 maximum = -(I128(1) << 125);
    uint32_t argmax = 0;

    for (uint32_t mask : masks) {
        int bytes[4];
        for (int b = 0; b < 4; b++) bytes[b] = (mask >> (8 * b)) & 255;
        uint16_t f3[8];
        for (int s = 0; s < 8; s++) {
            f3[s] = 0;
            for (int b = 0; b < 4; b++) f3[s] |= sub[(s * 4 + b) * 256 + bytes[b]];
        }
        I128 numerator = I128(popcount(mask)) * 6 * den;
        for (int s = 0; s < 192; s++) {
            int a = tr[f3[fs[4 * s]] * 48 + fs[4 * s + 1]], t = ft[a];
            if (t == 255) continue;
            int b = tr[f3[fs[4 * s + 2]] * 48 + fs[4 * s + 3]];
            assert(ft[b] == t);
            numerator += I128(w[t]) * q[off[t] + fi[a] * dims[t] + fi[b]];
        }
        uint8_t f2[96];
        for (int s = 0; s < 96; s++) {
            uint8_t v = 0;
            for (int b = 0; b < 4; b++) v |= vl[(s * 4 + b) * 256 + bytes[b]];
            assert(v != 15);
            f2[s] = vf[v];
        }
        for (int s = 0; s < 48; s++)
            numerator += I128(4) * q[off[5] + f2[vs[2 * s]] * 9 + f2[vs[2 * s + 1]]];

        array<int, 5> hist{};
        for (uint32_t im : incident) hist[popcount(mask & im)]++;
        I128 slack = S * (reference - numerator) - potential_a;
        for (int k = 0; k < 5; k++) slack -= b_coeff[k] * hist[k];
        if (slack < minimum_slack) {
            minimum_slack = slack;
            slack_mask = mask;
        }
        assert(slack >= 0);
        if (numerator > maximum) {
            maximum = numerator;
            argmax = mask;
        }
    }
    assert(maximum == reference);
    assert(minimum_slack == 0);

    // Verify all m+1 vertex degrees d in {0..m} in Q_m
    I128 min_phi = I128(1) << 125;
    int min_phi_d = -1;
    for (int d = 0; d <= m; d++) {
        I128 phi_d = 0;
        for (int k = 0; k < 5; k++) {
            phi_d += choose_i128(d, k) * choose_i128(m - d, 4 - k) * b_coeff[k];
        }
        if (phi_d < min_phi) {
            min_phi = phi_d;
            min_phi_d = d;
        }
    }
    I128 cm4 = choose_i128(m, 4);
    I128 total_deficit_num = potential_a * cm4 + I128(16) * min_phi;
    I128 total_deficit_den = S * cm4;
    assert(total_deficit_num > 0);

    cout << "{\"status\":\"PASS_EXACT_128BIT_POTENTIAL\""
         << ",\"m\":" << m
         << ",\"Q4_orbits_checked\":" << masks.size()
         << ",\"maximum_numerator\":\"" << decimal(maximum) << "\""
         << ",\"common_denominator\":\"" << decimal(total_den) << "\""
         << ",\"minimum_Q4_slack\":\"" << decimal(minimum_slack) << "\""
         << ",\"minimizing_Q4_mask\":" << slack_mask
         << ",\"min_phi_m\":\"" << decimal(min_phi) << "\""
         << ",\"minimizing_degree_d\":" << min_phi_d
         << ",\"deficit_numerator\":\"" << decimal(total_deficit_num) << "\""
         << ",\"deficit_denominator\":\"" << decimal(total_deficit_den) << "\"}\n";
    return 0;
}
