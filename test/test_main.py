"""Test file for testing the main.py file"""

import unittest # for creating the test case
from unittest.mock import patch # for mocking the input
import io # for capturing the output
import sys # for restoring the stdout and removing the main module from the cache
import importlib # for importing the main.py file
from pathlib import Path # for getting the path of the main.py file

class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """Sets up the test environment by removing the main module from the cache"""
        super().setUp()
        sys.modules.pop("main", None)

    @patch("builtins.input", side_effect=["1", "2"])
    def test_soma_1_2(self, _mock_input):
        """Testa se o programa imprime 3 quando o usuário digita 1 e depois 2"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("3", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["0", "0"])
    def test_soma_0_0(self, _mock_input):
        """Testa se o programa imprime 0 quando o usuário digita 0 e depois 0"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("0", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["7", "3"])
    def test_soma_7_3(self, _mock_input):
        """Testa se o programa imprime 10 quando o usuário digita 7 e depois 3"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("10", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["7", "-7"])
    def test_soma_7_m7(self, _mock_input):
        """Testa se o programa imprime 0 quando o usuário digita 7 e depois -7"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("0", captured_output.getvalue().strip())

if __name__ == "__main__":
    # add the parent directory to the path in order to run it from the run command in vscode
    main_file_folder = Path(__file__).parents[1].as_posix() # pylint: disable=invalid-name
    sys.path.insert(0, main_file_folder)
    unittest.main()
