# Assignment

**Name:** Mumandam Frank Randy Teneng  
**Matriculation Number:** 520225  
**Department:** Software Engineering  

---

# Question 1: Tree Traversals

```cpp
#include <iostream>
using namespace std;

class TreeNode{
public:
    int data;
    TreeNode *lchild, *rchild;

    TreeNode(int value){
        data = value;
        lchild = nullptr;
        rchild = nullptr;
    }
};

void showInorder(TreeNode* treeRoot){
    if(treeRoot != nullptr){
        showInorder(treeRoot->lchild);
        cout << treeRoot->data << " ";
        showInorder(treeRoot->rchild);
    }
}

void showPreorder(TreeNode* treeRoot){
    if(treeRoot != nullptr){
        cout << treeRoot->data << " ";
        showPreorder(treeRoot->lchild);
        showPreorder(treeRoot->rchild);
    }
}

void showPostorder(TreeNode* treeRoot){
    if(treeRoot != nullptr){
        showPostorder(treeRoot->lchild);
        showPostorder(treeRoot->rchild);
        cout << treeRoot->data << " ";
    }
}

int main(){
    TreeNode* treeRoot = new TreeNode(50);
    treeRoot->lchild = new TreeNode(25);
    treeRoot->rchild = new TreeNode(75);

    return 0;
}
```

# Question 2: Merging Binomial Trees

```cpp
#include <iostream>
using namespace std;

class BinomialNode{
public:
    int value;
    BinomialNode *childNode, *nextSibling;

    BinomialNode(int x){
        value = x;
        childNode = nextSibling = nullptr;
    }
};

BinomialNode* combineTrees(BinomialNode* firstTree, BinomialNode* secondTree){
    if(firstTree->value > secondTree->value)
        swap(firstTree, secondTree);

    secondTree->nextSibling = firstTree->childNode;
    firstTree->childNode = secondTree;

    return firstTree;
}
```

# Question 3: Search Key in BST

```cpp
bool searchElement(TreeNode* treeRoot, int targetValue){
    if(treeRoot == nullptr)
        return false;

    if(treeRoot->data == targetValue)
        return true;

    if(targetValue < treeRoot->data)
        return searchElement(treeRoot->lchild, targetValue);

    return searchElement(treeRoot->rchild, targetValue);
}
```

# Question 4: Insert into BST

```cpp
TreeNode* addElement(TreeNode* treeRoot, int valueToInsert){
    if(treeRoot == nullptr)
        return new TreeNode(valueToInsert);

    if(valueToInsert < treeRoot->data)
        treeRoot->lchild = addElement(treeRoot->lchild, valueToInsert);
    else
        treeRoot->rchild = addElement(treeRoot->rchild, valueToInsert);

    return treeRoot;
}
```

# Question 5: Maximum Key in BST

```cpp
int getLargest(TreeNode* treeRoot){
    TreeNode* currentNode = treeRoot;

    while(currentNode->rchild != nullptr)
        currentNode = currentNode->rchild;

    return currentNode->data;
}
```

# Question 6: Minimum Key in BST

```cpp
int getSmallest(TreeNode* treeRoot){
    TreeNode* currentNode = treeRoot;

    while(currentNode->lchild != nullptr)
        currentNode = currentNode->lchild;

    return currentNode->data;
}
```

# Question 7: Delete an Element from BST

```cpp
TreeNode* deleteElement(TreeNode* treeRoot, int valueToDelete){

    if(treeRoot == nullptr)
        return nullptr;

    if(valueToDelete < treeRoot->data)
        treeRoot->lchild = deleteElement(treeRoot->lchild, valueToDelete);

    else if(valueToDelete > treeRoot->data)
        treeRoot->rchild = deleteElement(treeRoot->rchild, valueToDelete);

    else{
        if(treeRoot->lchild == nullptr)
            return treeRoot->rchild;

        if(treeRoot->rchild == nullptr)
            return treeRoot->lchild;
    }

    return treeRoot;
}
```
