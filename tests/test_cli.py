import unittest
import subprocess
import os


class TestAzulCLI(unittest.TestCase):
    def test_cli_json(self):
        filename = 'test_output.json'
        subprocess.run(['python', 'cli.py', '--format', 'json',
                       '--output', 'test_output'], check=True)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

    def test_cli_csv(self):
        filename = 'test_output.csv'
        subprocess.run(['python', 'cli.py', '--format', 'csv',
                       '--output', 'test_output'], check=True)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)
