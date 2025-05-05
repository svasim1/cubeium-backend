cdef extern from "generator.h":
    # Declare the functions from the Cubiomes library
    ctypedef struct Generator:
        pass

    void setupGenerator(Generator *g, int mc_version, int biome_type)
    void applySeed(Generator *g, int dimension, unsigned long long seed)
    int getBiomeAt(Generator *g, int scale, int x, int y, int z)

# Python wrapper class
cdef class BiomeGenerator:
    cdef Generator generator

    def __init__(self, int mc_version, int biome_type=0):
        setupGenerator(&self.generator, mc_version, biome_type)

    def set_seed(self, int seed, int dimension=0):
        applySeed(&self.generator, dimension, seed)

    def get_biome(self, int x, int y, int z, int scale=1):
        return getBiomeAt(&self.generator, scale, x, y, z)