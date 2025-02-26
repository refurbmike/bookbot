import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

from stats import word_count, letter_count, get_book_text, sort_letter_counts
book_text = get_book_text(book_path)
letters_dict = letter_count(book_text)
sorted_letters = sort_letter_counts(letters_dict)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")

print(f"Found {word_count(book_text)} total words")

print("--------- Character Count -------")

def formatted_list(sorted_letters):
    for letter, count in sorted_letters:
        print(f"{letter}: {count}")

formatted_list(sorted_letters)

print("============= END ===============")