#Tiegan Cozzie
# October 5, 2021
# Identifies how many times a word appears within an input by the user

import string

alpha=string.ascii_lowercase

def make_word_list(userInput):
    userInput=userInput.lower()
    newInput=""
    for letter in userInput:
       if (letter in alpha) or( letter==" "):
           newInput=newInput+letter
    newInput=newInput.split()
    return newInput

    

def count_freq(words):
    counted=[]
    for i in words:
        if i not in counted:
            counted.append(i)
            
    for i in counted:
        if words.count(i)>1:
            print(i, "appeared", words.count(i), "times")
        else:
            print(i,"appeared once")
                    
                

def main():
    userInput=input("Enter words: ")
    words= make_word_list(userInput)
    print("Words Count: ")
    count_freq(words)

main()
