#include <iostream>
#include <queue>
using namespace std;

int main()
{
	queue<int> qu;
	int x, y;

	x = 4;
	y = 5;
	qu.push(x);
	qu.push(y);
	x = qu.front();
	qu.pop();
	qu.push(x+5);
	qu.push(16);
	qu.push(x);
	qu.push(y-3);
	cout<<"Queue Elements: ";
	while(!qu.empty())
	{
		cout<<qu.front()<<" ";
		qu.pop();
	}
	cout<<endl;
	
}
