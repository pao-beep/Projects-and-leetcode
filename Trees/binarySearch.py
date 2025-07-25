def BinarySearch(list,item):

    list_len = len(list)
    if list_len == 0:
        return "n/a"
    list.sort()
    print(list)
    found = None
    temp = list
    while found is None:
        partition = len(temp)//2
        print(temp)
        print(f"partition:{partition}")
        # if (partition % 2) != 0:
        #     partition+=1

        if item == temp[partition]:
            found= temp[partition]
            break
        if item > temp[partition]:
            temp = temp[partition:]
        if len(temp)==1 and found is None:
            return "not found"
        else:
            temp = temp[:partition]
    return found
#ret =BinarySearch([4,9,3,1,7,0,2],1)
#ret =BinarySearch([4,9,3,1,7,0],9)
#ret =BinarySearch([4,9,3,1,7,0],7)
#ret =BinarySearch([4,9,3,1,7,0,2],0)
ret=BinarySearch([0, 2, 4, 6, 8, 10, 12, 14, 16],9)
print(f"ret:{ret}")



