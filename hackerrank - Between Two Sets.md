### [hackerrank - Between Two Sets](https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true)

You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being *between* the two arrays. You must determine how many such numbers exist.

For example, given the arrays  and , there are two numbers between them:  and . , , and  for the first value. Similarly, ,  and , .

**Function Description**

Complete the *getTotalX* function in the editor below. It should return the number of integers that are betwen the sets.

getTotalX has the following parameter(s):

- *a*: an array of integers
- *b*: an array of integers

**Input Format**

The first line contains two space-separated integers,  and , the number of elements in array  and the number of elements in array . 
The second line contains  distinct space-separated integers describing  where . 
The third line contains  distinct space-separated integers describing  where .

**Constraints**

- 
- 
- 

**Output Format**

Print the number of integers that are considered to be *between*  and .

**Sample Input**

```
2 3
2 4
16 32 96
```

**Sample Output**

```
3
```

**Explanation**

2 and 4 divide evenly into 4, 8, 12 and 16. 
4, 8 and 16 divide evenly into 16, 32, 96.

4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.



#### 다시해볼것!!

~~~python
#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    bcd=[]
    for i in range(max(a), min(b)+1):
        if min(b)%i == 0:
            bcd += [i]
    bcd = set(bcd)
    for i in b:
        for j in range(1, min(b)+1):
            if i%j != 0 and j in bcd:
                bcd -= {j}
    result = bcd.copy()
    for i in bcd:
        for j in a:
            if i%j != 0 and i in result:
                result -= {i}
    return len(result)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

~~~

