import unittest
from algorithm import search
class TestSearch(unittest.TestCase):
  def setUp(self):
    self.array = [10, 5, 20, 30, 1, 4]

  def test_successful(self):
    self.assertTrue(search(self.array, 20, 5))

  def test_failed(self):
    self.assertFalse(search(self.array, 100, 3))

  def test_emptyArray(self):
    self.assertFalse(search([], 10, 5))



  def test_searchingNoneFailed(self):
    self.assertFalse(search(self.array, None, None))

  def test_searchingNoneSuccessful(self):
    self.assertTrue(search([None], None, None))


if __name__ == '__main__':
    unittest.main()


