#include<iostream>
#include<string>
#include<vector>
#include<map>

using namespace std;

int main() {
    int n = 0;
    vector<int> vec;
    map<int, int> myMap;
    map<int, int>::iterator it;

    cin >> n;

    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        vec.push_back(a);

        it = myMap.find(a);
        if (it != myMap.end()) {
            myMap[a]++;
        } else { myMap[a] = 1; }
    }

    for (map<int, int>::iterator iter = myMap.begin(); iter != myMap.end(); ++iter) {
        int k = iter->first;
        int v = iter->second;

        for (int i = 0; i < v; i++) {
            cout << k << " ";
        }

        // int k = iter->first;
        // cout << iter->first << " " << iter->second << "\n";
    }
    cout << "\n";
}

