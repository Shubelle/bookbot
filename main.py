def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    num_words = count_words(text)
    char_dict = char_amount(text)
    dict_list = dict_to_list(char_dict)
    print("--- Report of book/frankenstein.txt ---")
    print(f"{num_words} words found in document")
    print()
    #print(sort_list(dict_list))
    for char, count in sort_list(dict_list):
        print(f"'{char}' was found {count} amount of times")
    print("--- End report ---")


def get_book_path(path):
    with open(path) as f:
        return f.read()
    
def count_words(x):
    words = x.split()
    return len(words)

def char_amount(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def dict_to_list(dict):
    new_list = list(dict.items())
    return new_list

def sort_list(list):
    sorted_list = sorted(list, key=lambda i: i[1], reverse=True)
    return sorted_list

main()