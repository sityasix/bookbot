def get_word_count(contents):
    return len(contents.split())

def get_char_count(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()

    contents = contents.lower()
    char_dict = {}
    for i in contents:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict

def sort_dict(unsorted_dict):
    sorted_list = []
    for i in unsorted_dict:
        if i.isalpha():
            sorted_list.append({"char": i, "num": unsorted_dict[i]})
    sorted_list.sort(reverse=True, key=get_num_key)
    return sorted_list



def get_num_key(items):
    return items["num"]

