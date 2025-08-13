#include <iostream>

using namespace std;

int count = 0;

void func(long long K, long long current_num, int use){
    if (current_num > K) return;
    if (use == 0b111) count++;

    func(K, current_num * 10 + 3, use | 0b001);
    func(K, current_num * 10 + 5, use | 0b010);
    func(K, current_num * 10 + 7, use | 0b100);
}

int main() {
    long long K;
    cin >> K;
    func(K, 0, 0);
    cout << count << endl;
}