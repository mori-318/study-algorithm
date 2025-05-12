#include <string>
#include <iostream>
#include <vector>

using namespace std;
int main() {
    int target_num = 23;
    vector<int> list_a = {1, 23, 542, 656, 88, 4, 3, 6, 4, 33, 32, 23};

    int target_count = 0;

    for (int i=0; i<list_a.size(); i++){
        if (list_a[i] == target_num) target_count ++;
    }

    cout << "count：" << target_count << endl;
    /*
    計算量は、O(N)
    */
}

