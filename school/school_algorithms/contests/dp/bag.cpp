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
    freopen("knapsack.in", "r", stdin);
    freopen("knapsack.out", "w", stdout);

    int s, n; cin >> s >> n;
    vector<int> v(1, 0);
    vector<vector<int>> dp(n + 1, vector<int>(s + 1, false));
    for (int i = 0; i < n; i++) {
        int aa; cin >> aa;
        v.push_back(aa);
    }

    dp[0][0] = true;

    for (int i = 1; i < n + 1; i++) {
        for (int j = 0; j < s + 1; j++) {
            dp[i][j] = dp[i - 1][j];
            if (v[i] <= j) {
                dp[i][j] = (dp[i][j] | dp[i - 1][j - v[i]]);
            }
        }
    }

    int maxx = 0;

    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= s; j++) {
            if (dp[i][j])
                maxx = j;
        }
    }

    cout << maxx;
}
