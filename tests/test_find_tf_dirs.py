import os
import tempfile
import unittest
from python.find_tf_dirs import find_tf_directories

class TestFindTFDirectories(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory with subdirectories and sample files.
        self.test_dir = tempfile.TemporaryDirectory()
        base_dir = self.test_dir.name

        # Create subdirectories.
        os.makedirs(os.path.join(base_dir, "dir1"), exist_ok=True)
        os.makedirs(os.path.join(base_dir, "dir2"), exist_ok=True)
        os.makedirs(os.path.join(base_dir, "dir3"), exist_ok=True)

        # In dir1, add a *.tf file.
        with open(os.path.join(base_dir, "dir1", "resource.tf"), "w") as f:
            f.write("resource \"aws_instance\" \"example\" {}")

        # In dir2, add a *.tf.json file.
        with open(os.path.join(base_dir, "dir2", "config.tf.json"), "w") as f:
            f.write("{}")

        # In dir3, add a file that should not trigger inclusion.
        with open(os.path.join(base_dir, "dir3", "README.md"), "w") as f:
            f.write("Nothing to see here.")

    def tearDown(self):
        # Clean up the temporary directory.
        self.test_dir.cleanup()

    def test_find_tf_directories(self):
        # Running find_tf_directories on our temporary structure.
        base_dir = self.test_dir.name
        result = find_tf_directories(base_dir)

        # Expect 'dir1' and 'dir2' to be in the result.
        expected_dir1 = os.path.join(base_dir, "dir1")
        expected_dir2 = os.path.join(base_dir, "dir2")
        expected_dir3 = os.path.join(base_dir, "dir3")  # This should not be included.

        self.assertIn(expected_dir1, result)
        self.assertIn(expected_dir2, result)
        self.assertNotIn(expected_dir3, result)

if __name__ == "__main__":
    unittest.main()
