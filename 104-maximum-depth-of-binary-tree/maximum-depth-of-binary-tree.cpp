/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {

       if (!root) return 0;

       int leftMax = 1 + maxDepth(root->right);
       int rightMax = 1 + maxDepth(root->left);

       if (leftMax > rightMax) return leftMax;
        else return rightMax;
        // int rightMax = 1
        // int leftMax = 1

        // if (root.left) leftMax++;
        // if (root.right) rightMaxx++:

        // max = 
    }
};