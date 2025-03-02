from stats import get_num_of_words, get_num_of_occurences, sort_dict
import sys 

def get_book_text(filepath: str):
    with open(filepath, "r") as f:
        contents = f.read()
        
    return contents

    
def main():
    print(sys.argv)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_of_words = get_num_of_words(text)
    num_of_occ = get_num_of_occurences(text)
    sorted_occ = sort_dict(num_of_occ)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for d in sorted_occ:
        for k, v in d.items():
            print(f"{k}: {v}")
    print("============= END ===============")


    

main()