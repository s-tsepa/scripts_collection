#include<iostream>
#include<vector>
#include<functional>
#include<algorithm>
#include<iterator>

using namespace std;

void swap(vector<int>& v, int x, int y);

void quicksort(vector<int> &vec, int L, int R) {
    int i, j, mid, piv;
    i = L;
    j = R;
    mid = L + (R - L) / 2;
    piv = vec[mid];

    while (i < R || j > L) {
        while (vec[i] < piv)
            i++;

        while (vec[j] > piv)
            j--;

        if (i <= j) {
            swap(vec, i, j);
            i++;
            j--;
        } else {
            if (i < R)
                quicksort(vec, i, R);
            if (j > L)
                quicksort(vec, L, j);
            return;
        }
    }
}

void swap(vector<int>& v, int x, int y) {
    int temp = v[x];
    v[x] = v[y];
    v[y] = temp;
}

int main() {
    int n; cin >> n;
    vector<int> vec1;

    for (int i = 0; i < n; i++) {
        int aa; cin >> aa;
        vec1.push_back(aa);
    }
    quicksort(vec1, 0, n - 1);
    for (int i = 0; i < n; i++) {
        cout << vec1[i] << " ";
    }
}
