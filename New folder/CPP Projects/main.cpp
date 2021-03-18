#include <iostream>
#include "addition.h"
#include "subtraction.h"
#include "multiplication.h"
#include "division.h"
using namespace std;

// declare function prototype
double add (double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);

// the main function
int main(){
	//declare variables
	double num1;
	double num2;
	int option;
	double result;
	
	// prompt for input
	cout << "Enter the first number " << endl;
	cin >> num1;
	
	cout << "Enter the second number " << endl;
	cin >> num2;
	
	cout << "What calculation you want to do?" << endl;
	cout << "Choose the following option:" << endl;
	cout << "choose 1: addition" << endl;
	cout << "choose 2: subtraction" << endl;
	cout << "choose 3: multiplication" << endl;
	cout << "choose 4: division" << endl;
	
	cin >> option;
	
	switch(option){
	case 1:
		cout<<"Result is :"<<add<float>(num1,num2);
		return 0;
	case 2:
		cout<<"Result is :"<<subtract<float>(num1,num2);
		return 0;
	case 3:
		cout<<"Result is :"<<multiply<float>(num1,num2);
		return 0;
	case 4:
		cout<<"Result is :"<<divide<float>(num1,num2);
		return 0;
	}



}

