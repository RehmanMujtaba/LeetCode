class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        
       int odd_ptr = 1;
       int  even_ptr = 0;

        while(odd_ptr < nums.size()) {
            if (nums[odd_ptr] % 2 == 1) {
                odd_ptr += 2;
            } else if (nums[even_ptr] % 2 == 0) {
                even_ptr += 2;
            } else {
                // int temp = nums[odd_ptr];
                // nums[odd_ptr] = nums[even_ptr];
                // nums[even_ptr] = temp;
                swap(nums[odd_ptr], nums[even_ptr]);
                even_ptr += 2;
                odd_ptr += 2;
            }
        }
        return nums;
    }
};