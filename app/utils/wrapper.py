import ctypes
import os

# Load the compiled Cubiomes shared library
cubiomes_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "cubiomes.so"))
cubiomes = ctypes.CDLL(cubiomes_path)
D
# Define constants
DIM_OVERWORLD = 0
DIM_NETHER = -1
DIM_END = 1

# Define the function signatures based on Cubiomes' header file
# Setup the generator
cubiomes.setupGenerator.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
cubiomes.setupGenerator.restype = None

# Apply the seed to the generator
cubiomes.applySeed.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_uint64]
cubiomes.applySeed.restype = None

# Get the biome at specific coordinates
cubiomes.getBiomeAt.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int]
cubiomes.getBiomeAt.restype = ctypes.c_int

# Define a Python class to wrap the generator
class BiomeGenerator:
    def __init__(self, mc_version: int, biome_type: int = 0):
        # Allocate memory for the generator struct
        self.generator = ctypes.create_string_buffer(256)  # Adjust size based on Cubiomes' generator struct
        cubiomes.setupGenerator(ctypes.byref(self.generator), mc_version, biome_type)

    def set_seed(self, seed: int, dimension: int = DIM_OVERWORLD):
        cubiomes.applySeed(ctypes.byref(self.generator), dimension, ctypes.c_uint64(seed))

    def get_biome(self, x: int, y: int, z: int) -> int:
        return cubiomes.getBiomeAt(ctypes.byref(self.generator), x, y, z)

# Example usage of the wrapper
if __name__ == "__main__":
    # Initialize the generator for Minecraft version 1.18
    generator = BiomeGenerator(mc_version=18)

    # Set the seed
    generator.set_seed(123456789)

    # Get the biome at coordinates (0, 63, 0) in the Overworld
    biome_id = generator.get_biome(0, 63, 0)
    print(f"Biome ID at (0, 63, 0): {biome_id}")