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
        // stack<int> stackOne;
        // stack<int> stackTwo;

        // ListNode* node = l1;
        // while(node != nullptr) { 
        //     stackOne.push(node->val);
        //     node = node->next;
        // }

        // node = l2;
        // while(node != nullptr) { 
        //     stackTwo.push(node->val);
        //     node = node->next;
        // }

        // int numOne = 0;
        // int i = 1;
        // while(!stackOne.empty()) {
        //     numOne +=  stackOne.pop() * i;
        //     i *= 10;
        // }

        // int numTwo = 0;
        // i = 1;
        // while(!stackTwo.empty()) {
        //     numTwo +=  stackTwo.pop() * i;
        //     i *= 10;
        // }

        // int result = numOne + numTwo;

        bool carryOver = false;
        int currNum = 0;
        // bool first = true;
        stack<ListNode*> nodeStack;

        ListNode* currOne  = l1;
        ListNode* currTwo = l2;

        while(currOne || currTwo) {
            ListNode* node = new ListNode;

            // currNum = (stackOne.empty()) : stackTwo.pop() ? stackOne.pop() + stackTwo.pop();

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