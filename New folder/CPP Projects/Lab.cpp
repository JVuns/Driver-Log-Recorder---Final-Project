#include <iostream>
using namespace std;

int main()
{
//	1st
	int n;
	cout<<"Enter an integer: ";
	cin>>n;
	cout<<endl<<n;
	
	if (n >= 0 )
	{
		cout<<"Good";
	}
	else
	{
		cout<<"bad";	
	}
	
//	2nd
	(n >= 0)? cout<<"Good":cout<<"Bad";	
	
//	3rd
	cout<<n<<((n%2 == 0)) ? "Good":"Bad";
	
//	Loop
	for (n = 1; n<10; n++)
	cout<<n<<endl;
	
//	while loop
	while(n	<10)
	cout<<n;
//	2nd
	do {
		cout<<"a";
	}while(n<20);

}
