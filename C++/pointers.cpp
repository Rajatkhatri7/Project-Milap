/*

Pointers points to memory location


*/


#include <iostream>
using namespace std;

int main(){

   int card = 40;
   int my_card = card;


   int *mypointer;
   mypointer = &card; //memory addr where card is stored

   my_card = *mypointer; //pointer deref.

   // pointer derefer: take the value at this memory address and assigning to variable 

    int *my2ndpointer;
    my2ndpointer = & my_card;



   printf("value of my_card is : %d\n" , my_card); //%d , %p etc are called format specifier
   printf("address of card is : %p \n" , mypointer);
   printf("value of my_card is : %d\n",my_card);
   printf("address of my_card is : %p\n",my2ndpointer);

 // my_card copies the value from card and assign it to a different memory location





    return 0;





}