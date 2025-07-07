#include <string>
#include <vector>
#include <iostream>
#include <climits>

using namespace std;

int main(){
    vector<int> list_a = {21, 11, 35, 64, 23, 56, 124, 23, 12};

    int lower_1 = INT_MAX;
    int lower_2 = INT_MAX;

    for (int i=0; i<list_a.size(); i++){
        if (list_a[i] < lower_1) lower_1 = list_a[i];
        else if (list_a[i] < lower_2) lower_2 = list_a[i];
    }

    cout << "2nd lower num : " << lower_2 << endl;
    /*
    計算量は、O(N)
    */
}