#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;


bool comp(const pair<int, int>& a, const pair<int, int>& b) {
    if (a.second > b.second) {
        return true;
    } else {
        if (a.second != b.second) {
            return false;
        } else {
            if (a.first < b.first) {
                return true;
            } else { return false; }
        }
    }
}


int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> vec;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        vec.push_back(pair<int, int>(a, b));
    }

    sort(vec.begin(), vec.end(), comp);

    for (int i = 0; i < n; i++) {
        cout << vec[i].first << " " << vec[i].second << "\n";
    }
}
