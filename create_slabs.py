from ase.build import fcc211, fcc111, fcc110, fcc100
from ase.io import write

slab_func_map = {"211": fcc211, "111": fcc111, "110": fcc110, "100": fcc100}
size_map = {"211": (6, 4, 4), "111": (4, 4, 4), "110": (4, 4, 4), "100": (4, 4, 4)}
doping_sites = {"211": [10, 2, 22], "111": [58], "110": [58], "100": [58]}
dopants = [13, 31, 32, 49, 50, 51, 81, 82, 83] + list(set(range(21, 31)) - {29}) + list(set(range(39, 49)) - {43}) + list(range(71, 80))

for mi in slab_func_map:
    for site in doping_sites[mi]:
        for dopant in dopants:
            slab = slab_func_map[mi]("Cu", size = size_map[mi], orthogonal = True, vacuum = 10)
            slab.numbers[site] = dopant
            filename = f"Cu{mi}_{dopant}_{site}.POSCAR"
            write(filename, slab)
            