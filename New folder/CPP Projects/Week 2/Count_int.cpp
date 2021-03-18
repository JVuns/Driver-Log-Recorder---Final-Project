#include <bits/stdc++.h>

#define SIZE(x) sizeof(x)* 8
using namespace std;

void printSignedRange(int count)
{
	int min = pow(2, count - 1);
	int max = pow(2, count - 1) - 1;
	
	printf("%d to %d\n", min * (-1), max);
}

void printUnsignedRange(int count)
{
	unsigned int max = pow(2, count) - 1;
	cout << "0 to "<<max<<endl;
}

int main()
{
	cout << "Size of int = " << sizeof(int)<<"Bytes"<<endl;
	cout << "Signed int = ";
	printSignedRange(SIZE(int));
	cout << "Signed int = ";
	printUnsignedRange(SIZE(unsigned int));
	cout << "Size of unsigned int = " << sizeof(unsigned int)<<"Bytes"<<endl;
	//A data structure that store key value of an array
	//A hierarchical data structure with nodes and child nodes
	//A hierarchical data structure similar to trees that is completely binary
	//A data structure with nodes that have connection/edge with other nodes
}
