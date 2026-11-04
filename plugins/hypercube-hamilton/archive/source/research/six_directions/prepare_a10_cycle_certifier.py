"""Create an 11-edge positive-certificate worker without editing A8 sources."""
from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'a8_full_cycle_certifier.cpp').read_text()
s=s.replace('12-edge','11-edge').replace('Input24','Input22').replace('output55','output53')
s=s.replace('1<<24','1<<25').replace('1u<<24','1u<<25')
s=s.replace('record[24]','record[22]').replace('record),24','record),22').replace('j<24','j<22')
s=s.replace('blocks.size()==7','blocks.size()==9').replace('blocks.size()==19','blocks.size()==20')
s=s.replace('record_bytes\\\":55','record_bytes\\\":53').replace('full_a8_proved','full_a10_proved')
needle='unsigned char record[22];'
s=s.replace(needle,'uint64_t offset=argc>7?stoull(argv[7]):0;in.seekg(streamoff(offset*22));assert(in);\n '+needle)
(R/'a10_cycle_certifier_chunk.cpp').write_text(s)
print('Created a10_cycle_certifier_chunk.cpp: 22-byte input, 53-byte positive record, optional input offset.')
