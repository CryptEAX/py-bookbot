from stats import word_count
from stats import char_count
from stats import expanded_dic
from stats import sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        print(file_contents)



def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_count("./books/frankenstein.txt")
    print("--------- Character Count -------")
    count = expanded_dic(char_count("./books/frankenstein.txt"))
    count.sort(reverse=True, key=sort_dict)
    for c in count:
        letter, num = c["char"], c["num"]
        if letter.isalpha() == True:
            print(f"{letter}: {num}")
    print("============= END ===============")
main()