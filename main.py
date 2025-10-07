from stats import count_words, count_characters

def get_book_text(filename):
    with open(filename) as f:
        return f.read()


def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = count_words(text)
    print(f"Found {word_count} total words")
    character_counts = count_characters(text)
    print(character_counts)

main()
