#Code to check weather a given word or sentence is a palindrome
while True: 
    word = input("Enter the word to check: ").lower()
    new = ""
    word_length = len(word)
    word_length = word_length - 1
    
    
    for i in range(word_length, -1, -1):
        new = new + word[i]
        print(word[i])

    


    if new == word:
        print(f"{word} is a palindrome")

    else:
        print(f"{word} is not a palindrome")


