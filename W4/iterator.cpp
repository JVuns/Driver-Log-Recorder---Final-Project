#include <iostream.>
#include <vector>
#include <iterator>
using namespace std;

int main()
{
	int mynumber[]={1,3,6,7,8,10};
	vector<int> x;
	
	for(auto it=begin(mynumber);it!=end(mynumber);++it)
	{
		x.push_back(*it);
	}
	
	cout<<"mynumber = ";
	for(auto it=begin(x);it!=end(x); ++it)
	{
		cout<<" "<<*it;
	}
}
