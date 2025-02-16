#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>


using namespace std;

int main() {
    string s1, s2;

    cin >> s1;
    cin >> s2;

    vector<char> vec1;
    vector<char> vec2;

    for (int i = 0; i < int(s1.size()); i++) { vec1.push_back(s1[i]); }
    for (int i = 0; i < int(s2.size()); i++) { vec2.push_back(s2[i]); }

    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());

    for (int i = 0; i < s1.size(); i++) {
        if (s1[i] != s2[i]) {
            cout << "NO";
            return 0;
        }
    }
    cout << "YES";
}

