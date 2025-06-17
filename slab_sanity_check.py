import os
from ase.io import read

path = "D:/ACADEMIC DOCUMENTS/IISc/CO2_act/DOPED_RELAXED/"
files = os.listdir(path)

# Things to check: Only one dopant per slab, number of fixed atoms must be as precedented
fix_count_map = {"111": [], "211": [], "100": [], "110": []}
dopant_count_map = {}
for file in files:
    slab = read(f"{path}/{file}")
    fix_count_map[file[3:6]].append(slab.constraints[0].index.shape[0])
    dopant = set(list(slab.numbers)) - {29}
    dopant_count_map[file] = list(slab.numbers).count(list(dopant)[0])

for mi in fix_count_map:
    fix_count_map[mi] = set(fix_count_map[mi])

print("fix_count_map:")
print(fix_count_map)

dopant_count_set = set(list(dopant_count_map.values()))
print("Set of dopant counts per slab:")
print(dopant_count_set)