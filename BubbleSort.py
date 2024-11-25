"""""
In place sort:
O(n**2) time complexity, O(1) space
each item in array, we have n swap
so n items * n swaps = O(n**2)
"""
class BubbleSort(object):
    def bubblesort(self, arr):
        n = len(arr)
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]

bsort = BubbleSort()
arr = [706500, 4, 60000, 12, -329025444, -672423, 12324]
print(arr)
bsort.bubblesort(arr)
print(arr)