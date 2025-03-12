#include <iostream>
#include <vector>    //imports needed for the progam to work and makes life easir
#include <string>

using namespace std;   // makes it so i dont have to use "std::"

class Contact{
    private:
    string name;  // declaring varibles 
    string email;
    string phone;
    public:
    Contact (string n,string e,string p){  // this will be used for later as to strore info Maybe
    name = n; 
    email=e;
    phone=p;
    }
    void print(){
        cout<<"Name: "<<name<<endl;      // used insted of get name getemail and get phone
        cout<<"Email: "<<email<<endl;
        cout<<"Phone: "<<phone<<endl;
    }
    

};
/*Todo: 
learn how to delete user data
use vector it not an array 
 */ 


void showContacts(vector<Contact>contacts){
    int count=1;
    for(Contact p: contacts){ 
        cout<<count<<" ";
        count++;
        p.print();
    }
}
int main()
{
    vector<Contact>contacts; // this is lists in other languages and is simmular to arrays
    while (true){
        int choice = 0;  // a varible that is later used for an if staytment
        cout<<"Enter Option: 1. Create New Contact  2. Delete Contact  3. Veiw Contact List 4.Exit"<<endl; // this is the user menue 
        cin>>choice;   //takes input from the menue and asign
        if (choice ==1){
            string name; 
            string email;       // just varibles
            string phone;
            cout<<"Enter Name: "<<endl;
            cin >> name;
            cout<< "Enter Email: "<<endl;    //user input 
            cin>> email;
            cout <<"Enter Phone: " <<endl;
            cin>>phone;

            Contact person =  Contact(name, email, phone);   // creates an varible that is used to put info in the class created later
            contacts.push_back(person);  // simmular to apend Maybe??

        }
        else if (choice ==2){
            // remove person by index   use contact vector 
            int index;
            showContacts(contacts); // displays the contents of the vector
            cout<<"Enter number contact remove: ";  //promts the user for a number wich is the index of the of the vector
            cin>>index;
            contacts.erase(contacts.begin()+index-1); // goes to the contact vector (.erase) is how to remove it from the vector
        }
        else if (choice ==3){
            /* print out contacts 
            use the contact vector
            */
           showContacts(contacts); // this insainly helpful code is used to show the information stored in the contacts vector


        }
        else{
            return 0;
        }
    }
}