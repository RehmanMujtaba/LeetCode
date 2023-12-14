class Solution {
public:
    int search(vector<int>& nums, int target) {

      int   l = 0;
      int  r = nums.size() - 1;

        while(l <= r){
            if (target < nums[l] || target > nums[r])  return -1;
            if (target == nums[r])  return r;
            int m = l + floor(((target - nums[l])/(nums[r] - nums[l])) * (r - l));
            if (nums[m] == target){
                return m;
             } else if (nums[m] < target) {
                l = m + 1;
              } else {
                r = m - 1;
              }
        }
        return -1;
    }
};