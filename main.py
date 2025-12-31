from stats import *
import sys

def get_book_text(path_to_file):
    
    # open the contents of the book
    with open(path_to_file) as f:
        book_text = f.read()

    return book_text

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # store the book as a string
    book_text = get_book_text(sys.argv[1])
    
    # get the count of words 
    total_count_of_words = count_words(book_text)

    # get the count of letters
    total_count_letters = count_characters(book_text)

    # Get the sorted list of dictionaries
    final_stats = sort_character_counts(total_count_letters)

    # Print the results of the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total_count_of_words} total words")
    print("--------- Character Count -------")
    
    # Print them out clearly
    for item in final_stats:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
