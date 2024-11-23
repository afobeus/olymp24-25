#include <iostream>
#include <string>
#include <vector>
#include <cstdint>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<int> letters_count('z' - 'a' + 1);
    for (int i = 0; i < n; ++i)
        ++letters_count[s[i] - 'a'];

    string full;
    for (char i = 'a'; i <= 'z'; ++i) {
        if (letters_count[i - 'a'])
            full += i;
    }
    for (int i = 0; i < full.size(); ++i)
        --letters_count[s[i] - 'a'];

    int result = INT32_MAX;
    for (int i = (int) full.size(); i < n; ++i) {
        bool enough_letters = true;
        int count_operations = 0;
        vector<int> letters_copy = letters_count;
        for (int j = 0; j < full.size(); ++j) {
            if (s[i - full.size() + j] != full[j]) {
                ++count_operations;
                if (--letters_copy[full[j] - 'a'] < 0) {
                    enough_letters = false;
                    break;
                }
            }
        }
        if (enough_letters)
            result = min(result, count_operations);
    }

    if (result == INT32_MAX)
        cout << -1;
    else
        cout << result;

    return 0;
}
