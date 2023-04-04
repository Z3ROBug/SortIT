# def bubbleSort(array):
#         swap = 0
#         comparision = 0
#         pre = 0
#         n = len(array)
#         for i in range(n):
#             for j in range(n-i-1):
#                 if array[j] > array[j+1]:
#                     swap += 1
#                     array[j], array[j+1] = array[j+1], array[j]
#                 comparision += 1
#             if pre == swap:
#                 print(f"Iteration: {i+1}\tComparision: {comparision}\tSwaps: {swap}\nArray: {array}")
#                 # res = font2.render(f"Iteration: {i+1}\tComparision: {comparision}\tSwaps: {swap}\t\tArray: {array.array}", True, 'Black')
#                 # screen.blit(res,(320,370+array.initial_pos))
#                 break
#             pre = swap
#             print(f"Iteration: {i+1}\tComparision: {comparision}\tSwaps: {swap}\nArray: {array}")
#             # res = font2.render(f"Iteration: {i+1}\tComparision: {comparision}\tSwaps: {swap}\t\tArray: {array.array}", True, 'Black')
#             # screen.blit(res,(320,370+array.initial_pos))
#             # array.initial_pos += 20

# bubbleSort(['P','Y','T','H','O','N'])

def Addition(matrixA, matrixB):
    matrix = []
    n = len(matrixA)
    for i in range(n):
        r = []
        for j in range(n):
            sum = matrixA[i][j] + matrixB[i][j]
            r.append(sum)
        matrix.append(r)
    return matrix


print(Addition([1,2,3,4],[4,3,2,1]))