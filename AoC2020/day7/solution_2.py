"""
--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

- faded blue bags contain 0 other bags.
- dotted black bags contain 0 other bags.
- vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
- dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?

Your puzzle answer was 85324.

Copy graph creation code from previous solution. Add numbers into tuples to determine how many bags of each kind you must have.
Go through each neighbouring node with DFS.

Add the new count to the previous count.


"""

import re, pprint
from itertools import groupby
def recursive_dfs(graph, source,path = []):

    count = 0
    for neighbour in graph[source]:
        print(neighbour)
        print(f"Count: {neighbour[0]}. Source: {source}. Neighbour: {neighbour[1]} - {graph[neighbour[1]]}.")
        count = count + int(neighbour[0]) * (recursive_dfs(graph, neighbour[1], path) + 1)
        path.append(neighbour[1])
    return count

graph = {}
with open('input.txt', "r") as input_file:
    arr = input_file.read().splitlines()
    for line in arr:
        parsedLine1 = re.split(' bags* *\.*| *contain |, ', line)
        lineList = [elem.strip() for elem in parsedLine1 if elem.strip() and elem != "no other"]
        parsedList = [''.join(j).strip() for elem in lineList[1:] for k,j in groupby(elem, str.isdigit)] 
        it = iter(parsedList)
        graph[lineList[0]] = list(zip(it, it))

count = recursive_dfs(graph, "shiny gold")
pprint.pprint(graph)
print(f"Solution: {count}")
