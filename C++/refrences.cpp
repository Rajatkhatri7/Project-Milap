#include <iostream>
using namespace std;

int main(){

    int score;
    score  =  200;

    int *mypointer = &score;



    printf("value of score is : %d\n", score);
    printf("address of score is : %p\n", mypointer);

    /*
    
    refer to a memory address 
    
    */

    int &another = score;
    another  =  800;

    // another is a reference to the score so if we chage the value of any one of these two vareible , value of another variable is also changed
    // another -> score -> 800
    

    printf("value of score is : %d\n", score);
    printf("address of score is : %p\n", mypointer);









    return 0 ;

}