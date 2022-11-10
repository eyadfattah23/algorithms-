import numbers
from unittest import result


def linear_search(list, target):
    """
    returns the index position of the target if found, else returns None
    """
    for i in range(0, len(list)):
        if list[i]== target:
            return i
    return None       
       
             

        
"""
len--->get the no. of items in list 
i--->index
"""




def verify(index):
    if index is not None:
        print("target found at index: ",index)
    else:
            print("target not found in list")

numbers=[1,2,3,4,5,6,7,8,9,10]


result=linear_search(numbers, 12)
verify(result) 
"""هنا انتا متوقع انك متلاقيش التارجت عشان التارجت 12 ونتا اخرك 10 """
##expected output 'target not found in list'


result=linear_search(numbers, 6)
verify(result) 
"""هنا انت بتجيب موقع رقم 6 اللي هو الخامس بالنسبة للغة البرمجة """
##expected output 'target found at index:  5'

