def word_count(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f"Found {len(words)} total words")
