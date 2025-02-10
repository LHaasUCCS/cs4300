import pytest

# Function to count words in a file
def count_words_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as file: # open file for read
        text = file.read()
    return len(text.split()) # split default spaces

# Parametrized test cases
@pytest.mark.parametrize(
    "filename, expected_count", 
    [
        ("Task6_read_me.txt", 104),  
    ]
)
def test_word_count(filename, expected_count):
    assert count_words_in_file(filename) == expected_count

print(count_words_in_file("Task6_read_me.txt"))
