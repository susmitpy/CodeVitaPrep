"""
How to Execute : 
python3 constellation.py < const.txt 
python3 constellation.py < const1.txt 
"""

N = int(input())
INPUT = [list(input().split(" ")) for i in range(3)]

final_output = ""

def get_str_repr(window):
    return "".join(["".join([window[i][j] for i in range(3)]) for j in range(3)])

def get_last_star_found(last_star_found, window_start,letter):
    if letter == "I":
        return window_start + 1

    return window_start + 2
    

def process_window(window, window_start, last_star_found): 
    str_window = get_str_repr(window)
    is_in_last_star_window = window_start <= last_star_found

    if not is_in_last_star_window:

        if str_window == "*********":
            return "E"

        if str_window == "****.****":
            return "O"

        if str_window == "***..****":
            return "U"

        if str_window == ".****..**":
            return "A"

        if str_window == "*.*****.*":
            return "I"

    if str_window[-3:] == "###":
        return "#"

    return ""

last_star_found = -5

for window_start in range(N-2):
    window = (
        [
            INPUT[i][window_start:window_start+3] for i in range(3)
        ]
    )

    letter = process_window(window, window_start, last_star_found)
    if letter != "":
        last_star_found = get_last_star_found(last_star_found, window_start, letter)

    final_output += letter

print(final_output)