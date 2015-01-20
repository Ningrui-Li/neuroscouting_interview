interview_tree_py
=================
The assignment info can be found in `interview_tree_py.txt`.

The script for generating this tree can be found in `interview_tree.py`.

An example of running this script:
`python interview_tree.py --levels 5 --output tree_level5.txt`

This will create the text file `tree_level5.txt` in the CWD containing a tree with 5 levels.

### How it works
The script was divided into 3 main steps:
1. Parsing command line arguments for the number of levels in the tree as well as the output file name.
2. Creating the node values in the tree based on the specified number of levels.
3. Writing the tree node values to a text file.

More information about each step can be found below.

#### Parsing command line arguments
The number of levels was the most essential input argument to this script. The only constraint was that it had to be a positive integer. The second argument was the name of the output text file. I made this more robust by checking for and removing any file name characters that were illegal (in Windows). I chose to print the output to a text file as opposed to printing the tree out on the console. This was because I was afraid that for large trees, some levels would span multiple lines, making the tree extremely messy and difficult to interpret.

#### Making the tree
The function `makeTree` was responsible for generating the tree. It took a single input argument: the number of levels in the tree. The function uses a nested for loop to iterate through each node in each element. The root node has value 1. In addition, the leftmost and rightmost nodes of each level also have value 1. This is because the leftmost node in each level gets its value from the sum of its parent as well as the parent's left sibling. However, the leftmost node of each level has a parent that is also the leftmost node of its level, so the parent does not have a left sibling. Thus, the leftmost node has the same value as its parent. This is also true for the rightmost nodes. Thus, all leftmost nodes and all rightmost nodes will have the same value as the root node, which is 1. 

In order to get the value for each non-root node, I looked for a quick way to get the value of its parent as well as the values of its parent's siblings. I decided to use a heap-like array structure for storing the string because it was fairly simple to index into the value of the parent node as well as the nodes adjacent to the parent. Since the first index of a heap-like array is unused, the index of the parent of a node located in index N of the array is N / 2. For example, the root node will be located at index 1 of the tree array, since the node located at the zeroth index is unused. In the second level, the two children of the root node will be located in index 2 and 3 of the array. In order to get the index of their parent, we can simply do division to get 2 / 2 = 1 and 3 / 2 = 1.5, which becomes floored to a 1, since it is an integer. After calculating the index of a node's parent node, the parent's siblings are simply located in the indices adjacent to the parent node. As long as a node at index N is not the leftmost or rightmost node in a level, its parent's left sibling will be located in index N/2 - 1 and its parent's right sibling will be located in index N/2 + 1. Thus, the tree can be generated iteratively following these steps.

After making the tree, the function makeTree returns a 1D integer array containing the values at each node.

#### Writing the tree
The function `printTree` takes in the 1D integer array created by `makeTree` as well as the output text file name as input arguments. Its purpose is to create a text file containing a visualization of the generated tree in the current working directory.

The nodes in each value are read level by level. Each level is printed on separate lines. There was an attempt to make the trees look fancy by adding variable amount of whitespace as well as forward and backward slashes to represent branches, but this system broke down for trees with 6 levels. This happened because some of the numbers had more than one digit, which threw off the spacing between numbers.