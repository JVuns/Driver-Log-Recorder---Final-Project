#include <iostream>
#include <deque>
using namespace std;

int main()
{
	deque<int>mydeque;
	int n;
	
	cout<<"Enter a number: ";
	cin>>n;
	
	for(int i=1;i<=n;i++)
	{
		mydeque.push_back(i);
	}
	cout<<"mydeque = ";
	
	deque<int>::iterator it = mydeque.begin();
	
	while(it!=mydeque.end())
	{
		cout<<" "<<*it++;
	}
}
