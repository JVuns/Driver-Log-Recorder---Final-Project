#include <iostream>
using namespace std;

//one func for all data type
template <typename T>//int myMax(int x, int y)
T myMax(T x ,T y)
{
	return(x>y)?x:y; //the ? is an if true statement
}

int main()
{
	cout<<myMax<int>(1,4)<<endl;
	cout<<myMax<double>(5.1,4.3)<<endl;
	cout<<myMax<char>('s','m')<<endl;
}
