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