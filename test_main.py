from main import *
import builtins

# create an instance of the object here
testhang = Hangsaman([])

# Characters Entered:
# 1. Is it a letter?
def test_if_letter_return_true():
    assert testhang.is_letter("l") is True
    assert testhang.is_letter("letter") is True

def test_if_letter_return_false():
    assert testhang.is_letter(4) is False
    assert testhang.is_letter("4") is False

# 2. Is it a single character or multiple?
def test_single_or_multiple_char_false():
    assert testhang.is_not_multiple_chars("lk") is False

def test_single_or_multiple_char_true():
    assert testhang.is_not_multiple_chars("l") is True

# 3. Is the letter in the word?
def test_if_letter_in_word_false():
    secret_word = "testme"
    assert testhang.is_letter_in_word("x") is False

def test_if_letter_in_word_true():
    assert testhang.is_letter_in_word(secret_word[0]) is True

# 4. Did they guess the word?

# Testing if the underscore is changed from a string to a list
def test_change_underscore_from_string_to_list():
    testhang.underscore = '_ _ _ _'
    testhang.change_underscore_from_string_to_list()
    assert testhang.underscore == ["_","_","_","_"]


def xtest_if_word_guessed_is_true():
    with mock.patch.object(builtins, 'input', lambda _: 'jelly'):
        assert is_word_guessed(letter) is True
# def test_is_word_guessed(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: "jelly"):
#     # guess = input("guess a letter test")
#     assert input("guess") == "jelly" is True

