def main():
    # read in CLI arguments
    args = parse_cli()
    # generate tree
    treeArray = makeTree(args.numLevels)
    # write tree to output file
    printTree(treeArray, args.outputFile)

def parse_cli():
    import argparse as ap

    par = ap.ArgumentParser(description="Generate rectilinear 3D mesh as "
                            "specified on the command line.",
                            formatter_class=ap.ArgumentDefaultsHelpFormatter)
    par.add_argument("--levels",
                     dest="numLevels",
                     help="number of tree levels that should be generated. should be a positive integer.",
                     type=int,
                     default=4)
    par.add_argument("--output",
                     dest="outputFile",
                     help="name of text file where the generated tree will be written",
                     default="tree.txt")

    args = par.parse_args()

    return args

def makeTree(numLevels):
    '''
    This function will generate a tree following the guidelines given in the assignment. The
    root node will always be 1. The left child node will contain the sum of the parent node's value and
    the value of the node to the left of the parent. If the parent is the leftmost node, then the left child
    node will just hold the same value held by its parent. The right child node will contain the sum of the
    parent node's value and the value of the node to the right of the parent. If the parent is the rightmost node, then the left child node will just hold the same value held by its parent. 
    
    Inputs:
    numLevels (int) - number of levels in the tree.
    
    Outputs:
    treeArray (1D int array) - 1D integer array representing the generated tree.
                               This array is organized like a heap, so the zeroth index is not used.
                               Index 1 holds root node value, indices 2-3 hold the second level nodes,
                               indices 4-7 hold the third level nodes, etc.
    '''
    # The tree will be represented using a 1D integer array that is organized like a heap. This makes it
    # easy to get a node's parent, as well as indexing into the nodes to the right and left of the parent.
    # For example, given a node at index N, the index of its parent is N/2. Assuming the parent is not
    # the leftmost or rightmost node, its siblings will be located at indices (N/2)-1 and (N/2)+1.
    
    # Pre-allocating space for the tree
    treeArray = [None] * pow(2, numLevels)
    # Note that the zeroth index is unused.
    treeArray[0] = 0
    
    for level in range(1, numLevels+1):
        # levelFirstIndex is the first array index of each level.
        # For example, the first (and only) index of level 1 is array index 1.
        # The array index of the first node in level 2 is array index 2.
        # The array index of the first node in level 3 is array index 4.
        # The array index of the first node in level N is array index 2^(N-1).
        levelFirstIndex = pow(2, level-1)
        for levelIndex in range(0, pow(2, level-1)):
            # Iterate through each index in the row.

            # Base case, root node holds value of 1
            if level == 1:
                treeArray.append(1)
            
            currentIndex = levelIndex + levelFirstIndex
            if (levelIndex == 0) or (levelIndex == pow(2, level-1)-1):
                treeArray[currentIndex] = 1
    
    return treeArray
    
def printTree(treeArray, outputFileName):
    '''
    This function will write the treeArray to a text file with the name given as a command line argument.
    
    Inputs: 
    treeArray (1D int array) - array holding the values of the tree
    outputFileName (String) - name of output text file
    
    Outputs:
    Text file with name outputFileName will be created in the CWD.
    '''
    print treeArray
    print "Writing tree to " + outputFileName
    
main()