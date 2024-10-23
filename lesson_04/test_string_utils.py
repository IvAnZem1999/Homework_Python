import pytest
from string_utils import StringUtils
utils = StringUtils()
def test_capitalize():
    # positive
    assert utils.capitilize("ivan") == "Ivan"
    assert utils.capitilize("hello world") == "Hello world"
    assert utils.capitilize("1234") == "1234"
    # negative
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("12user") == "12user"


def test_trim():
    #positive
    assert utils.trim("   world") == "world"
    assert utils.trim("  123") == "123"
    assert utils.trim("  05 may") == "05 may"
    # negative
    assert utils.trim( "") == ""
    assert utils.trim( "123  ") == "123  "
    

def test_to_list():
    #positive
    assert utils.to_list("1:2:3", ":") == ["1" , "2" , "3"]
    assert utils.to_list("Mark,Krein") == ["Mark" , "Krein"]
    # negative
    assert utils.to_list(",,") == ["" , "" , ""]


def test_contains():
    #positive
    assert utils.contains("World", "W") == True
    assert utils.contains("World", "F") == False
    #negative
    assert utils.contains("   ", " ") == True
    assert utils.contains("  ", "J") == False


def test_delete_symbol():
    #positive
    assert utils.delete_symbol("World", "l") == "Word"
    assert utils.delete_symbol("IronMan", "Man") == "Iron"
    #negative
    assert utils.delete_symbol(" ", " ") == ""
    assert utils.delete_symbol("!@#$", "@") == "!#$"

    
def test_start_witch():
    #positive
    assert utils.starts_with("World", "W") == True
    assert utils.starts_with("05 may", "0") == True
    assert utils.starts_with("IronMan", "L") == False
    #negative
    assert utils.starts_with("!@#", "!") == True
    assert utils.starts_with("!@#", "#") == False
    assert utils.starts_with("  ", " ") == True


def test_end_witch():
    #positive
    assert utils.end_with("World", "d") == True
    assert utils.end_with("05 may", "y") == True
    assert utils.end_with("IronMan", "L") == False
    #negative
    assert utils.end_with("!@#", "#") == True
    assert utils.end_with("!@#", "!") == False
    assert utils.end_with("  ", " ") == True


def test_is_empty():
    #positive
    assert utils.is_empty("") == True
    assert utils.is_empty("  ") == True
    assert utils.is_empty("22") == False
    #negative
    assert utils.is_empty("213438576752333333358988477388057") == False


def test_list_to_string():
    #positive
    assert utils.list_to_string(["1, 2, 3"]) == "1, 2, 3"
    assert utils.list_to_string(["01 may, 02 may, 03 may"]) == "01 may, 02 may, 03 may"
    #negative
    assert utils.list_to_string([""]) == ""
    assert utils.list_to_string([" , , "]) == " , , "