#include <iostream>
#include <string>
using namespace std;

class Larger {
	private:
		int first;
		int second;

	public:
		Larger();
		Larger(int f, int s);
		int getFirst();
		int getSecond();
		void setFirst(int f);
		void setSecond(int s);		
		int isLarger();	
};

// your code here
int larger::getFirst	


int main() {
	
	Larger l;
	int f, s;
	
	cout << "Enter first data " << endl;
	cin >> f;
	l.setFirst(f);
	
	cout << "Enter second data " << endl;
	cin >> s;
	l.setSecond(s);

		
	cout << "The larger of " << f << " and " << s << " is " << l.isLarger() << endl;

	return 0; 
}

