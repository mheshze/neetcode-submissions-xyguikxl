class LinkedList:
    
    def __init__(self): 
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        ind = 0
        temp = self.head.next
        while temp:
            if ind == index:
                return temp.val
            ind += 1           
            temp = temp.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val,self.head.next)
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
        

    def remove(self, index: int) -> bool:
        #  go till the the value before index
        i = 0
        curr = self.head
        while i< index and curr:
            i+=1
            curr = curr.next
        
        # add it now to the thingy
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False



    def getValues(self) -> List[int]:
        res = []
        cur = self.head.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
        

class ListNode:
    def __init__(self,val,nextNode=None) -> None:
        self.next = nextNode
        self.val = val