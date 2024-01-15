def main():
    def get_key(val, my_dict):
   
        for key, value in my_dict.items():
            if val == value:
                return key
 
        return "key doesn't exist"

    chars_dict = {}
    lst_chars = []
    num_words = 0
    with open("./books/frankenstein.txt") as frankenstein:
        book = frankenstein.read()
        words = book.split()
        for word in words:
            num_words += 1
            chars = [x for x in word.lower()]
            for char in chars:
                if char.isalpha():
                    if not char in chars_dict:
                        chars_dict[char] = 0
                    chars_dict[char] += 1
        
        lst_chars = list(chars_dict.values())
        lst_chars.sort(reverse=True)
        print("--- Begin report of books/frankenstein.txt ---")
        print(F"{num_words} words found in the document")
        print("")
        for num in lst_chars:
            print(f"The '{get_key(num, chars_dict)}' character was found {num} times")
        print("--- End report ---")
        


main()
