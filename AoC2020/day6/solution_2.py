"""
--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

- In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
- In the second group, there is no question to which everyone answered "yes".
- In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
- In the fourth group, everyone answered yes to only 1 question, a.
- In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

Your puzzle answer was 3406.


Create an alphabet set and find the intersection between that base set with the answers set created in the previous solution. 
Count the len of the intersection and add it all up.
"""
count = 0
alpha_set = set(map(chr, range(97, 123)))
with open('input.txt', 'r') as input_file:
    arr = input_file.read().splitlines()
    arr.append("") # Add this line so the last group gets read correctly.
    group = ""
    for line in arr:
        if line != "":
            alpha_set = set(line.strip("\n")).intersection(alpha_set)
            group += line.strip("\n")
        else:
            count += len(alpha_set)
            alpha_set = set(map(chr, range(97, 123)))
            group = ""

print(f'Solution: {count}')
