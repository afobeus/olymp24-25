#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    while (n--) {
        long long v1, k1, r1, v2, k2, r2, t;
        cin >> v1 >> k1 >> r1 >> v2 >> k2 >> r2 >> t;
        long long vasya_dist = v1 * k1 * (t / (k1 + r1)) + v1 * min(k1, (t % (k1 + r1)));
        long long petya_dist = v2 * k2 * (t / (k2 + r2)) + v2 * min(k2, (t % (k2 + r2)));
        if (vasya_dist > petya_dist)
            cout << "V\n";
        else if (petya_dist > vasya_dist)
            cout << "P\n";
        else
            cout << "D\n";
    }

    return 0;
}
