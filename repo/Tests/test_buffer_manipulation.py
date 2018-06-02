from unittest import TestCase

from repo.UdpMagic import buffer_manipulation


class TestBuffermanipulation(TestCase):
    def test_buffer_manipulation(self):
        data = ['a', 'b', 'c']
        reversed_data = ['c', 'b', 'a']
        duplicate_data = ['a', 'a', 'b', 'b', 'c', 'c']
        double_data = ['a', 'b', 'c', 'a', 'b', 'c']
        self.assertEqual(buffer_manipulation(data, "reverse"), reversed_data)
        self.assertEqual(buffer_manipulation(data, "duplicate"), duplicate_data)
        self.assertEqual(buffer_manipulation(data, "double"), double_data)
