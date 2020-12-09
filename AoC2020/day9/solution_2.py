"""
--- Part Two ---
The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?


Your puzzle answer was 209694133.

Use the code from last time. Loop through set of length n to find contiguousList that sums up to the invalid value.

"""

value = 0
count = 0
with open('input.txt', 'r') as input_file:
    arr = input_file.read().splitlines()
    xmas = []
    fullxmas = []
    for line in arr:
        fullxmas.append(int(line))
        if count < 25:
            xmas.append(int(line))
            count += 1
        else:
            potentialSum = int(line)
            index = 0
            for index in range(len(xmas)):
                if (potentialSum - xmas[index]) in xmas:
                    xmas = xmas[1:]
                    xmas.append(potentialSum)
                    break
                index += 1
            else:
                print(f'Found invalid value. {line}')
                for n in range(1,25):
                    for i in range(len(fullxmas)):
                        for j in range(i+n, len(fullxmas)):
                            if int(line) == sum(fullxmas[i:j]):
                                contiguousList = fullxmas[i:j]
                                contiguousList.sort()
                                print(f'Found list {contiguousList}. Encryption Weakness: {contiguousList[0] + contiguousList[len(contiguousList)-1]}')
                                
                                exit()


