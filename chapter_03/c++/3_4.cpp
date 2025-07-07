#include <string>
#include <vector>
#include <iostream>
#include <climits>

using namespace std;

int main() {
    vector<int> list_a = {21, 11, 35, 64, 23, 56, 124, 23, 12};

    int lowest = INT_MAX;
    int highest = 0;

    for (int i=0; i<list_a.size(); i++) {
        if (list_a[i] < lowest) lowest = list_a[i];
        else if (list_a[i] > highest) highest = list_a[i];
    }

    int max_diff = highest -lowest;
    cout << "max_diff : " << max_diff << endl;
    /*
    計算量はO(N)
    */
}