import pytest

import pytest


# Define the reverse_string function
def reverse_string(string):
  return string[::-1]


# Here is an example of a test function
def test_reversed_string():
  assert reverse_string("hello") == "olleh"
  assert reverse_string("world") == "dlrow"


# Here is an example of a test class
class TestStringFunctions:

  def test_upper(self):
    assert "hello".upper() == "HELLO"

  def test_isupper(self):
    assert "HELLO".isupper()
    assert not "Hello".isupper()

  def test_split(self):
    s = "hello world"
    assert s.split() == ["hello", "world"]
    with pytest.raises(TypeError):
      s.split(2)
