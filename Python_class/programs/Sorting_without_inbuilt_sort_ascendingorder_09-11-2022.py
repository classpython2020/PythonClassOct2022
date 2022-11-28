
#ascending order
#this is how to sort the list of elements without using sort method

def sortingwithoutinbuiltsort_ascendingorder(data):
    list=[]
    while data:
        min=data[0]
        for i in data:
            if i <min:
                min=i
        list.append(min)
        data.remove(min)
    print(list)

sortingwithoutinbuiltsort_ascendingorder([1,23,4,56,6])


