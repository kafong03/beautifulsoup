# Milestone-4

# Technical Brief
For Milestone 4, I implemented \_\_iter\_\_(self) in the BeautifulSoup class (bs4/\_\_init\_\_.py). You can find my additions in that file starting at line 548.
The iterable object that is generated allows for the user to traverse the BeautifulSoup object's nodes through a preorder depth-first search traversal without saving the whole document tree at once (per project requirements). Not only does this implementation save memory space [O(1) for the current node], but also allows for O(N) time complexity.

__\_\_iter\_\_(self) specifics__
__self.contents[0]__ provides the starting node
__current_node__ holds the node that is yielded to the user
__next_node__ holds the following node (PageElement.next_element) before current_node is yielded so that the iteration through the tree is not affected by any mutations.
Additionally, an empty list is returned in the case of there being an empty document.