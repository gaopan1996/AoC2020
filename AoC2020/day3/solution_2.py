"""
--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

Your puzzle answer was 3772314000.


Take the concept of the previous solution but put it in a method. Make sure to get go down y lines by skipping if the line number isn't modulo.
"""
def traverseMap(x,y):
    treeCount = 0
    index1, index2 = [0,0]
    with open('input.txt', 'r') as input_file:
        arr = input_file.read().splitlines()
        lineLength = len(arr[0])
        for line in arr:
            if index2%y == 0:
                if line[index1%lineLength] == '#':
                    treeCount += 1
                index1 += x
            index2 += 1
    return treeCount
trees = traverseMap(1,1)*traverseMap(3,1)*traverseMap(5,1)*traverseMap(7,1)*traverseMap(1,2)

print(f'Solution: {trees}')
