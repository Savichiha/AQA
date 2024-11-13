import pytest
from StringUtils import StringUtils

utils = StringUtils()


def test_capitilize():
    # Позитивные тесты
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("SkyPro") == "Skypro"

    # Негативные тесты
    assert utils.capitilize("") == ""
    assert utils.capitilize("123abc") == "123abc"


def test_trim():
    # Позитивные тесты
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("skypro") == "skypro"

    # Негативные тесты
    assert utils.trim("   ") == ""
    assert utils.trim("") == ""


def test_to_list():
    # Позитивные тесты
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]

    # Негативные тесты
    assert utils.to_list("", ",") == []
    assert utils.to_list("a;b;c;d", ",") == ["a;b;c;d"]


def test_contains():
    # Позитивные тесты
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "U") is False

    # Негативные тесты
    assert utils.contains("", "U") is False
    assert utils.contains("SkyPro", "") is False


def test_delete_symbol():
    # Позитивные тесты
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

    # Негативные тесты
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"
    assert utils.delete_symbol("", "k") == ""


def test_starts_with():
    # Позитивные тесты
    assert utils.starts_with("SkyPro", "S") is True
    assert utils.starts_with("SkyPro", "P") is False

    # Негативные тесты
    assert utils.starts_with("", "S") is False
    assert utils.starts_with("SkyPro", "") is False


def test_end_with():
    # Позитивные тесты
    assert utils.end_with("SkyPro", "o") is True
    assert utils.end_with("SkyPro", "y") is False

    # Негативные тесты
    assert utils.end_with("", "o") is False
    assert utils.end_with("SkyPro", "") is False


def test_is_empty():
    # Позитивные тесты
    assert utils.is_empty("") is True
    assert utils.is_empty(" ") is True
    assert utils.is_empty("SkyPro") is False

    # Негативные тесты
    assert utils.is_empty(" a ") is False
    assert utils.is_empty("0") is False


def test_list_to_string():
    # Позитивные тесты
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"

    # Негативные тесты
    assert utils.list_to_string([], ",") == ""
    assert utils.list_to_string(["Sky"], ",") == "Sky"