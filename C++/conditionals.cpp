/*

ternary operator
if-else
if-elseif-else
while
do-while
Switch

*/


#include <iostream>
using namespace std;

int main(){

    int rating = 5;

    rating==5? cout<<"its best \n":cout<<"its not best\n";  //ternary

    if (rating==5){

        cout<<"its best";
    }
    else if(rating==4){

        cout<<"its quite goood"<<endl;
    }
    else{

        cout<<"dont go for it its bad";
    } 

    /*
    if (0 or null){

        body
    }

    body will never be executed becoz compile true as 1 and false as 0  and if false in condition body never executed
    
    */



   return 0;


}
