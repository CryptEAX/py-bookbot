def word_count(file_path):
    with open(file_path) as f:
        text = f.read()
        print(f"Found {len(text.split())} total words")

# def char_count(file_path):
#     with open(file_path) as f:
#         text = f.read()
#         words = text.split()
#         char_list = {}
#         for word in words:
#             for letter in word:
#                 if letter in char_list:
#                     char_list[letter.lower()] += 1
#                 else:
#                     char_list[letter.lower()] = 1
#         print(char_list)



def char_count(file_path):
    with open(file_path) as f:
        text = f.read()
        char_list = {}
        for letter in text:
            if letter.lower() in char_list:
                char_list[letter.lower()] += 1
            else:
                char_list[letter.lower()] = 1
        print(char_list)