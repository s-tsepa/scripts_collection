#include <utility>
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <queue>
#include <deque>
#include <set>

using namespace std;

void test(deque<int> q1, deque<int> q2) {
    deque<int>::iterator it = q1.begin();
        while (it != q1.end()) {
            std::cout << ' ' << *it++;
        }
        cout << " ^ ";
        deque<int>::iterator it2 = q2.begin();
        while (it2 != q2.end()) {
            std::cout << ' ' << *it2++;
        }
        cout << "\n";
}

void check(deque<int> &q1, deque<int> &q2) {
    if (q1.size() < q2.size()) {
        q1.push_back(q2.front());
        q2.pop_front();
    }
    if (q1.size() - q2.size() > 1) {
        q2.push_front(q1.back());
        q1.pop_back();
    }
}

int main() {
    deque<int> q1;
    deque<int> q2;

    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        char a; int x;
        cin >> a;

        if (a == '-') {
            cout << q1.front() << "\n"; q1.pop_front();
            check(q1, q2);
            continue;
        }

        cin >> x;

        if (a == '+') {
            q2.push_back(x);
        } else {
            q1.push_back(x);
        }

        // test(q1, q2);
        check(q1, q2);
        // test(q1, q2);
    }
}
