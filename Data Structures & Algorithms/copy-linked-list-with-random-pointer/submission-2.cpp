/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/


//two passes, first for creating deepcopys and hashmaps old nodes to the copies
//second pass is for node connecting
//linear time and o(n) memory

class Solution {
public:

    unordered_map<Node*, Node*> map;
    Node* copyRandomList(Node* head) {
        if (head==nullptr) return nullptr;
        if(map.count(head)) return map[head];

        Node* copy= new Node(head->val);
        map[head]=copy;
        copy->next=copyRandomList(head->next);
        copy->random=map[head->random];
        return copy;
        
        
    }
};
