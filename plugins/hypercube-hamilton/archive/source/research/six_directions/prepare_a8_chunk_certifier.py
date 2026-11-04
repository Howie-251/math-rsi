"""Separate bounded chunk producer; does not modify the running executable."""
from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'a8_full_cycle_certifier.cpp').read_text()
needle=' unsigned char record[24];uint64_t total=0,positive=0,unknown=0,exhausted=0;'
assert needle in s
s=s.replace(needle,' uint64_t offset=argc>7?stoull(argv[7]):0;in.seekg(streamoff(offset*24));assert(in);\n'+needle)
(R/'a8_full_cycle_certifier_chunk.cpp').write_text(s)
