#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ull> vull;
typedef vector<ll> vll;

#define FOR(i,a,b) for (int i = a; i <= b; ++i)
#define FORDOWN(i,a,b) for(int i = a; i >= b; --i)
#define pb(x) push_back(x)
#define all(a) (a).begin(),(a).end()

vector<vi> arr;

int main() {
    int n, m;
    cin >> n >> m;
    arr.resize(n);
    for (int i = 0; i < n; i++) {
        arr[i].resize(3);
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
    }
    for (int q = 0; q < m; q++) {
        int x;
        cin >> x;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (x >= arr[i][0] && x <= arr[i][1]) {
                if ((x - arr[i][0]) % 2 == 0)
                    ans += arr[i][2];
                else
                    ans -= arr[i][2];
            }
        }
        cout << ans << "\n";
    }
    cout << "\n\n\n";
    return 0;
}