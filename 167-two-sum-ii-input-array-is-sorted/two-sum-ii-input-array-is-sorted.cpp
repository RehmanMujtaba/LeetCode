class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // Time: O(n)
        // Space: O(1)

        int low = 0;
        int high = numbers.size() - 1;
        vector<int> solution;

        while(true) {
            if (numbers[low] + numbers[high] == target) {
                solution.push_back(low + 1);
                solution.push_back(high + 1);
                        return solution;
            }
            if (numbers[low] + numbers[high] < target) {
                low++;
            } else if (numbers[low] + numbers[high] > target) {
                high--;
            }
        }
        return solution;
    }
};