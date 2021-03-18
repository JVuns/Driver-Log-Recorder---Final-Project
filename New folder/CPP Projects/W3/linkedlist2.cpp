#include <iostream>
#include <stdlib.h>

struct Node
{
	int data;
	struct Node*next;
};

void printList(struct Node *n)
{
	while(n!=NULL)
	{
		printf(" %d", n->data);
		n= n->next;
	}
}


