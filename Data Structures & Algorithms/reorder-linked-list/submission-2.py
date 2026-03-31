# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arrList = []
        temp = head
        while temp:
            arrList.append(temp)
            temp = temp.next
        
        i = 0
        j = len(arrList) - 1
        while i < j:
            if i >= j:
                break
            arrList[i].next = arrList[j]
            i += 1
            arrList[j].next = arrList[i]
            j -= 1
        arrList[i].next = None
            
