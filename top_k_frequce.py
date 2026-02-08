import heapq
nums = [1,1,1,2,2,3]
k = 2
def top_k(nums, k):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    print(freq)
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)
    print(heap)               
    print(heapq.heappop(heap))
    print(heap)
    print(num for count, num in heap)
    return [num for count, num in heap]

top_k(nums, k)

# assert set(top_k([1,1,1,2,2,3], 2)) == {1,2}