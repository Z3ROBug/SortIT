class Algo:
    def __init__(self,array):
        self.array = array

    recursion = 0

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

    def mergeSort(self):
        Algo.recursion = 0
        toSort = Algo(self.array)
        toSort.__merge()
        Algo.recursion -= 1
        return f'Recursions: {Algo.recursion}\nSorted Array: {self.array}'
    
    def __partition(self,array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def __quick(self, low, high):
        Algo.recursion += 1
        if low < high:
            part = Algo(self.array)
            pi = part.__partition(self.array, low, high)
            low_quick = Algo(self.array)
            low_quick.__quick(low, pi - 1)
            high_quick = Algo(self.array)
            high_quick.__quick(pi + 1, high)
    
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
        pass



# # text = '6,4,2,351,2511,24,5221,12312,1124,52'
# # sort = text.split(",")
# sort = [6,4,2,351,2511,24,5221,12312,1124,52]
# length = len(sort)
# try:
#     flo = False
#     for i in range(length):
#         index = sort[i].find(".")
#         if index != -1:
#             flo = True
#     if flo:
#         for i in range(length):
#             sort[i] = float(sort[i])
#     else:
#         raise
# except:
#     # sort = text.split(",")
#     sort = [6,4,2,351,2511,24,5221,12312,1124,52]
#     try:
#         integer = False
#         for i in range(length):
#             if sort[i].find(".") == -1:
#                 integer = True
#         if integer:
#             for i in range(length):
#                 sort[i] = int(sort[i])
#     except:
#         # sort = text.split(",")
#         sort = [6,4,2,351,2511,24,5221,12312,1124,52]
# a = Algo(sort)
# # a.mergeSort()
# print(a.selectionSort())