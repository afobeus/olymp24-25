#include <iostream>
#include <vector>
#include <cstdint>

using namespace std;

vector<int> numbers;
vector<pair<int, int>> seg_tree;

pair<int, int> recalculate(pair<int, int> left, pair<int, int> right) {
    if (left.second == right.second)
        return make_pair(min(left.first, right.first),
                         left.second);
    else if (left.second > right.second)
        return left;
    else
        return right;
}

void build(int l, int r, int v) {
    if (l + 1 == r) {
        seg_tree[v] = make_pair(l, numbers[l]);
        return;
    }
    int m = (l + r) / 2;
    build(l, m, 2 * v);
    build(m, r, 2 * v + 1);
    seg_tree[v] = recalculate(seg_tree[2 * v], seg_tree[2 * v + 1]);
}

pair<int, int> get_points(int v, int l, int r, int get_l, int get_r) {
    if (l >= get_r || r <= get_l)
        return {-1, INT32_MIN};
    if (get_l <= l && r <= get_r)
        return seg_tree[v];
    int m = (l + r) / 2;
    return recalculate(get_points(2 * v, l, m, get_l, get_r),
                       get_points(2 * v + 1, m, r, get_l, get_r));
}

void change(int v, int l, int r, int x, int y) {
    if (r <= x || x < l)
        return;
    if (l + 1 == r and l == x) {
        seg_tree[v] = make_pair(x, y);
        return;
    }
    int m = (l + r) / 2;
    change(2 * v, l, m, x, y);
    change(2 * v + 1, m, r, x, y);
    seg_tree[v] = recalculate(seg_tree[2 * v], seg_tree[2 * v + 1]);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n;
    numbers.resize(n);
    for (int i = 0; i < n; ++i)
        cin >> numbers[i];
    seg_tree.resize(4 * n);
    build(0, n, 1);

    long long answer = 0;
    cin >> q;
    int type, num1, num2;
    for (int i = 0; i < q; ++i) {
        cin >> type >> num1 >> num2;
        if (type == 1) {
            pair<int, int> points = get_points(1, 0, n, num1, num2 + 1);
            answer += points.first + points.second;
        } else
            change(1, 0, n, num1, num2);
    }

    cout << answer;


    return 0;
}