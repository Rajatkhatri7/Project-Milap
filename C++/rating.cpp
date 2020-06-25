#include <iostream>
#include <string>
using namespace std;



int main(){

    int rating;
    string my_str;
//cout<<"Please rate our services from 1 to 5 \n";

    

    while(rating>5){
        cout<<"please enter value between 1 and 5\n";
        cin>>rating;
    

   
        if(rating==5){
            cout<<"Thanks for giving us 5 star\n";
        }
        else if (rating==4){


            cout<<"thankyou we will improve next time \n ";

        }
        else{
            cout<<"Please mentiion Your issues: ";
            getline(cin,my_str);
            cout<<my_str<<endl;
            
        }

}




return 0;

}