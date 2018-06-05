# Note
## Insert sort
It is a little slow to write down the code.
Because I don't divide the system into several module and then write code.
The key mechanism is:
- Traversal the list, assume the first element is sorted
- For each element, compare it with the sorted list, and insert.
- when insert, find the right position, store the element to a variable, and move the sorted list from rear to front.

Dividing make things easier.

## Shell sort
Shell sort will just do the gap element sort the same as insert sort.

## Heap sort
Heap need:
- Write the heap adjust, adjust the root node value to the right position. If max heap, then root node value need to be
the max value. Use while to find the right location to its children. If min heap, the root node need to be the smallest.
- Build the heap. The concept of why: [heap sort](http://shmilyaw-hotmail-com.iteye.com/blog/1775868)
 我们注意到，前面虽然有一个堆调整的过程，但是这个过程主要针对的是一个树中的一个结点。如果树中间有多个结点不符合最大堆的条件，我们光调整某一个结点是没有用的。
 那么，就需要一个办法来将整棵树调整成符合条件的最大堆。 首先第一个问题，从哪个结点开始进行调整。我们来看这棵二叉树，很显然，它最后的一个元素也肯定就是最终的
 一个叶结点。那么取它的父结点应该就是有子结点的最大号的元素了。那么从它开始就是最合适的。取它的父结点可以通过一个简单的i / 2来得到，i为当前结点的下标。
```
public static void buildMaxHeap(int[] a)
{
    for(int i = a.length / 2; i >= 0; i--)
        maxHeapify(a, i);
}
```
- pop the element from the heap
Make the change from the end with 0, and then adjust the list from 0 to end-1, the end element is the most lagest one.