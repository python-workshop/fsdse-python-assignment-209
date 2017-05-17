from unittest import TestCase


class TestMax_prod_three(TestCase):
    def test_max_prod_three(self):
        try:
            from build import max_prod_three
        except ImportError:
            self.assertFalse("Function not found")

        self.assertRaises(TypeError, max_prod_three, None)
        self.assertRaises(ValueError, max_prod_three, [1, 2])
        self.assertEqual(max_prod_three([5, -2, 3]), -30)
        self.assertEqual(max_prod_three([5, -2, 3, 1, -1, 4]), 60)