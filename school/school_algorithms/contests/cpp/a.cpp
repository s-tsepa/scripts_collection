#include <utility>
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <set>

using namespace std;

int main() {
    multiset<int> a;
    int n; int k;

    vector<int> arr;

    cin >> n >> k;
    k += 1;

    for (int i = 0; i <= n; ++i) {
        int in = 0;
        if (i < n) {
            cin >> in;
        }
        if (i + 1 >= k) {
            cout << *a.begin() << " ";
            a.erase(a.find(arr[i - k + 1]));
            a.insert(in);
            arr.push_back(in);
        } else {
            a.insert(in);
            arr.push_back(in);
        }
    }
}
