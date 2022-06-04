# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


print("Enter the word to be checked: ")
word = str(input())
print("Enter the anagram which the word is to be checked against: ")
anagram = str(input())

def find_anagram(word, anagram):
    split_word = []
    split_word.extend(word)

    word_check_rating = 0
    
    for char in split_word:
        if char in anagram:
            word_check_rating += 1
        else:
            word_check_rating += 0
            
    if word_check_rating < len(anagram):
        print(False)
    else:
        print(True)


find_anagram(word, anagram)

        

