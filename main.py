from stats import get_num_words , get_num_char, sorted_dict
import sys
def main():
    if (len(sys.argv) != 2):
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    char_dict = get_num_char(sys.argv[1])
     
    print("============ BOOKBOT ============\n"
     "Analyzing book found at books/frankenstein.txt...\n"
     "----------- Word Count ----------")
    get_num_words("books/frankenstein.txt")
    print("--------- Character Count -------\n")
    sorted_dict(char_dict)
    print("============= END ===============")

if __name__ == "__main__":
    main()
