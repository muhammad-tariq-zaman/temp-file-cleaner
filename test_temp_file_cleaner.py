import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


class TestTempCleaner(unittest.TestCase):
    def test_scan_finds_only_temp(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, "a.tmp"), "w").write("x" * 5)
            open(os.path.join(d, "keep.txt"), "w").write("x" * 5)
            open(os.path.join(d, "b.bak"), "w").write("x" * 3)
            found = dict(main.scan(d))
            self.assertEqual(len(found), 2)
            self.assertEqual(sum(found.values()), 8)


if __name__ == "__main__":
    unittest.main()
