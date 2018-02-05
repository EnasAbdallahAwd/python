

def charvowels(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    NewWord=""
    for  word in myword:
        if word   not in  vowels:
            NewWord+=word

    return NewWord



if __name__=='__main__':
    myword=input("Enter word")
    print(charvowels(myword))
