import unittest
from memory import Memory

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.mem = Memory()

    def test_add_memory(self):
        self.assertEqual(self.mem.Add(10), 10)
        self.assertEqual(self.mem.Add(-5), 5)

    def test_subtract_memory(self):
        self.mem.Add(10)
        self.assertEqual(self.mem.Subtract(5), 5)

    def test_clear_memory(self):
        self.mem.Add(10)
        self.assertEqual(self.mem.Clear(), 0)

    def test_read_memory(self):
        self.mem.Add(15)
        self.assertEqual(self.mem.Read(), 15)

if __name__ == '__main__':
    unittest.main()
