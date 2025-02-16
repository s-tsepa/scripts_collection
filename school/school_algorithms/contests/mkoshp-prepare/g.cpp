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

vi arr;

bool f(int n, int m) {
    ll kr = arr[m + 1];
    ll free = 0;
    for (int i = 0; i <= m; i++)
        free += arr[i];
    ll n_free = 0;
    for (int i = m + 2; i < n; i++)
        n_free += kr - arr[i];
    return free >= n_free;
}

int main() {
    int n;
    cin >> n;
    arr.resize(n);
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    sort(arr.rbegin(), arr.rend());
    if (arr[0] == arr[n - 1]) {
        cout << 0;
        return 0;
    }
    int l = -1, r = n - 1;
    while (r - l != 1) {
        int mid = (l + r) / 2;
        if (f(n, mid))
            r = mid;
        else
            l = mid;
    }
    cout << r + 1;
    return 0;
}