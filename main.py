from stats import count_words, count_characters, sort_characters_by_counts

def get_book_text(filename):
    with open(filename) as f:
        return f.read()


def main():
    filename = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}")

    text = get_book_text(filename)
    word_count = count_words(text)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    character_counts = count_characters(text)
    #print(character_counts)
    sorted_counts = sort_characters_by_counts(character_counts)
    #print(sorted_counts)

    for count in sorted_counts:
        char = count["char"]
        how_many = count["count"]
        if char.isalpha():
            print(f"{char}: {how_many}")
    print("============= END ===============")


main()
