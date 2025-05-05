from setuptools import setup, Extension
from Cython.Build import cythonize

# Define the extension module
extensions = [
    Extension(
        "wrapper",  # Name of the generated module
        ["  wrapper.pyx"],  # Cython source file
        libraries=["cubiomes"],  # Link against the Cubiomes library
        library_dirs=["../../cubiomes"],  # Path to the compiled Cubiomes library
        include_dirs=["../../cubiomes"],  # Path to the Cubiomes header files
    )
]

# Setup script
setup(
    name="cubiomes_wrapper",
    ext_modules=cythonize(extensions),
)