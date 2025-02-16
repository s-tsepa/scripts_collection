#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

using pi = pair<int, int>;

struct pair_hash {
    template <class T1, class T2>
    std::size_t operator() (const std::pair<T1, T2> &pair) const {
        return std::hash<T1>()(pair.first * 1000) ^ std::hash<T2>()(pair.second);
    }
};

vector<pi> res(100 * 100);

size_t get_neighbours(pi cur, const vector<unordered_set<int>>& arr) {
    auto c1 = cur.first;
    auto c2 = cur.second;
    size_t i = 0;
    for (const auto& e : arr[c1]) {
        if (arr[c2].find(e) != arr[c2].end()) {
            res[i] = make_pair(c1, e);
            i++;
            res[i] = make_pair(e, c2);
            i++;
        }
    }

    for (const auto& e1 : arr[c1]) {
        for (const auto& e : arr[e1]) {
            if (e1 != c2 || e != c1) {
                if (arr[c2].find(e) != arr[c2].end()) {
                    res[i] = make_pair(e1, e);
                    i++;
                }
            }
        }
    }
    return i;
}


void bfs(pi start, pi end, const vector<unordered_set<int>>& arr, unordered_map<pi, pi, pair_hash>& store) {
    auto compare = [](pair<int, pi> lhs, pair<int, pi> rhs) {
        return lhs.first > rhs.first;
    };
    priority_queue<pair<int, pi>, std::vector<pair<int, pi>>, decltype(compare)> q(compare);

    store[start] = make_pair(1, 0);

    q.emplace(0, start);
    while (!q.empty()) {
        auto data = q.top();
        q.pop();

        if (data.second == end) {
            return;
        }
        auto cur = data.second;
        size_t s = get_neighbours(cur, arr);
        for (size_t i = 0; i < s; i++) {
            const auto& neigh = res[i];
            int step = int(neigh.first != cur.first) + int(neigh.second != cur.second);
            if (store.find(neigh) == store.end()) {
                q.emplace(store[cur].second + step, neigh);
                store.emplace(neigh, make_pair(store[cur].first + 1, store[cur].second + step));
            }

            if (store[neigh].second > store[cur].second + step) {
                store[neigh] = make_pair(store[cur].first + 1, store[cur].second + step);
            }

            if (neigh == cur) {
                q.emplace(store[cur].second + step, neigh);
            }
        }
    }
}

int main() {
    int n, m, a1, b1, a2, b2;
    cin >> n >> m >> a1 >> b1 >> a2 >> b2;
//    n = 10000; m = 9999; a1 = 1; b1 = 2; a2 = 9999; b2 = 10000;
    a1--;
    a2--;
    b1--;
    b2--;
    vector<unordered_set<int>> arr(m);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
//        a = i + 1; b = i + 2;
        a--;
        b--;
        arr[a].emplace(b);
        arr[b].emplace(a);
    }

    unordered_map<pi, pi, pair_hash> store;
    bfs(make_pair(a1, b1), make_pair(a2, b2), arr, store);

    const auto& res = store[make_pair(a2, b2)];
    cout << res.second << ' ' << res.first;

    return 0;
}
