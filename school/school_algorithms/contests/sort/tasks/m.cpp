#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

bool comp(string a, string b) {
    int len = min(a.size(), b.size());

    for (int i = 0; i < len; i++) {
        if (a[i] == b[i]) {
            continue;
        } else {
            return (a[i] > b[i]);
        }
    }

    return (a.size() < b.size());
}

bool comp2(string a, string b) {
    string s1 = a + b;
    string s2 = b + a;

    return (s1 > s2);
}

int main() {
    ios_base::sync_with_stdio(0);
    freopen("number.out", "wt", stdout);
    freopen("number.in", "rt", stdin);
    cin.tie(nullptr);

    string s;
    vector<string> vec;

    while (cin >> s) {
        vec.push_back(s);
    }

    sort(vec.begin(), vec.end(), comp2);

    for (size_t i = 0; i < vec.size(); i++) {
        cout << vec[i];
    }
}

