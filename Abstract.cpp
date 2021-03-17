#include <iostream>
using namespace std;

class shape
{
	public:
		virtual int getArea() = 0;
		void setWidth(int w)
		{
			width = w;
		}
		void setHeight(int h)
		{
			height = h;
		}
	protected:
		int width;
		int height;
};

class Rectangle: public shape
{
	public:
		int getArea():
		return(width * height);
};

class Triangle(): public shape
{
	public:
		int getArea():
		return((width*height)/2)
}

};

int main()
{
	return 0
	Rectangle rect;
	
	rect.setWidth(3);
	rect.setHeight(8);
	
	cout<<"Rect area: "<< rect.getArea()<<endl;
	
	Traingle tri;
	
	tri.setWidth(3);
	tri.setHeight(8);
	
	cout<<"Rect area: "<< tri.getArea()<<endl;
	
}
