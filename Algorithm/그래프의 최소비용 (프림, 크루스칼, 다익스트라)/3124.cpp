// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

#define MAXV 100000

int T, V, E;

int link[MAXV];
int Size[MAXV];

int find(int x) {
	while (x != link[x]) x = link[x];
	return x;
}

bool same(int a, int b) {
	return find(a) == find(b);
}

void unite(int a, int b) {
	a = find(a);
	b = find(b);
	if (Size[a] < Size[b])
		swap(a, b); // always a > b _swap(T &a, T &b)
	link[b] = a;
	Size[a] += Size[b];
}	

int main() {
	int A, B, C;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> V >> E;
		vector<pair<int, pair<int, int>>> edges;
		for (int i = 0; i < V; i++) 
			link[i] = i, Size[i] = 1;
		for (int i = 0; i < E; i++) {
			cin >> A >> B >> C;
			A--; B--;
			edges.push_back({ C, {A, B } });
		}
		sort(edges.begin(), edges.end());
		long long weight = 0;
		for (auto edge : edges) {
			int a = edge.second.first;
			int b = edge.second.second;
			int w = edge.first;
			if (!same(a, b)) {
				unite(a, b);
				weight += w;
			}	
		}
		cout << "#" << tc << ' ' << weight << endl;
	}
}