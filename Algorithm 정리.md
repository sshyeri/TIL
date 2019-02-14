# 알고리즘?

- 알고리즘은 문제를 해결하기 위한 방법

  ### 무엇이 좋은 알고리즘인가?

  1. 정확성 : 얼마나 정확하게 동작하는가
  2. 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
  3. 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
  4. 단순성 : 얼마나 단순한가
  5. 최적성 : 더 이상 개선할 여지없이 최적화되었는가

## 시간복잡도 Big O

- 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시
- 요소 수가 증가에 따른 연산수

![BigO_complexity](C:\Users\student\Desktop\hyeri\TIL\images\BigO_complexity.JPG)



# 완전 검색(Exaustive Search)

- **Brute-force** 혹은 **generate-and-test **기법이라고도 불린다.
- 모든 경우의 수를 테스트한 후, 최종 해법을 도출한다.
- 일반적으로 경우의 수가 상대적으로 작을 때 유용하다.
- 문제를 풀 때, 우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직하다.

# 탐욕(Greedy) 알고리즘

- 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행해 최종적인 해답에 도달한다.

- 지역적으로는 최적이지만, 이들을 수집해 얻은 최종해는 최적이라는 보장이 없다.

- 일반적으로, 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근이 된다.

  ### 동작 과정

  1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합(Solution Set)에 추가한다.
  2. 실행 가능성 검사 : 새로운 부분해 집합이 실행 가능한지를 확인한다. 곧, 문제의 제약 조건을 위반하지 않는지를 검사한다.
  3. 해 검사 : 새로운 부분해 집합이 문제의 해가 되는지를 확인한다. 아직 전체 문제의 해가 완성되지 않았다면 1의 해 선택부터 다시한다.


# 정렬

## 버블 정렬 O(n <sup>2</sup> )

- 코딩이 가장 손쉽다.

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
- 정렬 과정
  - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
  - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬
  - 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다 하여 버블 정렬 이라고 함

~~~python
def BubbleSort(a):
    for i in range(len(a)-1, 0, -1): # 범위 끝 위치
        for i in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]	 #swap!
~~~



## 카운팅 정렬 O(n+k) 

>  n 리스트 길이, k 정수의 최대값

- 길이, 범위가 비교적 작을 경우 가능

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

- 제한 사항

  - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
  - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.

- 정렬 과정

  - Data에서 각 항목들의 발생 회수 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열에 저장

  ~~~
  Data 	0 4 1 3 1 2 4 1
  counts 	1 3 1 1 2
  0 1 1 1 2 3 4 4
  ~~~

  - 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 counts의 원소 조정

  ~~~
  Data 	0 4 1 3 1 2 4 1
  counts 	1 3 1 1 2
  counts 	1 4 5 6 8
  temp	
  ~~~

~~~python
def counting_sort(A, B, k)
#A[1 .. n] -- 입력 배열 ( 1 to k)
#B[1 .. n] -- 정렬된 배열
#C[1 .. k] -- 카운트 배열

C = [0]*k

for i in range(len(A)):
    C[A[i]] += 1
for i in range(1, len(C)):
    C[i] += C[i-1]
for i in range(len(A)-1, -1, -1):
    B[C[A[i]]-1] = A[i]
    C[A[i]] -= 1
    
~~~



### 선택 정렬



### 퀵 정렬



### 삽입 정렬



### 병합 정렬



## 정렬 알고리즘 비교

|  알고리즘   |   평균 수행시간   |   최악 수행시간   | 알고리즘 기법 | 비고                                                         |
| :---------: | :---------------: | :---------------: | :-----------: | :----------------------------------------------------------- |
|  버블 정렬  | O(n<sup>2</sup> ) | O(n<sup>2</sup> ) |  비교와 교환  | 코딩이 가장 손쉽다.                                          |
| 카운팅 정렬 |      O(n+k)       |      O(n+k)       |  비교환 방식  | n이 비교적 작을 때만 가능하다.                               |
|  선택 정렬  | O(n<sup>2</sup>)  | O(n<sup>2</sup> ) |  비교와 교환  | 교환의 회수가 버블, 삽입정렬보다 작다.                       |
|   퀵 정렬   |    O(n log n)     | O(n<sup>2</sup>)  |   분할 정복   | 최악의 경우 O(n<sup>2</sup>)이지만, 평균적으로는 가장 빠르다. |
|  삽입 정렬  | O(n<sup>2</sup>)  | O(n<sup>2</sup> ) |  비교와 교환  | n의 개수가 작을 때 효과적이다.                               |
|  병합 정렬  |    O(n log n)     |    O(n log n)     |   분할 정복   | 연결리스트의 경우 가장 효율적인 방식                         |



