''' Program to dope specific sites on supercells'''
from ase.io import read, write
from ase.build import fcc111, fcc110, fcc211, fcc100

slab_func_map = {"211": fcc211, "111": fcc111, "110": fcc110, "100": fcc100}
size_map = {"211": (6, 4, 4), "111": (4, 4, 4), "110": (4, 4, 4), "100": (4, 4, 4)}
doping_sites = {"211": [10, 2, 22], "111": [58], "110": [58], "100": [58]}
dopants = [13, 31, 32, 49, 50, 51, 81, 82, 83] + list(set(range(21, 31)) - {29}) + list(set(range(39, 49)) - {43}) + list(range(72, 80))
print(f"Number of dopants = {len(dopants)}")
print(f"Total number of surfaces = {6*len(dopants)}")
path = "D:/ACADEMIC DOCUMENTS/IISc/CO2_act/RELAXED SUPERCELLS - OC20/"
save_path = "D:/ACADEMIC DOCUMENTS/IISc/CO2_act/DOPED_RELAXED/"
for mi in slab_func_map:
    for site in doping_sites[mi]:
        for dopant in dopants:
            cu_slab = read(f"{path}Cu{mi}_opt_fixed.POSCAR")
            cu_slab.numbers[site] = dopant
            filename = f"Cu_{mi}_{dopant}_{site}.POSCAR"
            write(f"{save_path}/{filename}", cu_slab)
            