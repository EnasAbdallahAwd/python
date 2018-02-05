def MultiplicationTable(num):
    list1 = []
    for i in range(num):
        list2 = []
        i += 1
        for x in range(i):
            x+=1
            list2.append(i*x)
        list1.append(list2)

    return list1

if __name__=='__main__':
    num=int(input("Enter num"))
    print(MultiplicationTable(num))
