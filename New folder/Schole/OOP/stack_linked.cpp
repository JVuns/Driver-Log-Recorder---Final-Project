#include<bits/stdc++.h>
using namespace std;

struct node {
	int data;
	node *next;
};

class Stack {
	public:
		node *top = NULL;
		void push(int val) {
			struct node* newnode = (struct node*) malloc(sizeof(struct node));
			newnode->data = val;
			newnode->next = top;
			top = newnode;
		}
		void pop() {
			if (top==NULL)
			cout << "Stack underflow" << endl;
			else {
				cout << "The popped element is " << top->data << endl;
				top = top->next;
			}
		}
		void display() {
			struct node* ptr;
			if (top==NULL)
			cout << "Stack is empty";
			else {
				ptr = top;
				cout << "Stack elements are: ";
				while (ptr != NULL) {
					cout << ptr->data << " ";
					ptr = ptr->next;
				}
			}
		}
		int peek() {
			if (top==NULL)
			cout << "Nothing in the stack yet";
			else {
			cout << "The topmost element in the stack is " << top->data << endl;
			}
		}	
};

int main() { 
	int ch, val;
	Stack st;
	cout << "*****MAIN MENU*****" << endl;
	cout << "1. PUSH" << endl;
	cout << "2. POP" << endl;
	cout << "3. PEEK" << endl;
	cout << "4. DISPLAY" << endl;
	cout << "5. EXIT" << endl;
	do {
		cout << "Enter your option: ";
		cin >> ch;
		switch (ch) {
			case 1: {
				cout << "Enter value to be pushed: ";
				cin >> val;
				st.push(val);
				break;
			}
			case 2: {
				st.pop();
				break;
			}
			case 3: {
				st.peek();
				cout << endl;
				break;
			}
			case 4: {
				st.display();
				cout << endl;
				break;
			}
			case 5: {
				cout << "Thank you for using the program" << endl;
				break;
			}
			default: {
				cout << "Invalid choice" << endl;
				break;
			}
		}
	}
	while(ch != 5);
	return 0;
}
