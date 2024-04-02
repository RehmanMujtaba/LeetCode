class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map_t, t_map_s = {}, {}

        for i in range(len(s)):
            s_map_t[s[i]] = s_map_t.get(s[i], t[i])
            t_map_s[t[i]] = t_map_s.get(t[i], s[i])

            if s_map_t[s[i]] != t[i] or t_map_s[t[i]] != s[i]:
                return False

        return True