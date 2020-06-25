#include <iostream>
using namespace std;

int main(){

    int intger_array[4] = {1,2,3,4};
    cout<<"address of integer_array"<< intger_array<<endl; // output memory address of starting element of array


    int another_array[4] ;
    another_array[0] = 10;
    another_array[1] = 15;

    cout<<"prev value at oth position "<< another_array[0]<<endl;


    *another_array = 29; // as another_array points to starting address of 0th element so, we can change the starting value by this way also
    cout<< "new value at 0th position "<<another_array[0]<<endl;
    cout<<"address of another_array "<<another_array<<endl;


    int *pointer = another_array; // pointing where another_array is pointing i.e at 0th position 
    cout<<"address which pointer is pointing "<<pointer<<endl;
    pointer++; 
    cout<<"new address to which pointer is now pointing "<<pointer<<endl;

    /*
    conclusion: pointer++ or pointer+=1 increment the address 
                Previously pointer pointing to 0th position of array 
                but after incremending it points to 1th position

                for integer address increment by 4
                for char it is 
    */

   *pointer = 25;
   cout<<"new value at 1t position of another_array: "<<another_array[1];


    return  0 ;


}