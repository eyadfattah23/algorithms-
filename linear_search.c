#include<stdio.h>
#include"cs50.h"
#include<string.h>
int linear_search(int list[],int target){
    int len =(sizeof(list)/sizeof(list[0]));
    for (int i = 0; i <len ; i++)
    {
        if (list[i]==target)
        {
            printf("target found after %i steps = %i\n",i+1,target);
            return target;

        }
    }
        
    printf("target not found\n");
    return 0;
}


///linear search for strings 

int strings_linear_search(string names_list[],string target){
for (int s = 0; s < (sizeof(names_list)/sizeof(names_list[0])); s++)
{
    if (strcmp(names_list[s],target)==0)        //هنا لو الاسمين بيساووا بعض الفنكشن هترجع صفر 
    {
        printf("target found in %i steps = %s \n",s+1,target);
        return 0;
    }
    
}
printf("target not found");
return 1;

}


int main(void){
int numbers[7];     //لازم تكتب عدد عناصر الارراي لو  هتعمل ديكليريشن بس من غير العناصر 
numbers[0]=4;
numbers[1]=6;
numbers[2]=8;

int array[] = {1,2,3,4,5,6};        //هنا محددتش العدد 
linear_search(array,6);


string names[]={"ahmed","gamal","eyad","mazen","ali","mai","mariam","sara"};
/*
if you wanna compare 2 strings use <string.h> lib which contain 'strcmp' func. that compares strings 
*/
strings_linear_search(names,"sara");



}