"""Prepare the independently verified core4 proof, preserving core1 sources."""
from pathlib import Path
R=Path(__file__).resolve().parent
text=(R/'T15_CORE1_FULL_CLOSURE.md').read_text()
text=text.replace('core1','core4').replace('3,5,9','3,5,15').replace('0,1,2,7,11,19','0,1,2,7,11,31')
replacements={
 'the three core4 pair geometries are coordinate images of $(3,5,1)$, with33 negatives each.':'the bridge pair3,5 uses33 negatives, while pairs3,15 and5,15 each use128 negatives (the last pair is a coordinate image of3,15).',
 '`r4_inverse_blockers_3_5_1_verification.json`':'the independently checked canonical inverse files for3,5,1 and3,15,1',
 '`q4_five_avoided_jpair_verification.json`':'`t15_core4_five_avoided_inputs.json`',
 'verify_t15_core4_c0_B.py':'verify_t15_core4_r4_c0_B.py',
 'Precisely105 B':'Precisely175 B',
 'All1091475':'All1819125',
 'verify_t15_core4_route_c0_residual.cpp':'verify_q5_full_input_certificates.cpp',
 'There are116 patterns per $u$.':'There are116 patterns when u=3 or5 and96 when u=15.',
 't15_core4_c2_types.cpp':'t15_core4_r4_c2_types.cpp',
 'Exactly420 unordered':'Exactly616 unordered',
 'leaving52390800':'leaving76839840',
 '`verify_t15_core4_joint_B.py` transports the completely checked canonical inverse families by coordinate permutations fixing1, intersects their three unresolved B sets, and compares the resulting exact sets with every supplied B input file.':'The independently audited R4 joint calculation transports the checked canonical inverse families by coordinate permutations fixing1 and intersects their three unresolved B sets. `verify_t15_core4_full_closure.py` compares these exact sets with every supplied B input file.',
 '|4|210|':'|4|272|','|6|28|':'|6|32|',
 't15_core4_joint_fourbridge_spectra.cpp':'r4_joint_fourbridge_parent.cpp',
 'verify_t15_core4_joint_fourbridge.cpp':'verify_r4_joint_fourbridge_generic.cpp',
 '|2|62370|420|52390800|0|':'|2|62370|616|76839840|0|',
 '|4|51975|210|261954000|1575|':'|4|51975|272|339292800|3045|',
 '|6|13860|28|279417600|6300|':'|6|13860|32|319334400|8820|',
 't15_core4_joint_fourbridge_c*_verification.json':'r4_joint_fourbridge_core4_c*_coverage_verification.json',
 'verify_t15_core4_joint_residual.cpp':'verify_q5_full_input_certificates.cpp',
 'All10395 positive residual':'All14385 positive residual',
 'there are1101870':'there are1833510',
}
for a,b in replacements.items():
    assert a in text,a
    text=text.replace(a,b)
text=text.replace('Step4 closes every one of these.','Step4 closes every one of these. The core4 B2 list is independently compared with precisely the zero-signature rows of the complete B input file; the producer also records every B input incompatible with any A spectrum and the two lists agree.')
text=text.replace('## Open risks and reproducibility','The full finite accounting is `T15_CORE4_FULL_CLOSURE_VERIFICATION.json`, produced by `verify_t15_core4_full_closure.py`. It checks all input lists, counts and immutable SHA-256 dependencies. The independently repeated four-bridge domain contains795342240 inputs, separate from the1833510 direct certificates.\n\n## Open risks and reproducibility')
(R/'T15_CORE4_FULL_CLOSURE.md').write_text(text)
