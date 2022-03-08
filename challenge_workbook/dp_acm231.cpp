#include<iostream>
#include<cstring>
using namespace std;

int n = 4, W = 5;
int w[100] = {2, 1, 3, 2}, v[100] = {3,2,4,2};


int dp[5][6]; 
int rec(int i, int j){
    if (dp[i][j] >=0){
        return dp[i][j];
    }
    int res;
    if (i == n){
        res = 0 ;
    }
    else if(j < w[i]){
        res = rec(i+1, j);
    }else{
        res = max(rec(i+1,j), rec(i+1, j-w[i])+v[i]);
    }
    dp[i][j] = res;
    return res;
}
void solve(){
    memset(dp, -1, sizeof(dp));
    rec(0,W);
    //printf("%d",rec(0,W));
    for (int i = 0; i < 5;i ++){
        for (int j = 0; j < 6; j ++)
        cout << dp[i][j] << " ";
    }
}
int main(){
    solve();
    return 0;
}