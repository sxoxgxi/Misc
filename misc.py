def add_ing(word: str) -> str:
    last = word[-3::]
    if len(word) >= 3 and last != 'ing':
        return word + 'ing'
    elif len(word) >= 3 and last == 'ing':
        word = word.replace("ing", 'ly')
        return word
    else:
        return 'provide atleast 3 characters long word'


hi = input("Enter a word: ")
print(add_ing(hi))
