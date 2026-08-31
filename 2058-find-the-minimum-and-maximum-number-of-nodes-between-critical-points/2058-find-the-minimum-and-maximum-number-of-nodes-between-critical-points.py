# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next 
        position = 1

        first = -1
        last = -1
        min_dist = float("inf")
        while curr.next:
            next_node = curr.next
            if((curr.val>prev.val and curr.val > next_node.val)or(curr.val<prev.val and curr.val< next_node.val) ):
                if first == -1:
                 first = position 

                else:
                    min_dist = min(min_dist,position - last)
                last = position
            prev = curr
            curr = next_node
            position +=1
        if first == last:
            return[-1,-1]
        max_dist = last - first
        return [min_dist,max_dist]

                        