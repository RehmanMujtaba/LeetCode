class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int low = 0;
        int high = numbers.size() - 1;
        vector<int> solution;

        while(low < high) {
            int current = numbers[low] + numbers[high];

            if (current == target) {
                solution.push_back(low + 1);
                solution.push_back(high + 1);
                break;
            }
            if (current < target) {
                low++;
            } else if (current > target) {
                high--;
            }
        }

        return solution;
    }
};