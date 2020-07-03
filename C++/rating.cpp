#include <iostream>
#include<string>
using namespace std;

int main(){

    int rating;
    string feedback;
    cout<<"please enter the rating\n";

    cin>>rating;
    if(rating>5 || rating<1){
        cout<<"please enter the correct rating: \n";
    }

   
    else if(rating==5){

        cout<<"Thankyou so much"<<endl;
    }
    else if(rating==4){
        cout<<"thnx we will inprove later \n";
    }
    else if (rating<4){
        cout<<"plesae mention the issues you faced: ";
        getline(cin,feedback);
        cout<<feedback;
    }



    return 0;


}