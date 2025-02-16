#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> bfs(int s, int t, vector<vector<int >> adj, int n) {
    vector<int> dist(n, n);

    vector<int> p(n, -1);

    dist[s] = 0;
    queue<int> q;
    q.push(s);

    while (!q.empty()) {
        int v = q.front();
        q.pop();

        for(int i = 0; i < n; ++i) {
            if (adj[v][i] == 1) {

                int u = i;

                if (dist[u] > dist[v] + 1) {
                    p[u] = v;

                    dist[u] = dist[v] + 1;
                    q.push(u);
                }
            }
        }
    }

    if (dist[t] == n) {
        return {};
    }

    vector<int> path;
    while (t != -1) {
        path.push_back(t);
        t = p[t];
    }

    reverse(path.begin(), path.end());
    return path;
}


int main() {

    int n, s, t;
    cin >> n;

    vector<vector<int>> matrix;

    for (int i = 0; i < n; ++i) {
        matrix.emplace_back(n, 0);
        for (int j = 0; j < n; ++j) {
            cin >> matrix[i][j];
        }
    }

    cin >> s >> t;

    s--;
    t--;

    if (s == t) {
        cout << 0;
        return 0;
    }

    vector<int> path = bfs(s, t, matrix, n);

    if (path.empty()) {
        cout << -1;
        return 0;
    }

    cout << path.size() - 1 << endl;

    for( auto c: path) {
        cout << c + 1 << " ";
    }

    return 0;
}
