class Algo:
    def __init__(self,array:list):
        self.array = array

    # Class Variable
    comparision = 0
    swap = 0
    iteration = 0
    recursion = 0

    # Bubble Sort
    def bubbleSort(self):
        Algo.iteration = 0
        Algo.comparision = 0
        Algo.swap = 0
        pre = 0
        n = len(self.array)
        for i in range(n):
            Algo.iteration += 1
            for j in range(n-i-1):
                if self.array[j] > self.array[j+1]:
                    Algo.swap += 1
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                Algo.comparision += 1
            if pre == Algo.swap:
                return self.array
            pre = Algo.swap
        return self.array

    # Selection Sort  
    def selectionSort(self):
        Algo.iteration = 0
        Algo.comparision = 0
        Algo.swap = 0
        sorted = self.array.copy()
        sorted.sort()
        for i in range(len(self.array)):
            Algo.iteration += 1
            min_idx = i
            for j in range(i+1, len(self.array)):
                Algo.comparision += 1
                if self.array[min_idx] > self.array[j]:
                    min_idx = j
            if min_idx == i and self.array == sorted:
                    return self.array
            if min_idx != i:
                Algo.swap += 1
                self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
        return self.array
    
    # Insertion Sort
    def insertionSort(self):
        Algo.iteration = 0
        Algo.swap = 0
        Algo.comparision = 0
        i = 0
        for i in range(1, len(self.array)):
            Algo.iteration += 1
            key = self.array[i]
            j = i-1
            while j >= 0:
                if key < self.array[j]:
                    Algo.comparision += 1
                    self.array[j + 1] = self.array[j]
                    Algo.swap += 1
                    j -= 1
                else:
                    Algo.comparision += 1
                    break
            self.array[j + 1] = key
        return self.array
    
    # Merge Sort
    def __merge(self):
        Algo.recursion += 1
        if len(self.array) > 1:
            mid = len(self.array)//2
            L = self.array[:mid]
            R = self.array[mid:]
            leftsorter = Algo(L)
            leftsorter.__merge()
            rightsorter = Algo(R)
            rightsorter.__merge()
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    self.array[k] = L[i]
                    i += 1
                else:
                    self.array[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                self.array[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                self.array[k] = R[j]
                j += 1
                k += 1

    # Merge Sort
    def mergeSort(self):
        Algo.recursion = 0
        toSort = Algo(self.array)
        toSort.__merge()
        Algo.recursion -= 1
        return f'Recursions: {Algo.recursion}\nSorted Array: {self.array}'
    
    # Quick Sort
    def __partition(self,array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    # Quick Sort
    def __quick(self, low, high):
        Algo.recursion += 1
        if low < high:
            part = Algo(self.array)
            pi = part.__partition(self.array, low, high)
            low_quick = Algo(self.array)
            low_quick.__quick(low, pi - 1)
            high_quick = Algo(self.array)
            high_quick.__quick(pi + 1, high)
    
    # Quick Sort
    def quickSort(self):
        Algo.recursion = 0
        toSort = Algo(self.array)
        toSort.__quick(0,len(self.array)-1)
        Algo.recursion -= 1
        return f'Recursions: {Algo.recursion}\nSorted Array: {self.array}'

    def shellSort(self):
        pass

    def heapSort(self):
        pass

    def countingSort(self):
        pass

    def radixSort(self):
        pass

    def bucketSort(self):
        arr = []
        slot_num = 10
        for i in range(slot_num):
            arr.append([])
        for j in self.array:
            index_b = int(slot_num * j)
            arr[index_b].append(j)
        for i in range(slot_num):
            insert = Algo(arr[i])
            arr[i] = insert.insertionSort()
        k = 0
        for i in range(slot_num):
            for j in range(len(arr[i])):
                 self.array[k] = arr[i][j]
                 k += 1
        return f'{self.array}'