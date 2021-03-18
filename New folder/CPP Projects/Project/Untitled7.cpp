#include <algorithm>
#include <iterator>
#include <string>
#include <iostream>
using namespace std;

int main(){
	// declare variables
	string day;
	string weekday[5]={"Monday","Tuesday","Wednesday","Thursday","Friday"};
	string weekend[2]={"Sunday", "Saturday"};
		
	// print message to the console
	cout << "What day is it today?" << endl;
	
	// get input data
	cin >> day;
	
	// process the data	
//	if (find(begin(weekday), end(weekday), 99) != end(ourArray))
//	{
//		cout<<"Im studying";
//	}
//	else
//		cout<<"I go fishing";
	
	for(int i = 0;i<7;i++)
	{
		if(weekday[i] == day)
		{
		cout<<"Im studying";
		return 0;
		}
		if(weekend[i] == day)
		{
		cout<<"I go fishing";
		return 0;
		}
		if(i==7)
		{
		cout<<"invalid data";
		return 0;
		}
		}	
		

}

