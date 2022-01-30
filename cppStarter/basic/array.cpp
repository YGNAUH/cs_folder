#include<iostream>
using namespace std;
int main(){
    int n[1]; // = {};
    n[0] = 1;
    cout << n[0] << endl;
    for (int i=0; i<1; i++){
        n[i] = 5;
        cout << n[i] << endl;
    }
    return 0;
}