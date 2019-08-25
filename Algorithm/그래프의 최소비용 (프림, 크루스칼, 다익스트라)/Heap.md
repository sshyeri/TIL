## 힙(heap)

- 완전 이진 트리의 일종으로 부모 노드와 자식 노드간에 항상 대소관계가 성립하는 자료구조
- 부모 노드가 자식 노드보다 항상 크면 최대힙(Max Heap) 그 반대는 최소힙(Min Heap)
- 부모-자식 노드의 대소관계만 중요하며 형제 노드들간에는 관계 없음.
- 우선순위큐(Priority Queue)의 구현이 가능.

### 구현

- 완전 이진 트리는 배열로 구현
- 구현을 쉽게 하기 위해 인덱스는 1부터 사용
- 현재 노드 : current
- 부모 노드 : current / 2
- 좌측 자식 : current * 2, 우측 자식 : current * 2 + 1

#### 삽입

1. 가장 끝에 원소를 추가
2. 추가한 값과 부모 노드와 크기 비교하며 교환

~~~c++
// 최소힙

void push(int value){
  heap[++heap_cnt] = value;
  
  int current = heap_cnt;
	int parent = current/2
  while(current>1 && heap[parent] > heap[current]){
    swap(&heap[parent], &heap[child]);
    current /= 2;
    parent /= 2;
  }
}
~~~

#### 삭제



#### 참고자료

- [TWpower's Tech Blog](https://twpower.github.io/137-heap-implementation-in-cpp)