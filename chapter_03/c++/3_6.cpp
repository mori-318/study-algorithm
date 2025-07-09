#include<string>
#include<iostream>

using namespace std;

int main(){
    int K = 10, N = 8;

    int count = 0;

    for (int x=0; x<K; x++){
        for (int y=0; y<K; y++){
            int z = N - x - y;
            if (z >= 0 && z <= K) count ++;
        }
    }

    cout << "count : " << count << endl;

    /*
    計算量は0(N)
    */
}