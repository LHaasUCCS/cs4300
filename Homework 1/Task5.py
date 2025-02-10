# List 
favorite_books = [
    {"title": "The Hobbit", "author": "JRR Tolkien"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "Moby Dick", "author": "Herman Melville"}
]

# List slicing 
def list_slicing():
    new_list = []
    first_three_books = favorite_books[:3]
    print("First three books:")
    for book in first_three_books:
        new_list.append(book)
    return new_list

# Dictionary 
student_database = {
    "student_001": {"name": "John Doe", "id": "S001"},
    "student_002": {"name": "Jane Smith", "id": "S002"},
    "student_003": {"name": "Alice Johnson", "id": "S003"},
}

new_list = list_slicing()

def test_favorite_books():
    assert len(favorite_books) == 4
    assert favorite_books[0]["title"] == "The Hobbit"
    assert favorite_books[0]["author"] == "JRR Tolkien"

def test_first_three_books():
    assert len(new_list) == 3
    assert new_list[0]["title"] == "The Hobbit"
    assert new_list[0]["author"] == "JRR Tolkien"
    assert new_list[2]["title"] == "The Great Gatsby"
    assert new_list[2]["author"] == "F. Scott Fitzgerald"

def test_student_database():
    assert len(student_database) == 3
    assert student_database["student_001"]["name"] == "John Doe"
    assert student_database["student_002"]["id"] == "S002"