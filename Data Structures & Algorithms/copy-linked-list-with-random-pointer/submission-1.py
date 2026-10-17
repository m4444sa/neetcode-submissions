class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = {None: None}

        # Pass 1: create a copy of every node, keyed by the original
        cur = head
        while cur:
            oldtocopy[cur] = Node(cur.val)
            cur = cur.next

        # Pass 2: wire up next and random using the map
        cur = head
        while cur:
            copy = oldtocopy[cur]
            copy.next = oldtocopy[cur.next]
            copy.random = oldtocopy[cur.random]
            cur = cur.next

        return oldtocopy[head]