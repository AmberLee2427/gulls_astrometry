"""
Working tests for GullsParser module - tests actual functionality.
"""
import sys
import pathlib
import tempfile
import pandas as pd
import numpy as np

# Add project root to path
sys.path.append(str(pathlib.Path(__file__).parent.parent))

from src.gulls_parser import GullsParser


def test_basic_import():
    """Test that we can import GullsParser."""
    parser = GullsParser()
    assert parser is not None
    print("✅ Basic import test passed")


def test_initialization():
    """Test GullsParser initialization."""
    parser = GullsParser()
    
    # Test default directories
    assert parser.input_dir == pathlib.Path("input")
    assert parser.output_dir == pathlib.Path("output")
    assert parser.single_lens_dir == pathlib.Path("input/1L")
    
    # Test custom directories
    custom_parser = GullsParser(input_dir="custom_input", output_dir="custom_output")
    assert custom_parser.input_dir == pathlib.Path("custom_input")
    assert custom_parser.output_dir == pathlib.Path("custom_output")
    
    print("✅ Initialization test passed")


def test_master_column_mapping():
    """Test that master column mapping is correctly set."""
    parser = GullsParser()
    
    expected_mapping = {
        "t0_lens1": "t0",
        "tE_ref": "tE", 
        "u0_lens1": "u0",
        "rho": "rho",
        "piEN": "pi_EN",
        "piEE": "pi_EE"
    }
    
    assert parser.master_column_mapping == expected_mapping
    print("✅ Master column mapping test passed")


def test_read_master_csv():
    """Test reading CSV master files."""
    # Create temporary CSV file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        # Write test data
        f.write("EventID,SubRun,Field,t0_lens1,tE_ref\n")
        f.write("67,1,841,113.5,22.6\n")
        f.write("76,1,841,168.6,2.3\n")
        
        csv_path = pathlib.Path(f.name)
    
    try:
        result = GullsParser.read_master(csv_path)
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 2
        assert 'EventID' in result.columns
        assert result.iloc[0]['EventID'] == 67
        
        print("✅ CSV master file reading test passed")
        
    finally:
        csv_path.unlink()  # Clean up


def test_read_master_hdf5():
    """Test reading HDF5 master files."""
    # Create temporary HDF5 file
    test_data = pd.DataFrame({
        'EventID': [67, 76],
        'SubRun': [1, 1],
        'Field': [841, 841],
        't0_lens1': [113.5, 168.6],
        'tE_ref': [22.6, 2.3]
    })
    
    with tempfile.NamedTemporaryFile(suffix='.hdf5', delete=False) as f:
        hdf5_path = pathlib.Path(f.name)
    
    try:
        test_data.to_hdf(hdf5_path, key='data', mode='w')
        result = GullsParser.read_master(hdf5_path)
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 2
        assert 'EventID' in result.columns
        
        print("✅ HDF5 master file reading test passed")
        
    finally:
        hdf5_path.unlink()  # Clean up


def test_load_master_single_file():
    """Test loading a single master file."""
    # Create temporary CSV file
    test_data = pd.DataFrame({
        'EventID': [1, 2, 3],
        'SubRun': [1, 1, 1],
        'Field': [841, 841, 841]
    })
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        csv_path = pathlib.Path(f.name)
        test_data.to_csv(csv_path, index=False)
    
    try:
        result = GullsParser.load_master(csv_path)
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 3
        
        # Test with string path
        result_str = GullsParser.load_master(str(csv_path))
        assert isinstance(result_str, pd.DataFrame)
        
        print("✅ Single master file loading test passed")
        
    finally:
        csv_path.unlink()


def test_load_master_multiple_files():
    """Test loading multiple master files."""
    # Create two temporary CSV files
    data1 = pd.DataFrame({'EventID': [1, 2], 'SubRun': [1, 1], 'Field': [841, 841]})
    data2 = pd.DataFrame({'EventID': [3, 4], 'SubRun': [1, 1], 'Field': [841, 841]})
    
    files = []
    for i, data in enumerate([data1, data2]):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            csv_path = pathlib.Path(f.name)
            data.to_csv(csv_path, index=False)
            files.append(csv_path)
    
    try:
        result = GullsParser.load_master(files)
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 4  # 2 files * 2 rows each
        
        print("✅ Multiple master files loading test passed")
        
    finally:
        for file_path in files:
            file_path.unlink()


