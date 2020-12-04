"""
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

Your puzzle answer was 176647680.

Same concept as the previous part, but an additional loop
"""
with open('input.txt') as input_file:
    lines = input_file.read().splitlines()
    count = 0
    while count < len(lines)-1:
        expense = lines[count]
        first_increment = count + 1
        while first_increment < len(lines): 
            expense_pair = lines[first_increment]
            expense_trio = 2020 - int(expense) - int(expense_pair)
            if str(expense_trio) in lines:
                print(f'Solution: {int(expense)*int(expense_pair)*expense_trio}')
                exit()
            first_increment += 1
        count += 1
