from memory_profiler import profile, memory_usage



# log_file = open('mem.log', 'w+')


@profile
def myFunction(list_size):
    myList = ['hello'] * list_size
    myList2 = ['world'] * list_size
    del myList2
    return myList


# myFunction(1000000)
# myFunction(1020000)
# myFunction(1030000)


myFunction(1000000)