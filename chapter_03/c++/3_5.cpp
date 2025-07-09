#include<string>
#include<vector>
#include<iostream>
#include<climits>

using namespace std;

int main(){
    vector<int> list_a = {8, 12, 16};

    int count = INT_MAX;

    // 全ての要素が偶数か判定
    bool are_all_even = true;
    for (int i=0; i<list_a.size(); i++){
        if (list_a[i] % 2 != 0){
            are_all_even = false;
            break;
        }
    }

    // 何回割り算が行えるかの最小値を計算
    for (int i=0; i<list_a.size(); i++){
        int a = list_a[i];
        int temp_count = 0;
        while (true){
            if (a % 2 == 0){
                a = a / 2;
                temp_count ++;
            }
            else break;
        }

        // temp_countがcountより小さければcountを更新
        if (temp_count < count){
            count = temp_count;
        }
    }

    cout << "minimum count : " << count << endl;
}