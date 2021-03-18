#include <iostream>
#include "headfolder/addnumber.h"
using namespace std;

int main()
{
	int a, b;
	
	cout<<"a = ";
	cin>>a;
	cout<<"b = ";
	cin>>b;
	cout<<a<<" + "<<b<<" = "<<addFunction(a,b)<<endl;
	return 0;
}
