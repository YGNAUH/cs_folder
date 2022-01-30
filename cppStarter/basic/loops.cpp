#include<iostream>
using namespace std;
int main(){
    int i = 5;
    int x = 10;
    //while loop
    while((x<2) || (x>5))
    {
        x--;
    }
    //for loop
    for (i; i<10; i++){
        x++;
    }
    char grade;
    //switch
    switch (grade)
    {
    case 'A':
        cout << "great" << endl;
        break;
    case 'B':
    case 'C':
        cout << "good" << endl;
        
    default:
        cout << "no res" << endl;
    }
}