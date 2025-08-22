""" 
Add astrometric columns to all data files in the inout directory and save the 
new files in the output directory.
"""

# IMPORTS MODULES
import pathlib

# IMPORTS CUSTOM MODULES
from src.gulls_parser import GullsParser

# DATA DIRECTORIES
input_dir = pathlib.Path("input")
output_dir = pathlib.Path("output")

# OUTPUT DIRECTORIES
output_single_lens_dir = output_dir / "1L"
output_binary_lens_dir = output_dir / "2L"
output_triple_lens_dir = output_dir / "3L"

# CREATE OUTPUT DIRECTORIES IF THEY DO NOT EXIST
output_single_lens_dir.mkdir(parents=True, exist_ok=True)
output_binary_lens_dir.mkdir(parents=True, exist_ok=True)
output_triple_lens_dir.mkdir(parents=True, exist_ok=True)

# print 1l master head
gulls_parser = GullsParser()
gulls_parser.load_single_lens_master()

# Show all columns when printing
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(gulls_parser.single_lens_master.head())

