from stats import count_words_in_text, count_characters_in_text, sort_list_of_characters
import sys, os

def get_book_text(f_path) -> str:
    with open(f_path, 'r') as f:
        return f.read()


def main():
    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book[2:]}...")
    text = get_book_text(book)
    num_words = count_words_in_text(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    chars_count = count_characters_in_text(text)
    sorted_list = sort_list_of_characters(chars_count)
    print("--------- Character Count -------")
    for c in sorted_list:
        if not c['character'].isalpha():
            continue
        print(f"{c['character']}: {c['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()
