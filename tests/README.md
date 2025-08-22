# GullsParser Tests

This directory contains comprehensive pytest tests for the GullsParser module.

## Test Structure

### Test Files

- **`test_gulls_parser.py`** - Main test suite covering core functionality
- **`test_incomplete_methods.py`** - Tests for methods that need implementation
- **`conftest.py`** - Test fixtures and configuration
- **`__init__.py`** - Makes tests a proper Python package

### Test Categories

#### 1. Unit Tests (`TestGullsParserInit`, `TestStaticMethods`)
- Test initialization and configuration
- Test static methods like `read_master`, `load_lc_file`, `save_lc_output`
- Test utility functions and calculations

#### 2. Integration Tests (`TestIntegration`)
- Test with real file structure
- Test complete workflows
- Test file name parsing and data flow

#### 3. Error Handling Tests (`TestErrorHandling`, `TestErrorScenarios`)
- Test edge cases and error conditions
- Test malformed files and missing data
- Test graceful failure modes

#### 4. Implementation Guidance Tests (`TestIncompleteMethodImplementation`)
- Test incomplete methods to guide development
- Define expected interfaces for future implementation
- Test placeholder functionality

## Running Tests

### Quick Start
```bash
# Install test dependencies
pip install -r requirements-test.txt

# Run all tests
python run_tests.py

# Or use pytest directly
pytest tests/ -v
```

### Specific Test Categories
```bash
# Run only unit tests
pytest tests/test_gulls_parser.py::TestStaticMethods -v

# Run only integration tests  
pytest tests/test_gulls_parser.py::TestIntegration -v

# Run only incomplete method tests
pytest tests/test_incomplete_methods.py -v

# Skip integration tests
pytest tests/ -m "not integration" -v
```

### Coverage Report
```bash
pytest tests/ --cov=src --cov-report=html
```

## Test Fixtures

The tests use several fixtures defined in `conftest.py`:

- **`temp_dir`** - Temporary directory for test files
- **`sample_lc_file_content`** - Sample light curve file content
- **`sample_master_data`** - Sample master DataFrame
- **`test_project_structure`** - Complete test project structure

## Current Status

### ✅ Implemented and Tested
- Basic class initialization
- Directory structure setup
- File discovery (finding .csv, .hdf5, .lc files)
- Basic error handling for missing files

### 🔄 Partially Implemented
- Master file loading (needs completion for different file types)
- Light curve file parsing (basic structure exists)
- Output file writing (basic structure exists)

### ❌ Not Yet Implemented (Tests Provide Guidance)
- `read_master()` - Reading CSV and HDF5 files
- `concatenate_master_df()` - Combining multiple master files  
- `load_lc_file()` - Complete LC file parsing with comment extraction
- `save_lc_output()` - Proper output file formatting
- `process_single_lens()` - Complete processing pipeline
- Binary and triple lens processing
- Actual astrometric calculations (currently returns zeros)

## Adding New Tests

### For New Features
1. Add test class to appropriate test file
2. Use descriptive test method names starting with `test_`
3. Use appropriate fixtures for setup
4. Test both success and failure cases

### For Bug Fixes
1. Write a test that reproduces the bug
2. Verify the test fails
3. Fix the bug
4. Verify the test passes

### Example Test Structure
```python
class TestNewFeature:
    """Test the new feature functionality."""
    
    def test_feature_success(self, temp_dir):
        """Test successful feature operation."""
        # Setup
        # Execute  
        # Assert
        
    def test_feature_error_handling(self, temp_dir):
        """Test feature error conditions."""
        # Test error scenarios
```

## Test Data

Tests use both:
- **Generated test data** - Created in fixtures for controlled testing
- **Real project data** - Integration tests can use actual files in `input/`

The real data files are:
- `input/1L/wg09_test_ffp.det.hdf5` - Master file
- `input/1L/wg09_test_ffp_1_673_851.det.lc` - Light curve file
- `input/1L/wg09_test_ffp_2_8_573.det.lc` - Light curve file

## Implementation Notes

The tests are designed to:
1. **Guide development** - Tests for incomplete methods show expected interfaces
2. **Catch regressions** - Ensure changes don't break existing functionality  
3. **Document behavior** - Tests serve as executable documentation
4. **Enable refactoring** - Comprehensive tests allow safe code changes

When implementing the incomplete methods, use the tests as a specification for the expected behavior.
