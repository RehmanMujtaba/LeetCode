class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        unordered_map<int,int> map;

       for (vector<int>::iterator it = nums.begin(); it != nums.end(); ++it) {
        if (map.find(*it) == map.end()) {
            map[*it] = 0;
        } else {
            int num = map[*it];
            map[*it] = num + 1;
            if (num > nums.size()/2 + 1) break;
        }
    }
        int max = 0;
        int element;

        for (auto i : map) {
            if (i.second >= max)  {
                max  = i.second; 
                element = i.first;
            }
        }
        return element;
    }
};