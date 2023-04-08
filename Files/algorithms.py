class Algo:

    def __init__(self,array):
        self.array = array

    def bubbleSort(self):
        comparision = 0
        swap = 0
        pre = 0
        n = len(self.array)
        for i in range(n):
            for j in range(n-i-1):
                if self.array[j] > self.array[j+1]:
                    swap += 1
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                comparision += 1
            if pre == swap:
                return f'Iterations: {i+1}\nComparisions: {comparision}\nSwaps: {swap}\nSorted Array: {self.array}'
            pre = swap
        return f'Iterations: {i+1}\nComparisions: {comparision}\nSwaps: {swap}\nSorted Array: {self.array}'
    
    def selectionSort(self):
        comparision = 0
        swap = 0
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i+1, len(self.array)):
                comparision += 1
                if self.array[min_idx] > self.array[j]:
                    min_idx = j
            if min_idx == i:
                    return f'Iterations: {i+1}\nComparisions: {comparision}\nSwaps: {swap}\nSorted Array: {self.array}'
            swap += 1
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
        return f'Iterations: {i+1}\nComparisions: {comparision}\nSwaps: {swap}\nSorted Array: {self.array}'
    
    def insertionSort(self):
        swap = 0
        comparision = 0
        i = 0
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i-1
            while j >= 0:
                if key < self.array[j]:
                    comparision += 1
                    self.array[j + 1] = self.array[j]
                    swap += 1
                    j -= 1
                else:
                    comparision += 1
                    break
            self.array[j + 1] = key
        return f'Iterations: {i+1}\nComparisions: {comparision}\nSwaps: {swap}\nSorted Array: {self.array}'
    
    def mergeSort(self):
        pass

    def quickSort(self):
        pass

    def shellSort(self):
        pass

    def heapSort(self):
        pass

    def countingSort(self):
        pass

    def radixSort(self):
        pass

    def bucketSort(self):
        pass