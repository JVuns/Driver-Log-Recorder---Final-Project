#include <iostream>
#include <string>
using namespace std;

// your code here
template <class T>

T larger(T data1, T data2)
{
	cout<<data1<<data2;
	if(data1>data2)
	{
		return data1;
	}
	else
	{
		return data2;
	}
}

int main() {
	string data1, data2;
	
	cout << "Enter first data " << endl;
	cin >> data1;
	
	cout << "Enter second data " << endl;
	cin >> data2;
		
	cout << "The larger of " << data1 << " and " << data2 << " is " << larger(data1, data2) << endl;

	return 0;
}

// your code here


