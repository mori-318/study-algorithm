#include <string>
#include <iostream>
#include <vector>

using namespace std;

int main(){
    string S = "125";

    int N = S.size();

    int sum = 0;

    // ２進数で１のところに＋を入れる
    for (int bit = 0; bit < (1 << N-1); bit++){
        int tmp = 0;
        for (int i = 0; i < N-1; i++){
            tmp = tmp * 10 + int(S[i] - '0');

            // +を挿入する位置かどうか確認
            if (bit & (1 << i)){
                sum += tmp;
                tmp = 0;
            }
        }

        //最後の部分を加算
        tmp = tmp * 10 + int(S[N - 1] - '0');
        sum += tmp;
    }

    cout << "sum : " << sum << endl;
}