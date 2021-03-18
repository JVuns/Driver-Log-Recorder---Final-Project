#include <iostream>
#include <stdlib.h>

typedef string Elem;
struct Node
{
	Elem elt;
	Node* par;
	Node* left;
	Node* right;
};

class Position
{
	private:
		Node* v;
		
	public:
		//constructor
		position(Node*);
		
	//gel elem
	Elem& operator*();
	
	Position left() const;
	
	Position right() const;
	
	Position right() const;

	bool isRoot() const;
	
	bool isExternal() const;
};

