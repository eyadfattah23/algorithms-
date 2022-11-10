import numbers
from unittest import result


def recursive_bin_search(list, target):         ##a recursive function is in that calls itself
    """
    this version wont return the index value,   it will just return a "TRUE" value if it exists and "FALSE" if not 
    """
    if len(list)==0:   ##في البايناري العادية الوايل لووب بتعمل الخطوة ديه علي اساس ان لو الليست فاضية فكدا الاول اكبر من الاخير فهيديك مفيش في الاخر 
        return False
    else:  
        midpoint=len(list)//2
        if list[midpoint]==target:
            return True
        else:
            if list[midpoint] < target:   
                return recursive_bin_search(list[midpoint+1:],target)
            else:
                return recursive_bin_search(list[:midpoint],target)

"""recursive binary search keeps calling itself and with each call to itself the size of the list is cut to half"""
"""so if we keep searching for a target that doesnt exist in the list it will kepp halving it self until it got an empty list"""
"""this is why we define the empty list as a stopping condition"""
def verify(result):
    print(result)

numbers=[0,1,2,3,4,5,6,7,8]
result=recursive_bin_search(numbers,12)
verify(result)

result=result= recursive_bin_search(numbers, 6)
verify(result)

"""
1- the recursive bin search func. called itself inside the bode of the function (L17)
2- when writing a recursive func. you always need a stopping condition and we start the body of our recursive function with the stopping condition 
3- in our recursion we had 2 stopping conditions (1*what a func. should return if an empty list is passed in
                                                  2*if the value at the mid point is the target we return true )
4-just keep calling the function until we hit 1 of the base cases {stopping conditions}                                                  
"""
##############
"""
1-if its not an empty list we get the mid point (L12)
2-once we have the mid point put yout next base case (L13,14)
3- so once you have the base cases the rest of the implementation of the function is to call the func. into smaller sub-lists til we hit on of the stopping conditions  
"""
##the no. of times recursive func. calls itself is called recursive depth 
