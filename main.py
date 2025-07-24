import sys
from stats import get_num_words
from stats import get_character_count
from stats import get_formatted_stats
print("============ BOOKBOT ============")
if len(sys.argv) < 2:    
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  

book = sys.argv[1]

def get_book_text(path):
    try:
        with open(path) as book:
            return book.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' does not exist.")
        sys.exit(1)
    
def main():
    text = get_book_text(book)
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    word_count, word_dict = get_num_words(text)
    word_dict = get_formatted_stats(word_dict)
    print(f"Found {word_count} total words")
    print(f"--------- Top 100 Words ---------")
    count = 0
    for w in word_dict:
        if count < 100:
            count += 1
            print(f"{w['char']}: {w['num']}")
    print("--------- Character Count -------")
    character_count = get_character_count(text)
    character_count = get_formatted_stats(character_count)
    for char_dict in character_count:
        print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")
main()