from typing import Optional


class ListNode[T]:
    def __init__(
        self,
        val: T,
        prev: Optional["ListNode[T]"] = None,
        next: Optional["ListNode[T]"] = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        result = []
        curr = self
        seen = set()

        while curr and curr not in seen:
            result.append(str(curr.val))
            seen.add(curr)
            curr = curr.next

        if curr is not None:
            result.append(f"{result[0]}... (cycle)")

        return " -> ".join(result)