# 2차원 배열

### 지그재그 순회

~~~python
#n*m 행렬의 i 행 j 열
for i in range(n):
    for j in range(m):
        arr[i][j + (m-1-2*j)*(i%2)]
~~~



### 델타를 이용한 2차 배열 탐색 (4방향 인접)

~~~python
arr = [[0 for i in range(n)] for j in range(m)]
dx = [0, 0, -1, 1] #상하좌우
dy = [-1, 1, 0, 0]

for x in range(len(arr)):
    for y in range(len(ary[x])):
        for i in range(4):
            test(arr[x+dx[i][y+dy[i]]])
~~~



### 전치 행렬

~~~python
#i행 j열
for i in range(n):
    for j in range(m):
        if i < j : 
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
~~~



# 비트 연산자

`&` : 비트 단위로 AND 연산을 한다.

`|` : 비트 단위로 OR 연산을 한다.

`<<` : 피연산자의 비트 열을 왼쪽으로 이동시킨다.

`>>` : 피연산자의 비트 열을 오른쪽으로 이동시킨다.

~~~python
#왼쪽이 피연산자. 피연산자를 이진수로 변환하여 오른쪽의 수 만큼 칸수 이동.
>>> 1<<4
16
#1 -> 10000

>>> 8<<1
16
#1000(8) -> 10000(16)

>>> 8>>1
4
#1000(8) -> 100(4)

~~~







# 문자열 매칭 알고리즘

찾고자 하는 문자열 패턴의 길이 m, 총 문자열 길이 n

### 고지식한 패턴 검색 알고리즘

### 카프-라빈 알고리즘

### KMP 알고리즘





### 보이어-무어 알고리즘 

- 패턴에 오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 패턴의 길이만큼.

- 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴내에 존재할 경우 기준을 맞춰준다.

- 일반적으로 **O(n)**보다 시간이 덜 듬, 최악의 경우: **O(mn)**
- `발상의 전환` : 패턴의 오른쪽부터 비교. 

![1548654234945](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548654234945.png)





### 정수표현

1. 부호와 절대치로 나뉘어 표현

2. 1의 보수
3. 2의 보수

# Stack



## 1. Stack의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조

- 선형 구조

  > 선형 구조 : 자료 간의 관계가 1대1의 관계
  >
  > 비선형구조 : 자료 간의 관계가 1대N의 관계(ex:트리)

- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.

- 마지막에 삽입한 자료를 가장먼저 꺼낸다. **LIFO(후입선출)**

- ADT(추상 자료형)이다.



## 2. 자료구조와 연산

> Class처럼 구성

### 자료구조

- C언어에서는 배열을 사용할 수 있다.
- 저장소 자체를 스택이라 부르기도 한다.
- 스택에서 마지막 삽입된 원소의 위치를  top이라 부른다.

### 연산

- **push **삽입 : 저장소에 자료를 저장
- **pop** 삭제 : 저장소에서 자료를 꺼낸다.  삽입한 자료의 역순으로
- **isEmpty** : 스택이 공백인지 아닌지 확인
- **peek** : 스택의 top에 있는 item(원소)을 반환

### python code

```python
class Stack:
    s=[]
    
    def push(self, item):
        self.s.append(item)
    def pop(self):
        if self.s:
            return self.s.pop()
        else:
            return "Stack is empty!"
    def isEmpty(self):
        if self.s:
            return False
        else:
            return True
    def peek(self):
        return self.s[-1]
    
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.isEmpty()
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

#-------output-----
Stack is not empty
3
3
2
1
Stack is empty!
Stack is empty!
```



## 3. 응용

### 괄호검사

- 괄호의 짝을 검사한다.

```python
s = Stack()
k = ['(','[','{']
kk = [')',']','}']

for i in input():
    if i in k:
        s.push(i)
    elif i in kk:
        if s.pop() != k[kk.index(i)]:
            print("짝이 맞지 않습니다.")
            break
if s.isEmpty():
    print("모든 짝이 맞습니다.")
else:
    print("짝이 맞지 않습니다.")
```

### function call

- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
  - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료.
  - 후입 선출 구조의 스택을 이용해 수행순서 관리
  - 함수 호출 발생 : 함수의 정보를 스택 프레임에 저장해 시스탬 스택에 삽입
  - 함수 실행 종료 : 시스템 스택의 top원소(스택 프레임)을 삭제(pop)하면서  프레임에 저장되어 있던 복귀주소 확인하고 복귀
  - 함수 호출과 복귀에 따라 이 과정을 반복해 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.



# 재귀 호출

- 자기 자신을 호출하여 순환 수행되는 것
- python에서 최대 재귀 깊이가 1,000번
- for문이 더 효율적일 때가 많음



## 응용

### 팩토리얼

```python
  def factorial(n):
      if n == 1:
          return 1
      else:
          return n * factorial(n-1)
  
  print(factorial(7))
  #output : 5040
```

### 피보나치

```python
  def fibo(n):
      if n < 2:
          return n
      else:
          return fibo(n-1) + fibo(n-2)
  
  print(fibo(8))
  #output : 21
```

> 피보나치 수를 구하는 함수를 재귀함수로 구현한 알고리즘은
>
> "엄청난 중복 호출이 존재한다"는 문제점이 있다.
>
>

# DP(동적계획법)

## Memoization

- 메모이제이션은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술이다. **동적 계획법의 핵심이 되는 기술이다.**
- 'memoization'은 글자 그대로 해석하면 '메모리에 넣기'라는 의미이며 '기억되어야 할 것' 이라는 뜻의 라틴어 memorandum에서 파생되었다. 흔히 '기억하기', '암기하기'라는 뜻의 memorization과 혼동하지만 정확한 단어는 memoization, 동사형은 memoize이다.

- 앞의 예의 피보나치 수를 구하는 알고리즘에서  fibo(n)의 값을 계산하자마자 저장하면 (memoize), 실행시간을 O(n)으로 줄일 수 있다.

- DP는 점화식을 잘 찾아야 한다! 점화식은 곧 재귀식!

  ```python
  def fibo(n) :
      global memo
      if n >= 2 and len(memo) <= n :
          memo.append(fibo(n-1) + fibo(n-2))
      return memo[n]
  memo = [0, 1]
  
  def fibo2(n):
      f = [0, 1]
      for i in range(2, n + 1):
          f.append(f[i-1] + f[i-2])
      return f[n]
  ```


## DFS(깊이우선탐색)

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 후입선출 구조의 스택 사용 

### 알고리즘

1. 시작 정점 v를 결정하여 방문한다.
2. 정점 v에 인접한 정점 중에서
   1. 방문하지 않은 정점 w가 있으면,  정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w로 하여 다시 2.를 반복한다.
   2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2.를 반복한다.
3. 스택이 공백이 될 때까지 2.를 반복한다.

```python
def dfs(s):
    print(s,end=" ")
    visited[s] = 1
    for i in range(1, len(G[s])):
        if visited[i]==0 and G[s][i]==1:
                dfs(i)

n, e = map(int,input().split())
n += 1
temp = list(map(int, input().split()))

G = [[0 for i in range(n)] for j in range(n)]
visited = [0 for i in range(len(G))]

for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(n):
    print(f"{i} {G[i]}")

dfs(1)

'''
input
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
output
0 [0, 0, 0, 0, 0, 0, 0, 0]
1 [0, 0, 1, 1, 0, 0, 0, 0]
2 [0, 1, 0, 0, 1, 1, 0, 0]
3 [0, 1, 0, 0, 0, 0, 0, 1]
4 [0, 0, 1, 0, 0, 0, 1, 0]
5 [0, 0, 1, 0, 0, 0, 1, 0]
6 [0, 0, 0, 0, 1, 1, 0, 1]
7 [0, 0, 0, 1, 0, 0, 1, 0]
1 2 4 6 5 7 3 
'''

```



# Code Tip

### 큰 수 리스트에 한자리씩 넣기

```python
arr = []
while i > 0:
    arr += [num%10]
    arr //= 10
```

### if else 문과 and or

```python
if a:
    k = b
else:
    k = c
--------------
k = (a and b) or c
```

```python
def my_bin(num):
    if num == 1:
        return '0b1'
    else:
        return my_bin(num//2) + str(num % 2)
----------------------
def my_bin(num):
    return '0b1' if num == 1 else my_bin(num//2) + str(num % 2)
-----------------------
def my_bin(num):
    return (num == 1 and '0b1') or (my_bin(num//2) + str(num % 2))
```

