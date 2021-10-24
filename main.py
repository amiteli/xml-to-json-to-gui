def initialize():
    # Reading the data inside the xml
    # file to a variable under the name
    # data
    with open('file_example.xml', 'r') as f:
        data = f.read()
    bs_data = BeautifulSoup(data, 'xml')

    return bs_data


def subclass(book):
    attributes = {}

    for child in book:
        if child.name is not None and child.string is not None:
            attributes.update({child.name: child.string})

    return attributes


def bookID(book):
    name = list(book.attrs.keys())[0]
    ID = book.attrs[name]
    return ID


def converter(x):
    # convert into JSON
    x = json.dumps(x)
    x = json.loads(x)
    return x

if __name__ == "__main__":
    from bs4 import BeautifulSoup
    import json

    bs_data = initialize()

    catalog = {}
    file = {}
    books = bs_data.find_all('book')
    for i in range(len(books)):
        newbookID = bookID(books[i])
        newbook = subclass(books[i])
        catalog.update({newbookID: newbook})
    file.update({bs_data.contents[0].name: catalog})

    file = converter(file)
    print(file)