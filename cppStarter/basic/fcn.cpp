#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int i1 = 15;
    int i2 = 16;
    int res;
    res = max(i1,i2);
    cout << "square root" << sqrt(res) << endl;
    cout << "squrare" << pow(res,2) << endl;
}
int max(int i1, int i2){
    int result;
    if (i1 > i2)
        result = i1;
    else
        result = i2;
    return result;
}