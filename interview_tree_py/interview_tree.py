import sys
import math
    
def main():
    # read in CLI arguments
    args = parse_cli()
    # basic error checking
    if args.numLevels <= 0:
      sys.exit("ERROR: Number of levels must be a positive integer.")
    if args.outputFile != makeValidFileName(args.outputFile):
      print "File name contained illegal characters, which were removed."
      print "%s was changed to %s" % (args.outputFile, makeValidFileName(args.outputFile))
      args.outputFile = makeValidFileName(args.outputFile)
    
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

def makeValidFileName(fileName):
    import string
    
    validChars = string.ascii_letters + string.digits + "._-@#$%^&()"
    validFileName = ''
    for char in fileName:
        if char in validChars:
            validFileName += char
    return validFileName
    
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
        # levelFirstIndex is also the number of nodes in the current level.
        levelFirstIndex = pow(2, level-1)
        
        # The tree is symmetric, so we actually only need to calculate node values 
        # for half the nodes in a level, since  the other half can be found by just
        # reflecting this half. 
        halfNumNodesInLevel = int(math.ceil(levelFirstIndex/2.))
        for levelIndex in range(0, halfNumNodesInLevel):
            # Iterate through each index in the row.
            if level == 1:
            # Base case, root node holds value of 1
                treeArray[1] = 1
            else:
                # currentIndex contains index of node we are currently calculating the value for
                currentIndex = levelIndex + levelFirstIndex
                # complementIndex contains index of node of the current node reflected across the tree
                complementIndex = 2*levelFirstIndex-levelIndex-1
                
                if (levelIndex == 0) or (levelIndex == pow(2, level-1)-1):
                    # If leftmost node or rightmost node of a level, the node value located there
                    # must be 1 because its parent must also be a leftmost or rightmost node, respectively.
                    treeArray[currentIndex] = 1
                    treeArray[currentIndex]
                elif (levelIndex % 2 == 1):
                    # If index of the node is odd, then it is a right child, so the value there
                    # should be the sum of its parent node and the node to the right of the parent.
                    
                    # Value of child node   =   value of parent node    + value of node to right of parent
                    treeArray[currentIndex] = treeArray[currentIndex/2] + treeArray[(currentIndex/2)+1]
                else:
                    # If index of the node is even, then it is a left child, so the value there
                    # should be the sum of its parent node and the node to the left of the parent.
                    
                    # Value of child node   =   value of parent node    + value of node to left of parent
                    treeArray[currentIndex] = treeArray[currentIndex/2] + treeArray[(currentIndex/2)-1]
                
                # Don't need to compute all nodes in this level, since we can just reflect it.
                treeArray[complementIndex] = treeArray[currentIndex]
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
    treeFile = open(outputFileName, 'w')
    print "Writing tree to " + outputFileName
    
    numLevels = int(math.log(len(treeArray), 2))
    charsPerNode = len(str(max(treeArray))) # number of digits in largest integer in tree
    
    # total number of characters per line
    maxNumNodesPerLevel = pow(2, numLevels-1) # lowest tree level has the max number of nodes per line
    charsBetweenNodes = 3*charsPerNode*maxNumNodesPerLevel-1 # amount of whitespace separation between
                                                             # node chunks
    
    for level in range(1, numLevels+1):            
        # Loop through each tree level.
        
        # charsBetweenNodes is used to determine the amount of whitespace between
        # node values in the printed tree. As the depth of the tree increases, there
        # is less whitespace between each node.
        if level == numLevels:
            charsBetweenNodes = 1;
        else:    
            charsBetweenNodes = charsBetweenNodes / 2;
            
        # levelFirstIndex is the array index in treeArray where the first node value of that
        # level is located.
        levelFirstIndex = pow(2, level-1)
        
        # levelString contains the node values
        levelString = ''
        # connectorString contains the branches/connections ('/' and '\') between node values
        connectorString = ''

        for levelIndex in range(pow(2, level-1)):
            # Loop through each node in the current level and concatenate each
            # node value to a simple string, with node values separated by spaces.
            currentIndex = levelFirstIndex + levelIndex;
            
            # nodeVal is the current node value converted to a string and padded with whitespace
            # such that it is the same length as the number in the tree with the most digits.
            nodeVal = '{val: <{spacing}}'.format(val=str(treeArray[currentIndex]), spacing=str(charsPerNode))            
            if level == numLevels:
                # The deepest level is a special case because there is no whitespace before the 
                # first node value.
                
                # The amount of whitespace between nodes with the same parent is 3*charsPerNode
                # because as the number of digits in the largest tree value increases, the parent node
                # and the two child nodes will both get one more digit/whitespace padding, increasing
                # the spacing by 3 characters.
                if levelIndex % 2 == 0:
                    # Whitespace between child nodes w/ same parent node
                    levelString += nodeVal + ' '*(3*charsPerNode)
                else:
                    # Whitespace between child nodes w/ different parent nodes
                    levelString += nodeVal + ' '*charsPerNode
            else:
                # In all other levels, the spacing between nodes is more predictable.
                levelString += ' '*(charsBetweenNodes) + nodeVal + ' '*(charsBetweenNodes+2-charsPerNode)
                # connectorString places slashes on the characters right before and after each node location
                connectorString += ' '*(charsBetweenNodes-1) + '/ \\' + ' '*(charsBetweenNodes)
        
        treeFile.write(levelString+'\n') 
        treeFile.write(connectorString+'\n')

    treeFile.close()
    
main()