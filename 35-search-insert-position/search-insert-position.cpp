class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int top = nums.size()-1;
        int bottom = 0;
        while (bottom <= top) {
            int spot = floor((top+bottom)/2);
                        cout << "TOP is: " << top << " BOTTOM is: " << bottom << " MID is: " << spot << endl;
            if (nums[spot] == target) {
                return spot;
            } else if (nums[spot] < target) {
                bottom = spot + 1;
            } else if (nums[spot] > target) {
                top = spot - 1;
            }
        }
        return bottom;
    }
};