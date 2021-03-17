#include <iostream>
#include <vector>
using namespace std;

int main()
{
	vector<int> myvector;
	
	myvector.push_back(10);
	myvector.push_back(15);
	myvector.push_back(8);
	myvector.push_back(3);
	myvector.push_back(7);
	
	for(int i = 0; i<myvector.size();i++)
	{
		cout<<myvector[i]<<" ";
	}
	cout<<endl;
	
	cout<<"myvector.front() = "<<myvector.front()<<endl;
	cout<<"myvector.back() = "<<myvector.back()<<endl;
	cout<<"myvector order no 2 = "<<myvector[1]<<endl;
	myvector.erase(myvector.begin());
	
	cout<<"delete no 2 = ";
	for(int i = 0; i<myvector.size();i++)
	{
		cout<<myvector[i]<<" ";
	}
	cout<<endl;
}
