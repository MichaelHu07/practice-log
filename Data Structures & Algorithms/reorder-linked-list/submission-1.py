# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        queue = deque()
        while head != None:
            queue.append(head)
            head = head.next
        counter = 0
            
        cur = queue.popleft()
        end = queue.pop()
        while True:
            if counter % 2 == 0:
                cur.next = end
                if len(queue) > 0:
                    cur = queue.popleft()
                else:
                    end.next = None
                    break
                counter += 1
            else: 
                end.next = cur
                if len(queue) > 0:
                    end = queue.pop()
                else: 
                    cur.next = None
                    break
                counter += 1
            



