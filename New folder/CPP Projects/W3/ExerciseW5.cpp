#include <iostream>
#include <stdlib.h>

struct Node
{
	struct Node* par = NULL;
	struct Node* left = NULL;
	struct Node* right = NULL;
};

void addRoot()
{
	struct Node* root = "Parent";
	root->left = "C1";
    root->right = "C2";
}

void ExpanExternal()
{
    root->left->left = new Node(4);
    root->left->right = new Node(4);
}

class LinkedBinaryTree { 
   public:
      LinkedBinaryTree(); // constructor
       int size() const; // number of nodes
       bool empty() const; // is tree empty?
       Position getRoot() const; // get the root
       PositionList positions(int) const; // list of nodes
       void addRoot(); // add root to empty tree
       void expandExternal(const Position& p); // expand external node
       Position removeAboveExternal(const Position& p); // remove p and parent
       void preorder(Node* v, PositionList& pl) const; // preorder utility 
       void inorder(Node* v, PositionList& pl) const; // inorder utility
       void postorder(Node* v, PositionList& pl) const; // postorder utility
       // NOTE: housekeeping functions such as destructor, copy constructor and 
       // assignment operator are omitted
   
   private:
       Node* root; // pointer to the root
       int n; // number of nodes
};
