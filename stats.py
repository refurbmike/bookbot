import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def word_count(book_text):
    book_words = book_text.split()
    return len(book_words)

def letter_count(book_text):
    letters = book_text.lower()
    letter_dict = {}

    for letter in letters:
        if letter.isalpha():
            if letter not in letter_dict:
                letter_dict[letter] = 0 
            letter_dict[letter] += 1
    return letter_dict

def get_count(item):
    return item[1]

def sort_letter_counts(letter_dict):
    letter_list = list(letter_dict.items())
    letter_list.sort(key=get_count, reverse=True)
    return letter_list

def main():
    book_text = get_book_text(book_path)
    letters_dict = letter_count(book_text)
    sorted_letters = sort_letter_counts(letters_dict)  
#    print(f"{word_count(book_text)} words found in the document")
#    print(letter_count(book_text))
#    print(sorted_letters)

main()