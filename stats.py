def word_count(file_path):
    with open(file_path) as f:
        text = f.read()
        print(f"Found {len(text.split())} total words")

def char_count(file_path):
    with open(file_path) as f:
        text = f.read()
        char_list = {}
        for letter in text:
            if letter.lower() in char_list:
                char_list[letter.lower()] += 1
            else:
                char_list[letter.lower()] = 1
        return char_list


def expanded_dic(char_list):
    sorted = []
    for char in char_list:
        count = char_list[char]
        item = {"char": char, "num": count}
        sorted.append(item)
    return sorted

def sort_dict(list):
    return list["num"]


