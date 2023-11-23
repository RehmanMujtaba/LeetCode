class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {    
        // for(int i=0; i < nums.size(); i++) {
        //     int theNum = nums[i];
        //         for(int j = i + 1; j < nums.size(); j++ ) {
        //             if (nums[j] == theNum) {
        //                 return true;
        //             }
        //         }
        // }
        // return false;
        unordered_map<int, int> map;

        for(int i = 0; i < nums.size(); i++) {
            if (map.find(nums[i]) == map.end()) {
                map[nums[i]] = 1;
            } else {
                return true;
            }
        }
        return false;
    }
};