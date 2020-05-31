class Solution:
    """
    输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，
    则最小的4个数字是1、2、3、4。
    """
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k==0:
            return []

        def maxHeapfy(maxHeap, i, n):
            left=2*i+1
            right=2*i+2
            maxPoint=i
            if left < n and maxHeap[left] > maxHeap[maxPoint]:
                maxPoint = left
            if right < n and maxHeap[right]>maxHeap[maxPoint]:
                maxPoint = right
            if maxPoint != i:
                maxHeap[i],maxHeap[maxPoint]=maxHeap[maxPoint],maxHeap[i]
                maxHeapfy(maxHeap,maxPoint,n)
        maxHeap= arr[:k]
        n = len(arr)
        for i in range(k//2-1, -1, -1):
            maxHeapfy(maxHeap, i, k)
        
        for i in range(k, n):
            if arr[i] < maxHeap[0]:
                maxHeap[0]=arr[i]
                maxHeapfy(maxHeap, 0, k)

        for i in range(k-1, 0, -1):
            maxHeap[i], maxHeap[0] = maxHeap[0], maxHeap[i]
            maxHeapfy(maxHeap, 0, i)
        
        return maxHeap