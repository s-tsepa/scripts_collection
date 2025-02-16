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
    int n, m;
    cin >> n;
    vector<int> a, b;
    for (int _ = 0; _ < n; _++) {
        int aa; cin >> aa;
        a.push_back(aa);
    }
    cin >> m;
    for (int _ = 0; _ < m; _++) {
        int aa; cin >> aa;
        b.push_back(aa);
    }

//    cout << a << '\n';
//    cout << b << '\n';

    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
//            cout << a[i - 1] << " " << b[j - 1] << '\n';
            if (a[i - 1] == b[j - 1])
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);
        }
    }
    int maxx = 0;

    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            if (dp[i][j] > maxx)
                maxx = dp[i][j];
        }
    }

//    cout << dp;
    cout << maxx;
}
