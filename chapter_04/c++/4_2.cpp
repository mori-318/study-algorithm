#include <iostream>
#include <vector>

using namespace std;

vector<int> memo;

int compute_tribonacci(int N){
    if (memo[N] != -1) return memo[N];
    if (N == 0 || N == 1){
        memo[N] = 0;
        return memo[N];
    }
    if (N == 2){
        memo[N] = 1;
        return memo[N];
    }
    memo[N] = compute_tribonacci(N-1) + compute_tribonacci(N-2) + compute_tribonacci(N-3);
    return memo[N];
}

int main(){
    int N;
    cout << "N : ";
    cin >> N;
    memo.assign(N+1, -1);  // メモの初期化

    cout << "The answer is " << compute_tribonacci(N) << endl;
}