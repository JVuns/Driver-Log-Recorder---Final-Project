#include <iostream>
#include <queue>
#include <bits/stdc++.h>
using namespace std;

class Queue
{
private:
	#define MAX 5
	int queue[MAX];
	int front = -1;
	int rear = -1;

public:
	int insert(int);
	int delete_element();
	int peek();
	void display();
};

int insert(queue<int> que)
{
	int elm;
	if(queue[MAX]==rear)
	{
		cout<<"OVERFLOW";	
	}
	else if(front == -1 && rear == -1)
	cout<<"Element: ";
	cin>>elm;
	que.push(elm);
}

void display(queue<int> que) {
	queue<int> qu = que;
	while (!qu.empty()) {
		cout << qu.front() << " ";
		qu.pop();
	}
	cout<<"Finished displaying"<<endl;
}

int main()
{
	queue<int> que;
	bool running;
	running = true;
	while(running = true)
	{
		int input;
		cout<<"***** MAIN MENU *****"<<endl;
		cout<<"1. Insert"<<endl;
		cout<<"2. Delete"<<endl;
		cout<<"3. Peek"<<endl;
		cout<<"4. Display the queue"<<endl;
		cout<<"5. Exit"<<endl;
		cin>>input;
		switch(input)
		{
			case 1:
				insert(que);
//			case 2:
//				delete_element();
//			case 3:
//				peek();
			case 4:
				display(que);
		}
	}
}

