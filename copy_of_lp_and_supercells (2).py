# -*- coding: utf-8 -*-
"""Copy of LP_and_supercells.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lUVh0D9C_8lGk3vcbXBHd1WF4XToHHYL
"""

!pip install ase
!pip install fairchem-core
!pip install huggingface_hub

from ase import Atoms
from ase.build import bulk
from ase.constraints import ExpCellFilter
from ase.optimize import BFGS
from huggingface_hub import login

from fairchem.core import pretrained_mlip, FAIRChemCalculator

# Logging into the UMA repository
hf_token = "<TOKEN>"
login(token = hf_token)

device = "cpu"
predictor = pretrained_mlip.get_predict_unit("uma-s-1", device=device)
calc = FAIRChemCalculator(predictor, task_name="omat")

atoms = bulk("Cu", "fcc", a = 3.56, cubic = True)
atoms.calc = calc

opt_geo = BFGS(atoms)
opt_geo.run(fmax = 0.01)

cell_filter = ExpCellFilter(atoms, mask=[1, 1, 1, 0, 0, 0])
opt = BFGS(cell_filter)
opt.run(fmax=0.01)

print("Final lattice:\n", atoms.get_cell())
print("Final positions:\n", atoms.get_positions())

from ase.build import bulk
atoms = bulk("Cu", "fcc", a = 3.6, cubic = True)
from ase.visualize import view
view(atoms, viewer = "x3d")

predictor1 = pretrained_mlip.get_predict_unit("uma-s-1", device="cpu")
calc1 = FAIRChemCalculator(predictor1, task_name="oc20")

def relax_system(filename):
  atoms = read(f"{filename}.POSCAR")
  atoms.calc = calc1
  opt1 = BFGS(atoms)
  opt1.run(fmax = 0.01)
  cell_filter = ExpCellFilter(atoms, mask=[1, 1, 1, 0, 0, 0])
  optimizer = BFGS(cell_filter)
  optimizer.run(fmax = 0.01)
  write(f"{filename}_opt.POSCAR", atoms)

filenames = ["Cu110", "Cu100", "Cu211", "Cu111"]
for filename in filenames:
  print(f"Started {filename} relaxation")
  relax_system(filename)
  print(f"Completed {filename} relaxation")