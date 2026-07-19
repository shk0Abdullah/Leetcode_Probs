# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Definition for singly-linked list.
        lst1 = []
        lst2 = []

        try:
            while l1 or l2:
                if l1:
                    lst1.append(l1.val)
                else:
                    lst1.append(0)

                if l2:
                    lst2.append(l2.val)
                else:
                    lst2.append(0)

                try:
                    l1 = l1.next
                except:
                    l1 = False

                try:
                    l2 = l2.next
                except:
                    l2 = False

            raise Exception

        except:

            lst2 = lst2[-1::-1]
            lst1 = lst1[-1::-1]

            carry = 0
            head = ListNode()
            r = head
            i = -1

            try:
                while True:
                    result = lst1[i] + lst2[i] + carry

                    carry = 0

                    if result <= 9:
                        r.val = result
                    else:
                        r.val = result % 10
                        carry = 1

                    i -= 1

                    # Only create a new node if there are more digits left
                    if abs(i) <= len(lst1):
                        r.next = ListNode()
                        r = r.next
                    elif carry:
                        r.next = ListNode(carry)
                        break
                    else:
                        break

            except IndexError:
                if carry:
                    r.next = ListNode(carry)

            return head