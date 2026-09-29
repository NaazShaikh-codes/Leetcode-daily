class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        carry = 0
        dummy = ListNode(0)
        current = dummy
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            digit = total % 10
            carry = total // 10
            current.next = ListNode(digit)
            current = current.next
        return dummy.next