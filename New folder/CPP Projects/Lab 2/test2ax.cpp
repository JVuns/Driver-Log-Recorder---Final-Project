#include <iostream>
using namespace std;

class printMe
{
	public:
	void abc(int x)
	{
		cout<<"First abc - value of x is "<<x<<endl;
	}
	void abc(double x)
	{
		cout<<"Second abc - value of x is"<<x<<endl;
	}
	void abc(int x, int y)
	{
		cout<<"Third abc - value of x and y is"<<x<<" and "<<y<<endl;
	}
};

int main()
{
	printMe hihohiho;
	hihohiho.abc(5);
	hihohiho.abc(1.234);
	hihohiho.abc(3, 9);
	
	return 0;
}
