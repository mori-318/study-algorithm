#include <iostream>

using namespace std;

int compute_tribonacci(int N){
    if (N==0 || N==1) return 0;
    else if (N==2) return 1;
    else return compute_tribonacci(N-1) + compute_tribonacci(N-2) + compute_tribonacci(N-3);
}

int main(){
    int N;
    cout << "N : ";
    cin >> N;
    cout << "tribonacci value N is " << compute_tribonacci(N) << endl;
}