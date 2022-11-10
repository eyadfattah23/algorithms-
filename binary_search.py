def binary_search(list, target):         ##remember:bin.search works by breaking the array into smaller sets untill we find the target
    first=0
    last=len(list)-1  
 ##هنا انتا محتاج الطول بس الفكرة ان البداية 0 
    #    """list positions starts at 0 not 1"""
     #"""we used 'first' and 'last' to point at the beginning and the end of the list"""

    while first<=last:        ## remember: a while loop takes a condition and keeps executing the code until the condition is false 
        midpoint=(first+last)//2                ##note: '//' is called a floor devision operator--> it rounds to the nearest whole number
        if  list[midpoint]==target:
            return midpoint
        elif list[midpoint]<target:
            first=  midpoint+1   
        else:
            last= midpoint-1

    return None
def verify(index):
    if index is not None:
        print("target found at index: ",index)
    else:
            print("target not found in list")


numbers=[1,2,3,4,5,6,7,8,9,10]


result=binary_search(numbers, 12)
verify(result) 
"""هنا انتا متوقع انك متلاقيش التارجت عشان التارجت 12 ونتا اخرك 10 """
##expected output 'target not found in list'


result=binary_search(numbers, 6)
verify(result) 
"""هنا انت بتجيب موقع رقم 6 اللي هو الخامس بالنسبة للغة البرمجة """
##expected output 'target found at index:  5'


"""
1-assign values to 1st and last (L 2,3)
2-value assigned to last call to len function to get the size of the list (L 3) 
3-inside the loop we have another value assignment and a simple division (L 9)
#till now the run time is constant
4-then we read a value from the list and comparing the midpoint to the target (L 12)
5-by redefining 1st and last we tell python to run the operation as many times as it needs to get the target 
6-after every loop the set becomes smaller (logarthmic run time )
"""



