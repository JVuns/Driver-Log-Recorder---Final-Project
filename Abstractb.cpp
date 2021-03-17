#include<bits/stdc++.h>
using namespace std;

void printStack(stack<int> st) {
	while (!st.empty()) {
		cout << st.top() << " ";
		st.pop();
	}
	cout << "\n";
}
int main() {
	
	stack<int> st;
	st.push(7);
	st.push(3);
	st.push(4);
	st.push(1);
	
	cout << "Stack size = " << st.size() << endl;
	printStack(st);
	
	cout << "\nTop stack = " << st.top();
	
	st.pop();
	
	cout << "\nPop stack. Stack size = " << st.size() << endl;
	printStack(st);
	
	st.pop();
	
	cout << "\nPop more. Stack size = " << st.size() << endl; 
	return 0;

}

