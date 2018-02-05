def task_dictionary(list):
    list_names={}
    for i in range(len(list)):
        list_names[list[i][0]]=[list[i]]
    return list_names





print(task_dictionary(['ahmed', 'fatma', 'Ibrahim']))
