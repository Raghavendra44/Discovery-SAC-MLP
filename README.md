-create_slabs.py creates Cu supercells with dopants at sites as discussed. All slabs are created with a vacuum of 10 A.
Facets: 100, 110, 111, 211. Surfaces of all miller indices other than 211 are 4 X 4 X 4 supercells. For 211, a 6 X 4 X 4 supercell is created.
-slabs_sanity_check.py allows one to check if slabs in a folder have exactly one dopant each, and if the number of fixed atoms in slabs of a given Miller index
are consistent.
-copy_of_lp_and_supercells(2).py is a .py version of the colab notebook used to compute teh lattice parameters and get relaxed supercells using UMA models.
-UMA_SLABS contains slab POSCARS ready-to-use for NEB calcs, with names in the format Cu_{miller index}_ {dopant atomic number} _{site number}.POSCAR (no spaces)

-create_surface_with_adsorbate.py

This script places CO₂ adsorbates on Cu slab structures and outputs `.extxyz` files for simulation.

Features:
- Loads initial and final CO₂ configurations from CO2_IS_POSCAR and CO2_IS_POSCAR
- Applies custom XY offsets for specific facets and dopant sites to make it atop configuration
- Outputs structured files: initial_<name>.extxyz, final_<name>.extxyz

Requirements:
- Python 3
- ASE library (install via: pip install ase)

Input Files:
- Slabs: SLABS/*.POSCAR
- Adsorbates: CO2_IS_POSCAR, CO2_FS_POSCAR

Usage:
Run the script in a Python environment:

    python generate_slab_with_adsorbates.py

Output:
- Directory: SLAB_WITH_ADSORbATES_XYZ/
- Files: Adsorbate-added slabs in .extxyz format

