"""Recipe arithmetic only: no source graph, candidate graph, or BFS."""
from math import gcd
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
N, M, r = 6941, 90, 316
gens = [(35, 35), (509, 5), (4285, 37), (6911, 49), (3639, 34)]

def factor(n):
    out, d = [], 2
    while d*d <= n:
        if n % d == 0:
            k = 0
            while n % d == 0:
                n //= d
                k += 1
            out.append([d, k])
        d += 1
    if n > 1:
        out.append([n, 1])
    return out

def order(a, n):
    x = 1
    for k in range(1, M + 1):
        x = x*a % n
        if x == 1:
            return k
    raise ValueError((a, n))

z = gens[2][0] * pow((pow(r, 37, N)-1) % N, -1, N) % N
conjugated = [((b+(1-pow(r,j,N))*z) % N, 73*j % M) for b,j in gens]
scale_base = conjugated[1][0]
normalized = sorted([(b*pow(scale_base,-1,N) % N,j) for b,j in conjugated], key=lambda x:x[1])
prime_checks = []
for p in range(1 + 90*((N-1)//90+1), 10000, 90):
    f = factor(p)
    prime_checks.append({"p":p,"factorization":f})
    if f == [[p,1]]:
        next_prime = p
        break
crt_checks = []
for p in range(1 + 45*((631-1)//45+1), 2000, 45):
    f = factor(p)
    crt_checks.append({"p":p,"factorization":f})
    if f == [[p,1]]:
        next_crt_prime = p
        break
result = {
    "source_N":N,"source_M":M,"source_r":r,
    "N_factorization":factor(N),
    "action_orders":{"mod11":order(r%11,11),"mod631":order(r%631,631),"mod6941":order(r,N)},
    "global_action_kernel_order":M//order(r,N),
    "CRT_action_kernel_orders":{"on_mod11":9,"on_mod631":2},
    "r45_modN":pow(r,45,N),
    "source_involution_count":gcd(1+pow(r,45,N),N),
    "positive_generators_normal_phase":[list(x) for x in gens],
    "inverse_generators_normal_phase":[[-pow(r,-j,N)*b%N,-j%M] for b,j in gens],
    "phase_relabel_old37_to_new1":{"phase_multiplier":73,"new_r":pow(r,37,N)},
    "translation_conjugation_z":z,
    "scaling_base":scale_base,"scaling_base_gcd_N":gcd(scale_base,N),
    "normalized_positive_generators_normal_phase":[list(x) for x in normalized],
    "normalized_phase52_offset_is_inverse2":normalized[3][0] == pow(2,-1,N),
    "next_faithful90_prime_checks":prime_checks,
    "next_faithful90_prime":next_prime,
    "hypothetical_faithful_field_group_order":90*next_prime,
    "order_jump":90*next_prime-90*N,
    "relative_jump":next_prime/N-1,
    "prioritized_degree8_relative_jump":6211/6073-1,
    "next_CRT_preserving_order45_prime_checks":crt_checks,
    "next_CRT_preserving_order45_prime":next_crt_prime,
    "CRT_preserving_order":90*11*next_crt_prime,
    "candidate_embedding_tests":0,"new_graphs":0,"BFS":0
}
(OUT/"ARITHMETIC.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
