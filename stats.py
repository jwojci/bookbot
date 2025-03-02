from collections import defaultdict


def get_num_of_words(book_contents: str):
    return len(book_contents.split())


def get_num_of_occurences(book_contents: str):
    storage = defaultdict(int)
    for char in book_contents:
        char = char.lower()
        storage[char] += 1
    
    return dict(storage)


def sort_dict(count_dict: dict):
    sorted_list = [{k: v} for k, v in sorted(count_dict.items(), key=lambda item: item[1], reverse=True)]
    return sorted_list