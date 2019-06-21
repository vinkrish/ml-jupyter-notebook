### Tree

A tree data structure can be defined recursively as a collection of nodes (starting at a root node), where each node is a data structure consisting of a value, together with a list of references to nodes (the "children"), with the constraints that no reference is duplicated, and none points to the root.

- Tree
- Parent
- Child
- Ancestors
- Descendants
- Sibling
- Height
- Degree
- Level
- Leaf Nodes
- Path Length

### Binary Tree

A data structure in which a record is linked to two successor records, usually referred to as the left branch when greater and the right when less than the previous record.

- max no of nodes on any level l is \(2^l\)
- max no of nodes for given height(h): \(2^h-1\)
- max no of nodes for whole tree: \(\sum_{l=0}^L 2^l = 2^h-1\) or \(\sum_{i}^h-1 2^i\)
- min no of nodes possible is h
- for n nodes, max height is n and min height is \(\lceil\log_2(n+1)\rceil\)
- \(e=n-1\) where e=no of edges
- \(n_0=n_2+1\) where \(n_0=\text{no of nodes with no child}\) and \(n_2=\text{no of nodes with 2 child}\)

$$n \le 2^h-1$$
$$2^h \ge n+1$$
$$h \ge \log_2(n+1)$$
$$h \ge \lceil\log_2(n+1)\rceil$$

$$n = n_0 + n_1 + n_2$$
