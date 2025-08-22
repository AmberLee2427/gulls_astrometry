"""
Pytest configuration file for GullsParser tests.
"""
import pytest
import tempfile
import shutil
import pathlib
import pandas as pd
from typing import Generator


@pytest.fixture
def temp_dir() -> Generator[pathlib.Path, None, None]:
    """Create a temporary directory for test files."""
    temp_path = pathlib.Path(tempfile.mkdtemp())
    yield temp_path
    shutil.rmtree(temp_path)


@pytest.fixture
def sample_lc_file_content() -> str:
    """Sample light curve file content for testing."""
    return """#fs: 0.968348 0.946456 0.911917 
#Sourcemag: 35.569 26.1783 22.2303 19.5046 19.3117 17.7303 16.953 16.5804 14.7459 19.0443 16.0382 
#Sourcedata: 29650 -8.64531 2.26471 45.238 61.677 -94.5465 96.4017 0.923965 2 10 4730.68 2.46395 0 0.922167 0.767067 9.32001 -0.517316 0.410646 -0.589734 267.223 -28.8905 8.30801 0.129165 0.0595409 -0.0857799 13.7366 0 
#Obssrcmag: 19.3117 26.1783 16.5804 
#Lensmag: 41.1432 31.7535 27.8141 25.0951 24.9053 23.3287 22.5571 22.1803 20.3458 24.6343 21.6396 
#Lensdata: 43423 -3.09634 1.8829 214.067 228.69 127.933 77.5453 0.694459 0 10 4769.48 4.61032 0 0.694385 6.40544 0.683356 -0.202709 0.400301 -0.60246 267.229 -28.9059 8.11897 -0.0598735 0.0567201 -0.0852444 13.7366 0 
#Obslensmag: 24.9053 31.7535 22.1803 
#Planet: 0.0100746 4.60334 43.4864 276.997 0.0145087 3.26534 11.7674 
#Event: 0.92019 327.325 110.655832887 163.519043955 -0.296902 2.2893 8.33479 0.0411327 
#Obsgroup: 0 3.51242e+06 0 1044.31 0 1 2 
Simulation_time measured_relative_flux measured_relative_flux_error true_relative_flux true_relative_flux_error observatory_code saturation_flag best_single_lens_fit parallax_shift_t parallax_shift_u BJD source_x source_y lens1_x lens1_y lens2_x lens2_y parallax_shift_x parallax_shift_y parallax_shift_z 
112.505968565 1.3672988 0.00417313 1.36523069019 0.00417313 0 0 1.3648701 5.32418e-06 7.2705e-06 2458346.5059686 0.636933 0.65473 -0.0466982 0 3.21864 0 0.816725 -0.615553 -0.00467182 
112.51440037 1.3660998 0.00417283 1.36504720547 0.00417283 0 0 1.3646689 5.37296e-06 7.33719e-06 2458346.5144004 0.637785 0.654184 -0.0466982 0 3.21864 0 0.816811 -0.615435 -0.00467123 
112.522832176 1.3606156 0.00417252 1.36486304973 0.00417252 0 0 1.3644672 5.42197e-06 7.4042e-06 2458346.5228322 0.638636 0.653638 -0.0466982 0 3.21864 0 0.816897 -0.615317 -0.00467063 
"""


@pytest.fixture
def sample_master_data() -> pd.DataFrame:
    """Sample master DataFrame for testing."""
    return pd.DataFrame({
        'EventID': [67, 76, 84],
        'SubRun': [1, 1, 1],
        'Field': [841, 841, 841],
        'galactic_l': [1.256491, 1.170004, 1.271671],
        'galactic_b': [-2.222655, -2.264559, -2.299232],
        't0lens1': [113.588110, 168.607977, 178.265612],
        'tE_ref': [22.595860, 2.320796, 10.092309],
        'u0lens1': [0.418063, 0.395149, 0.273929],
        'rho': [0.002698, 0.003156, 0.003004],
        'piEN': [0.090032, -0.018454, -0.081317],
        'piEE': [0.011362, -0.011969, 0.030994],
        'alpha': [303.083675, 229.654620, 163.623397],
        'q': [0.000997, 0.005000, 0.013573],
        's': [2.713747, 0.876284, 1.258564]
    })


@pytest.fixture
def test_project_structure(temp_dir: pathlib.Path, sample_lc_file_content: str, sample_master_data: pd.DataFrame):
    """Create a complete test project structure."""
    # Create directory structure
    input_dir = temp_dir / "input"
    output_dir = temp_dir / "output"
    
    single_lens_dir = input_dir / "1L"
    binary_lens_dir = input_dir / "2L"
    triple_lens_dir = input_dir / "3L"
    
    for dir_path in [single_lens_dir, binary_lens_dir, triple_lens_dir]:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    for dir_path in [output_dir / "1L", output_dir / "2L", output_dir / "3L"]:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    # Create sample light curve files
    lc_file1 = single_lens_dir / "wg09_test_ffp_1_841_67.det.lc"
    lc_file2 = single_lens_dir / "wg09_test_ffp_1_841_76.det.lc"
    
    lc_file1.write_text(sample_lc_file_content)
    lc_file2.write_text(sample_lc_file_content.replace("67", "76"))
    
    # Create sample master file (CSV)
    master_file = single_lens_dir / "master.csv"
    sample_master_data.to_csv(master_file, index=False)
    
    # Create sample master file (HDF5)
    hdf5_file = single_lens_dir / "master.hdf5"
    sample_master_data.to_hdf(hdf5_file, key='data', mode='w')
    
    return {
        'temp_dir': temp_dir,
        'input_dir': input_dir,
        'output_dir': output_dir,
        'single_lens_dir': single_lens_dir,
        'binary_lens_dir': binary_lens_dir,
        'triple_lens_dir': triple_lens_dir,
        'lc_files': [lc_file1, lc_file2],
        'master_files': [master_file, hdf5_file]
    }
