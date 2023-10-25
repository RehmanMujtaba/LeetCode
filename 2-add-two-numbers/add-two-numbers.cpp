/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        bool carryOver = false;
        int currNum = 0;
        stack<ListNode*> nodeStack;

        ListNode* currOne  = l1;
        ListNode* currTwo = l2;

        while(currOne || currTwo) {
            ListNode* node = new ListNode;

            if (!currTwo) {
                currNum = currOne->val;
                currOne = currOne->next;
            } else if (!currOne) {
                currNum = currTwo->val;
                currTwo = currTwo->next;
            } else {
                currNum = currOne->val + currTwo->val;
                currOne = currOne->next;
                currTwo = currTwo->next;
            }
            
            if (carryOver) {
                currNum += 1;
                carryOver = false;
            }


            if (currNum > 9) {
                carryOver = true;
                currNum -= 10;
            }

            ListNode* newNode = new ListNode(currNum);
            nodeStack.push(newNode);
        }

        // Deal with excess carry over
        if (carryOver) {
            ListNode* newNode = new ListNode(1);
            nodeStack.push(newNode);
        }

        ListNode* root = nullptr;
        while (nodeStack.empty() == false) {
            ListNode* newNode = nodeStack.top();
            nodeStack.pop();
            newNode->next = root;
            root = newNode;
        }

        return root;

    }
};