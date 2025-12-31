# function to count words in the string by splitting them
def count_words(string_to_split):
    tally = len(string_to_split.split())

    return tally

# function to count characters
def count_characters(string_to_count):

    # convert all of the string in the book to lowercase 
    lower_case_string = string_to_count.lower()

    counts = {}

    for letter in lower_case_string:
        counts[letter] = counts.get(letter, 0) + 1

    return counts

def sort_character_counts(char_dict):
    # 1. Convert dictionary items to a list of tuples
    items_list = list(char_dict.items())
    
    # 2. Sort the list by the count (index 1) in descending order
    # Using a lambda function to target the integer value
    items_list.sort(key=lambda x: x[1], reverse=True)
    
    # 3. Create a list of single-item dictionaries
    sorted_list = []
    for char, count in items_list:
        # We only care about alphabetic characters for these stats
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
            
    return sorted_list