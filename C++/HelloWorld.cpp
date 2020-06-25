#include <iostream>
#include <vector>
#include <string>
#include <cmath>
//check the docs to see the available functions in cmath

using namespace std;

int main()
{
    vector<string> msg{"hello ","C++ ","world ","its ", "rajat " , "here"};
    string firname = "ram";
    string lastname = " sinha";

    string fullname = firname.append(lastname);
    cout<<fullname<<"\n";
    cout<<"lengt of full name is "<<fullname.length()<<"\n";

    // can use size() as alise of leangth()

    cout<<"Accessing the words in the string: "<<fullname[6]<<"\n";


    string nickName;
    cout << "Type your nick name with sirname also: ";
    getline(cin,nickName);      //to get the full line if we use cinn and type fullname than it will output only firstname not fullname
    cout << "Your nick name is: " << nickName<<"\n";  //watch the output carefully

    

      if (fullname.length()>10)
        {
            cout<<"your name is so lenghty "<<"\n";

        }
        else{
            cout<<"your name length is : "<<fullname.length()<<endl;
        }

    for (const string & word :msg)
    {
        cout<<word<<"";
      

  
    }
    cout<<endl;




}

