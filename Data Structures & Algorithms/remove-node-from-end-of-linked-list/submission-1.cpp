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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode*dummy = new ListNode(0,head);
        ListNode*left = dummy;
        ListNode* right= head;
        while (n>0){
            right=right->next;
            n--;
        }// 0 to n window

        while(right!=nullptr){
            left= left->next;

            right = right->next;
        }//window to the end

        left->next=left->next->next; 
        return dummy->next;// skip one, the one nth from the back
    }
};
