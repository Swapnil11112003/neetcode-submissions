class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
        {
            return false;
        }

         unordered_map<char, int> count;

        // Increment count for characters in `s` and decrement for `t`
        for (int i = 0; i < s.length(); i++) {
            count[s[i]]++;
            count[t[i]]--;
        }

        // Check if all counts are zero
        for (auto entry : count) {
            if (entry.second != 0) {
                return false;
            }
        }

        return true;
    }
};
