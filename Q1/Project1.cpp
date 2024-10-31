#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Contact{
    private:
    string name;
    string email;
    string phone;
    public:
    Contact (string n,string e,string p){
    name = n; 
    email=e;
    phone=p;
    }
    void print(){
        cout<<name<<endl;
        cout<<email<<endl;
        cout<<phone<<endl;
    }
    

};
/*Todo: 
learn how to delete user data
use vector it not an array 
 */ 



int main()
{
    vector<Contact>contacts;
    while (true){
        int choice = 0;
        cout<<"enter an Option: 1. enter contact 2. delete contact  3. veiw list 4. exit"<<endl;
        cin>>choice;
        if (choice ==1){
            string name; 
            string email;
            string phone;
            cout<<"enter name "<<endl;
            cin >> name;
            cout<< "enter email"<<endl;
            cin>> email;
            cout <<"Enter Phone " <<endl;
            cin>>phone;

            Contact person =  Contact(name, email, phone);
            contacts.push_back(person);

        }
        else if (choice ==2){
            // remove person by index   use contact vector 

        }
        else if (choice ==3){
            /* print out contacts 
            use the contact vector
            */
           cout<<

        }
        else{
            return 0;
        }
    }
}