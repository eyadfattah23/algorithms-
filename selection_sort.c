#include<stdio.h>





void swap(int* num1,int* num2){        

int tmp = *num1;
*num1 = *num2;
*num2 = tmp;
}






///// the key is in making 2 loops for selecting and swaping 
void select_sort(int array[], int number){
    //arg1 is the array we wanna sort 
    //arg2 is the size of the array
//0  1  2  3  4  5 
//60 40 50 30 10 20



int index_of_min;

for (int i = 0; i < number; i++)        //you can replace number with number-1 cus u dont need to check the last element
{
    index_of_min = i;   // the min is controlled by i
                        //the 1st loop be like array[0] = array [min] for now till sth happens 

    for (int j = i+1; j < number; j++)      //i+1 bec we dont need to check the 1st element again
    
        if(array[j] < array[index_of_min])       // array[j] refers to all the elements you're gonna select to compare them with array[index_of _min] 
            index_of_min =j;
            swap(&array[index_of_min], &array[i]);
 
        
}



}




void print(int arr[],int size){

    for (int i = 0; i < size; i++)
    {
    printf("%d ",arr[i]);
    }
    
}



int main(void){

    int numbers[]={60,40,50,30,10,20};
    int n=sizeof(numbers)/sizeof(numbers[0]);
    select_sort(numbers,n);

    printf("new array: \n");
    print(numbers,n);

}

