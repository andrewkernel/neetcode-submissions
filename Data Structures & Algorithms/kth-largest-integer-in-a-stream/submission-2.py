class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        

    def add(self, val: int) -> int:
        heap = []
        self.nums.append(val)
        heapq.heapify(heap)

        for num in self.nums:
            heapq.heappush(heap, num)

            while self.k < len(heap):
                heapq.heappop(heap)
        
        return int(heap[0])
        
