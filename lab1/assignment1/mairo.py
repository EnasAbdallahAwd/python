
def task_mairo(num):
    for i in range(num):

        print("" * (num-(i+1))+ "*" *(i+1))




if __name__=='__main__':
    #num=int(input("Enter num"))
    print(task_mairo(3))
