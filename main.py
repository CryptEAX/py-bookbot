import sys
from stats import word_count
from stats import char_count
from stats import expanded_dic
from stats import sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        print(file_contents)



def main():
    try:
        filepath = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}")
        print("----------- Word Count ----------")
        word_count(filepath)
        print("--------- Character Count -------")
        count = expanded_dic(char_count(filepath))
        count.sort(reverse=True, key=sort_dict)
        for c in count:
            letter, num = c["char"], c["num"]
            if letter.isalpha() == True:
                print(f"{letter}: {num}")
        print("============= END ===============")
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()