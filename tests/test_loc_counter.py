import os
import tempfile
import tools.repo_introspect.loc_counter

def test_count_loc_by_ext():
    # Create a temporary directory structure
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create some test files
        py_file = os.path.join(tmpdir, 'test.py')
        md_file = os.path.join(tmpdir, 'test.md')
        
        # Write content to files
        with open(py_file, 'w') as f:
            f.write('print("hello")\nprint("world")\n')
        
        with open(md_file, 'w') as f:
            f.write('# Test\n\nThis is a test file.\n')
        
        # Call the function
        result = tools.repo_introspect.loc_counter.count_loc_by_ext(tmpdir)
        
        # Verify results
        assert '.py' in result
        assert '.md' in result
        assert result['.py'] == 2  # 2 non-empty lines
        assert result['.md'] == 3  # 3 non-empty lines
        
        print("Test passed!")
        
if __name__ == '__main__':
    test_count_loc_by_ext()
