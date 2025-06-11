import os
import re
from ase.io import read
from ase.build import add_adsorbate

# Define paths
slab_dir = "/kaggle/input/discovery-slabs/SLABS"
output_dir = "SLABS_WITH_ADSORBATE"
os.makedirs(output_dir, exist_ok=True)

# Load adsorbates
is_adsorbate = read('/kaggle/input/discovery-slabs/CO2_IS_POSCAR')
fs_adsorbate = read('/kaggle/input/discovery-slabs/CO2_FS_POSCAR')
fs_adsorbate.rotate(90, 'z', rotate_cell=False)

# Offsets only for Cu211 dopant sites
cu211_offsets = {
    2: (-0.2, 0.1),
    10: (-0.3, 0),
    22: (0, 0.1)
}

def process_slab(slab_path):
    """Process slab file, apply central position with dopant-dependent offset for Cu211."""
    try:
        slab = read(slab_path)
        filename = os.path.basename(slab_path)
        base_name = os.path.splitext(filename)[0]

        # Extract surface type and dopant site number
        match = re.match(r'(Cu\d{3})_\d+_(\d+)', base_name)
        if not match:
            print(f"Skipping unrecognized filename format: {filename}")
            return None

        surface_type = match.group(1)
        dopant_site = int(match.group(2))

        # Calculate center of surface cell
        a, b = slab.cell.cellpar()[:2]
        center_position = (a / 2, b / 2)

        # Use default offset (0, 0), override if Cu211 and known dopant
        offset = (0, 0)
        if surface_type == "Cu211":
            offset = cu211_offsets.get(dopant_site, (0, 0))

        def create_slab(adsorbate):
            new_slab = slab.copy()
            add_adsorbate(new_slab, adsorbate, height=2.0,
                          position=center_position, offset=offset)
            return new_slab

        return {
            'initial': create_slab(is_adsorbate),
            'final': create_slab(fs_adsorbate),
            'base_name': base_name
        }

    except Exception as e:
        print(f"Error processing {slab_path}: {str(e)}")
        return None

# Process all slabs
for filename in sorted(os.listdir(slab_dir)):
    if filename.endswith(".POSCAR"):
        result = process_slab(os.path.join(slab_dir, filename))
        if result:
            result['initial'].write(f"{output_dir}/initial_{result['base_name']}.traj")
            result['final'].write(f"{output_dir}/final_{result['base_name']}.traj")
            print(f"Generated: {result['base_name']}")

print(f"\nSuccessfully processed {len(os.listdir(output_dir)) // 2} slabs in {output_dir}/")