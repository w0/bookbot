    
def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print_report(book_path, word_count, letter_count)

def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lower_string = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    count = {}
    
    for letter in alphabet:
        count[letter] = lower_string.count(letter)

    return count

def print_report(path, word_count, letter_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    my_list = []

    for k, v in letter_count.items():
        my_list.append({'name': k, 'count': v})

    my_list.sort(reverse=True, key=sort_on)

    for ltr in my_list:
        print(f"The '{ltr["name"]}' character was found {ltr["count"]} times")

    print("--- End report ---")


def sort_on(dict):
    return dict["count"]

main()