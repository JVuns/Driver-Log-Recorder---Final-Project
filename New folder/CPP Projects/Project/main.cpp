#include <iostream>
#include "sum.h"
using namespace std;

int main()
{
	float a = 3.5, b = 4.5;
	cout<<"sum is :"<<sumFunction<float>(a,b)<<endl;	
	cout<<"sum is :"<<sumFunction<int>(a,b)<<endl;
}
