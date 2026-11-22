import json

def show_books(books):
    for book in books:
        print(book["name"], "- prioriy: ", book["prioriy"])

def save_books(books):
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=2)

def load_books():
    
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def show_books(books):
    print("\n--- Your Book Collection ---")
    if not books:
        print("Your library is empty.")
    else:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")
        print(f"\nTotal books: {len(books)}")
    print("--------------------------\n")
