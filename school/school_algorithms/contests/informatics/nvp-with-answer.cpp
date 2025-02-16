#include <algorithm>

using namespace std;

int main() {

    unsigned int n;
    cin >> n;

    vector<int> a;
    a.reserve(n);

    for (int k = 0; k < n; ++k) {
        cin >> a[k];
    }

    int d[1000], p[1000];

    for (int i = 0; i < n; ++i) {
        d[i] = 1;
        p[i] = -1;
        for (int j = 0; j < i; ++j)
            if (a[j] < a[i])
                if (1 + d[j] > d[i]) {
                    d[i] = 1 + d[j];
                    p[i] = j;
                }
    }

    int ans = d[0],  pos = 0;
    for (int i = 0; i < n; ++i)
        if (d[i] > ans) {
            ans = d[i];
            pos = i;
        }

    vector<int> path;
    while (pos != -1) {
        path.push_back (pos);
        pos = p[pos];
    }
    reverse (path.begin(), path.end());
    for (int i : path)
        cout << a[i] << ' ';
}
