#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	char a[100];
	printf("Input day here: ");
	scanf("%s",&a);
	if (a == "Weekday") {
		printf("Im studying");
	}
	else if (a == "Weekend") {
		printf("Im going fishing");
	}
	else {
		printf("Invalid");
		printf(a);
	}
	return 0;
}

