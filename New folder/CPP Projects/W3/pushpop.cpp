#include<iostream>
#include<queue>
using namespace std;

void printQueue(queue<int> q) {
	queue<int> qu = q;
	while (!qu.empty()) {
		cout << qu.front() << " ";
		qu.pop();
	}
	cout << endl;
}

int main() {
	queue<int> a;
	
	cout << "a.empty() = " <<a.empty() << endl;
	a.push(1);
	a.push(2);
	a.push(3);
	
	cout << "Queue = ";
	printQueue(a);
	
	cout << "a.empty() = " << a.empty() << endl;
	cout << "a.size() = " << a.size() << endl;
	cout << "a.front() = " << a.front() << endl;
	cout << "a.back() = " << a.back() << endl; 
	
	cout << "a.pop() = ";
	a.pop();
	printQueue(a);
	
	cout << "a.push() = ";
	a.push(4);
	printQueue(a);
	
	return 0;
}

