def get_num_words(file):
    with open(file) as f:
        f_contents = f.read()
        words = f_contents.split()
        num_words = 0
        for word in words:
            num_words += 1
    print (f"Found {num_words} total words")

def get_num_char(file):
     with open(file) as f:
        f_contents = f.read()
        chars = f_contents.lower()
        char_dict = {}
        for char in chars:
            if char.isalpha():
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
        return(char_dict)

def sorted_dict(chars):
    list_of_dicts = [{'char': key, 'num': value} for key, value in chars.items()]
    list_of_dicts.sort(reverse=True,  key=lambda item: item['num'])
    for dict in list_of_dicts:
        print(f"{dict["char"]}: {dict["num"]}")
