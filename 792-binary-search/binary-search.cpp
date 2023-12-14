class Solution {
public:
    int search(vector<int>& nums, int target) {

      int   l = 0;
      int  r = nums.size() - 1;
      int   k = target;

        while(l <= r){
            if (k < nums[l] || k > nums[r])  return -1;
            if (k == nums[r])  return r;
            int m = l + floor(((k - nums[l])/(nums[r] - nums[l])) * (r - l));
            int num = nums[m];
            if (num == k){
                return m;
             } else if (num < k) {
                l = m + 1;
              } else {
                r = m - 1;
              }
        }
        return -1;
    }
};