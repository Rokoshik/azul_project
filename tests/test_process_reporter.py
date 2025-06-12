import unittest
from azul.process_reporter import get_processes


class TestAzulProcessReporter(unittest.TestCase):
    def test_get_processes(self):
        data = get_processes()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIn('pid', data[0])
        self.assertIn('name', data[0])
        self.assertIn('username', data[0])
