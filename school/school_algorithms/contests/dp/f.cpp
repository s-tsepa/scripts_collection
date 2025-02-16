#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

template <typename T1>
ostream& operator<<(ostream& out, vector<T1> a) {
    for (int i = 0; i < a.size(); ++i) {
        cout << a[i] << " ";
    }
    cout << "\n";
    return out;
}

int main() {
    int n; cin >> n;
    vector<int> v(1, 0);
    for (int i = 0; i < n; i++) {
        int aa; cin >> aa;
        v.push_back(aa);
    }

    vector<int> dp(101, 1e4 + 1);
    sort(v.begin(), v.end());

    dp[2] = v[2] - v[1];
    dp[3] = v[3] - v[1];


    for (int i = 4; i <= n; i++)
        dp[i] = min(dp[i - 1], dp[i - 2]) + v[i] - v[i - 1];

    cout << dp[n];
}
