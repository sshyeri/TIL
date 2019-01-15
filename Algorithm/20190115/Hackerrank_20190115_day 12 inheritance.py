import numpy
n, m, p = map(int, input().split())
print(n, m, p)
array1 = numpy.array([list(map(int, input().split())) for i in range(n)])
array2 = numpy.array([list(map(int, input().split())) for i in range(m)])
print(array1, array2)

