"""
--- Part Two ---
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?

Your puzzle answer was 548.


Take answer from previous part and put the seats in a dictionary and print it out. Manually scour the map for empty seat by process of elim. Calculate the SID.
"""
import pprint

def calculate_seat(seat_line):
    rows = seat_line[:7]
    columns = seat_line[7:]
    rowBinary = rows.replace("B","1").replace("F","0")
    columnBinary = columns.replace("R","1").replace("L","0")
    row = int(rowBinary,2)
    column = int(columnBinary,2)
    return row, column

with open('input.txt', "r") as input_file:
    arr = input_file.read().splitlines()
    flight_map = {k: [] for k in range(127)}
    for line in arr:
        row, column = calculate_seat(line)
        flight_map[row].append(column)

pprint.pprint(flight_map)

