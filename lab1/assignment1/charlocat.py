
def charLocat(text, letter):
    list=[]

    for pos, char in enumerate(text):
        if char == letter:
            list.append(pos)
    return list

if __name__=='__main__':
    text=input("Enter text")
    letter=input("Enter letter to select:")
    print(charLocat(text,letter))
