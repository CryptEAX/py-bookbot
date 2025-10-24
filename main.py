from stats import word_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        print(file_contents)



def main():
    word_count("./books/frankenstein.txt")

main()