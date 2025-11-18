from stats import get_word_count
from stats import get_char_count
from stats import sort_dict

def get_book_test(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents


def main():
    filepath = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    frank_txt = get_book_test(filepath)
    word_count = get_word_count(frank_txt)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count = get_char_count(filepath)

    sorted_dict = sort_dict(char_count)
    for i in sorted_dict:
        print(f'{i["char"]}: {i["num"]}')

    print("============= END ===============")

main()
