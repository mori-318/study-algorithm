#include <iostream>

using namespace std;

int main() {
    int target_num = 23;
    int list_a[] = {1, 23, 542, 656, 88, 4, 3, 6, 4, 33, 32, 23};

    int max_idx = 0;
    for (int i = 0; i < sizeof(list_a) / sizeof(list_a[0]); i++) {
        if (list_a[i] == target_num) {
            max_idx = i;
        }
    }
    cout <<"最大のインデックスは、" << max_idx << endl;
}