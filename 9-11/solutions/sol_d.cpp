#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<int>> allowed_before(10,
                                       vector<int> (10) = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9});
    int num;
    for (int i = 0; i < m; ++i) {
        cin >> num;
        auto num_pos = allowed_before[num % 10].begin();
        while (*num_pos != num / 10)
            ++num_pos;
        allowed_before[num % 10].erase(num_pos);
    }
    vector<set<int>> prohibited_numbers(n);
    int index, x;
    for (int i = 0; i < k; ++i) {
        cin >> index >> x;
        for (int j = 0; j < x; ++j) {
            cin >> num;
            prohibited_numbers[index].insert(num);
        }
    }

    vector<vector<int>> dp(n, vector<int> (10, 0));
    for (int i = 0; i < 10; ++i)
        dp[0][i] = 1;
    for (int i : prohibited_numbers[0])
        dp[0][i] = 0;

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < 10; ++j) {
            if (prohibited_numbers[i].find(j) != prohibited_numbers[i].end())
                continue;
            for (int p : allowed_before[j]) {
                dp[i][j] += dp[i - 1][p];
            }
        }
    }

    long long result = 0;
    for (int i = 1; i < 10; ++i)
        result += dp[n - 1][i];

    cout << result;

    return 0;
}
