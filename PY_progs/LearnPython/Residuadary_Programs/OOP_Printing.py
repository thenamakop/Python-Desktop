class book():
    title = None
    author = None
    edition = None
    Publisher = None
    genre = None
    price = None

SherlockHolmes = book()

SherlockHolmes.title = "Sherlock Holmes"
SherlockHolmes.author = "Arthur Conan Doyle"
SherlockHolmes.edition = "First"
SherlockHolmes.Publisher = "Penguin Books"
SherlockHolmes.genre = "Crime, Mystery"
SherlockHolmes.price = "500"

OxfordDictionary = book()

OxfordDictionary.title = "Oxford Dictionary"
OxfordDictionary.author = "Oxford University Press"
OxfordDictionary.edition = "Indian Edition"
OxfordDictionary.Publisher = "Oxford University Press"
OxfordDictionary.genre = "Dictionary"
OxfordDictionary.price = "1122"

def print_book_details(book):
    for attribute in dir(book):
        if not attribute.startswith("__"):
            print(f"{attribute}: {getattr(book, attribute)}")

print_book_details(SherlockHolmes)
print_book_details(OxfordDictionary)