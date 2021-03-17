#include <iostream>	
#include <map>
using namespace std;

//roman-number converter (1-9999)

class characterconv
{
	public:
	string number(int x)
	{
		cout<<"Enter your number: ";
		int inpnum;
		cin>>inpnum;
		cout<<"Converting number into roman...";
		//converting number to roman
		string roman[] = {"M", "CM", "D", "CD","C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
		int integer[] = {1000 ,900, 500 ,400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
		string conversion = "";
		for (int i = 0; i < 13; i++) 
		{
			while (inpnum - integer[i] >= 0) 
				{
				conversion += roman[i];
				inpnum -= integer[i];
				}
		}
		cout << conversion;
	}

};

int main()
{
	characterconv charconv;
	cout<<"Choose an option: \n(1)Decimal to Roman\n(2)Roman to decimal\n";
	int a;
	int abc[4]{1,2,3,4};
	cout<<abc;
	cin>>a;
	if(a == 1)
	{
	charconv.number(a);
	}
	{
	cout<<"Invalid input";
	}
};
