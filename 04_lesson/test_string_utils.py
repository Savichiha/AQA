import unittest
from StringUtils import StringUtils


class TestStringUtils(unittest.TestCase):

    def setUp(self):
        self.utils = StringUtils()

    def test_capitilize(self):
        # Позитивные тесты
        self.assertEqual(self.utils.capitilize("skypro"), "Skypro")
        self.assertEqual(self.utils.capitilize("SkyPro"), "Skypro")

        # Негативные тесты
        self.assertEqual(self.utils.capitilize(""), "")
        self.assertEqual(self.utils.capitilize("123abc"), "123abc")

    def test_trim(self):
        # Позитивные тесты
        self.assertEqual(self.utils.trim("   skypro"), "skypro")
        self.assertEqual(self.utils.trim("skypro"), "skypro")

        # Негативные тесты
        self.assertEqual(self.utils.trim("   "), "")
        self.assertEqual(self.utils.trim(""), "")

    def test_to_list(self):
        # Позитивные тесты
        self.assertEqual(self.utils.to_list("a,b,c,d"), ["a", "b", "c", "d"])
        self.assertEqual(self.utils.to_list("1:2:3", ":"), ["1", "2", "3"])

        # Негативные тесты
        self.assertEqual(self.utils.to_list("", ","), [])
        self.assertEqual(self.utils.to_list("a;b;c;d", ","), ["a;b;c;d"])

    def test_contains(self):
        # Позитивные тесты
        self.assertTrue(self.utils.contains("SkyPro", "S"))
        self.assertFalse(self.utils.contains("SkyPro", "U"))

        # Негативные тесты
        self.assertFalse(self.utils.contains("", "U"))
        self.assertFalse(self.utils.contains("SkyPro", ""))

    def test_delete_symbol(self):
        # Позитивные тесты
        self.assertEqual(self.utils.delete_symbol("SkyPro", "k"), "SyPro")
        self.assertEqual(self.utils.delete_symbol("SkyPro", "Pro"), "Sky")

        # Негативные тесты
        self.assertEqual(self.utils.delete_symbol("SkyPro", "X"), "SkyPro")
        self.assertEqual(self.utils.delete_symbol("", "k"), "")

    def test_starts_with(self):
        # Позитивные тесты
        self.assertTrue(self.utils.starts_with("SkyPro", "S"))
        self.assertFalse(self.utils.starts_with("SkyPro", "P"))

        # Негативные тесты
        self.assertFalse(self.utils.starts_with("", "S"))
        self.assertFalse(self.utils.starts_with("SkyPro", ""))

    def test_end_with(self):
        # Позитивные тесты
        self.assertTrue(self.utils.end_with("SkyPro", "o"))
        self.assertFalse(self.utils.end_with("SkyPro", "y"))

        # Негативные тесты
        self.assertFalse(self.utils.end_with("", "o"))
        self.assertFalse(self.utils.end_with("SkyPro", ""))

    def test_is_empty(self):
        # Позитивные тесты
        self.assertTrue(self.utils.is_empty(""))
        self.assertTrue(self.utils.is_empty(" "))
        self.assertFalse(self.utils.is_empty("SkyPro"))

        # Негативные тесты
        self.assertFalse(self.utils.is_empty(" a "))
        self.assertFalse(self.utils.is_empty("0"))

    def test_list_to_string(self):
        # Позитивные тесты
        self.assertEqual(self.utils.list_to_string([1, 2, 3, 4]), "1, 2, 3, 4")
        self.assertEqual(self.utils.list_to_string(["Sky", "Pro"], "-"), "Sky-Pro")

        # Негативные тесты
        self.assertEqual(self.utils.list_to_string([], ","), "")
        self.assertEqual(self.utils.list_to_string(["Sky"], ","), "Sky")


if __name__ == "__main__":
    unittest.main()