word = input("Enter a word: ")
word_length = len(word) - 1

loopCounter = 0

while (loopCounter <= word_length):
    if(word[loopCounter]) == word[word_length - loopCounter]:
        if(loopCounter == word_length):
            print("This word is a palindrome.")
            break
    else:
        print("This ain't no palindrome.")
        break
    loopCounter += 1
