class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        queue = deque()
        stones.sort()
        for stone in stones:
            queue.append(stone)
        while len(queue) > 1:
            stone1 = queue.pop()
            stone2 = queue.pop()
            if stone1 < stone2:
                stone2 -= stone1
                queue.append(stone2)
            if stone2 < stone1:
                stone1 -= stone2
                queue.append(stone1)
            queue = deque(sorted(queue))
        if len(queue) == 0:
            return 0
        else: 
            return queue.pop()
