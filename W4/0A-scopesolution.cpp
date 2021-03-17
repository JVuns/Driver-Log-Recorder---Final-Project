#include <iostream>
using namespace std;

int mynumber =1;

int main(void){
	int mynumber = 2;
	
	cout<<mynumber<<endl;
	cout<<::mynumber<<endl;
	
	::mynumber=5;
	mynumber = 10;
	
	cout<<mynumber<<endl;
	cout<<::mynumber<<endl;
	
	return 0;
}
