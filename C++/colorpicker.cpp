#include <iostream>
#include <string>

using namespace std;

int main(){

    string myColor;
    string firname;
    string lastname;

    cout<<"Enetr your fav color: ";
    getline(cin , myColor); //storing the entire line into variable
    cout<<"HY "<<myColor<<" is my fav too."<<endl;

    cout<<"Hey what's your first name? \n";
    getline(cin,firname);
    cout<<"and your lastname also please \n";
    getline(cin,lastname);
    cout<<"Nice to meet you "<<firname<<" "<<lastname<<endl;
    



    return 0;
}