from combiner import Combiner

import unittest


class TestCombiner(unittest.TestCase):
    def setUp(self):
        self.test_class = Combiner()

    def test_empty_filepaths(self):
        with self.assertRaises(FileNotFoundError):
            self.test_class.check_csv_filepaths([])

    def test_not_exists_filepaths(self):
        with self.assertRaises(FileNotFoundError):
            self.test_class.check_csv_filepaths(['not_exists_files.csv'])

    def tearDown(self):
        del self.test_class


if __name__ == '__main__':
    unittest.main()