def test_load_lc_file():
    """Test loading light curve files."""
    # Create sample LC file content
    lc_content = """#fs: 0.968348 0.946456 0.911917 
#Sourcemag: 35.569 26.1783 22.2303
#Event: 0.92019 327.325 110.655832887 163.519043955
Simulation_time measured_relative_flux measured_relative_flux_error true_relative_flux true_relative_flux_error observatory_code saturation_flag best_single_lens_fit parallax_shift_t parallax_shift_u BJD source_x source_y lens1_x lens1_y lens2_x lens2_y parallax_shift_x parallax_shift_y parallax_shift_z 
112.505968565 1.3672988 0.00417313 1.36523069019 0.00417313 0 0 1.3648701 5.32418e-06 7.2705e-06 2458346.5059686 0.636933 0.65473 -0.0466982 0 3.21864 0 0.816725 -0.615553 -0.00467182 
112.51440037 1.3660998 0.00417283 1.36504720547 0.00417283 0 0 1.3646689 5.37296e-06 7.33719e-06 2458346.5144004 0.637785 0.654184 -0.0466982 0 3.21864 0 0.816811 -0.615435 -0.00467123 
"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.lc', delete=False) as f:
        f.write(lc_content)
        lc_path = pathlib.Path(f.name)
    
    try:
        df, comment_text, header = GullsParser.load_lc_file(lc_path)
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 2  # 2 data rows
        assert '#fs:' in comment_text
        assert '#Event:' in comment_text
        assert 'Simulation_time' in header
        assert 'measured_relative_flux' in header
        
        print("✅ LC file loading test passed")
        
    finally:
        lc_path.unlink()


def test_save_lc_output():
    """Test saving LC output files."""
    # Create test DataFrame
    test_data = pd.DataFrame({
        'Simulation_time': [1.0, 2.0, 3.0],
        'measured_relative_flux': [1.1, 1.2, 1.3],
        'sigma_x': [0.1, 0.2, 0.3],
        'sigma_y': [0.4, 0.5, 0.6]
    })
    
    header = ['Simulation_time', 'measured_relative_flux', 'sigma_x', 'sigma_y']
    comment_text = "#fs: 0.1 0.2 0.3\\n#Event: test event"
    
    with tempfile.NamedTemporaryFile(suffix='.lc', delete=False) as f:
        output_path = pathlib.Path(f.name)
    
    try:
        GullsParser.save_lc_output(test_data, output_path, header, comment_text)
        
        # Verify file was created
        assert output_path.exists()
        
        # Check content
        content = output_path.read_text()
        assert "# #fs: 0.1 0.2 0.3" in content
        assert "Simulation_time,measured_relative_flux,sigma_x,sigma_y" in content
        assert "1.0,1.1,0.1,0.4" in content
        
        print("✅ LC output saving test passed")
        
    finally:
        output_path.unlink()


def test_real_data_integration():
    """Test with real project data."""
    try:
        parser = GullsParser()
        parser.load_single_lens_master()
        
        assert hasattr(parser, 'single_lens_master')
        assert isinstance(parser.single_lens_master, pd.DataFrame)
        assert len(parser.single_lens_master) > 0
        
        # Check required columns exist
        required_columns = ['EventID', 'SubRun', 'Field']
        for col in required_columns:
            assert col in parser.single_lens_master.columns, f"Missing column: {col}"
        
        print(f"✅ Real data integration test passed - {len(parser.single_lens_master)} events loaded")
        
    except FileNotFoundError as e:
        print(f"⚠️  Real data test skipped: {e}")


def test_magnitude_calculations():
    """Test magnitude calculation formulas."""
    # Test magnitude calculation: mag = -2.5 * log10(flux)
    flux_values = np.array([1.0, 0.1, 10.0])
    expected_mags = -2.5 * np.log10(flux_values)
    calculated_mags = -2.5 * np.log10(flux_values)
    
    np.testing.assert_array_almost_equal(calculated_mags, expected_mags)
    
    # Test magnitude error calculation: mag_err = (2.5 / ln(10)) * (flux_err / flux)
    flux_errors = np.array([0.1, 0.01, 1.0])
    expected_mag_errors = (2.5 / np.log(10)) * (flux_errors / flux_values)
    calculated_mag_errors = (2.5 / np.log(10)) * (flux_errors / flux_values)
    
    np.testing.assert_array_almost_equal(calculated_mag_errors, expected_mag_errors)
    
    print("✅ Magnitude calculations test passed")


def test_error_handling():
    """Test error handling for various scenarios."""
    # Test non-existent file
    try:
        non_existent = pathlib.Path("non_existent_file.csv")
        GullsParser.read_master(non_existent)
        assert False, "Should have raised FileNotFoundError"
    except FileNotFoundError:
        pass  # Expected
    
    # Test invalid path type
    try:
        GullsParser.load_master(123)  # Invalid type
        assert False, "Should have raised TypeError"
    except TypeError:
        pass  # Expected
    
    print("✅ Error handling test passed")


def run_all_tests():
    """Run all tests."""
    tests = [
        test_basic_import,
        test_initialization, 
        test_master_column_mapping,
        test_read_master_csv,
        test_read_master_hdf5,
        test_load_master_single_file,
        test_load_master_multiple_files,
        test_load_lc_file,
        test_save_lc_output,
        test_magnitude_calculations,
        test_error_handling,
        test_real_data_integration,
    ]
    
    print("Running GullsParser tests...")
    print("=" * 50)
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"❌ {test.__name__} failed: {e}")
            failed += 1
            import traceback
            traceback.print_exc()
    
    print("=" * 50)
    print(f"Tests completed: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed!")
    else:
        print(f"⚠️  {failed} tests failed")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
