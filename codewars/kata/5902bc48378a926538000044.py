# https://www.codewars.com/kata/5902bc48378a926538000044/train/python
# Given a string s of lowercase letters ('a' - 'z'), get the maximum distance between two same letters, and return this distance along with the letter that formed it.
# If there is more than one letter with the same maximum distance, return the one that appears in s first.
def dist_same_letter(st):
    print(st)
    last_index = {} #  charater:index pairs
    for i, ch in enumerate(st):
        last_index[ch] = i
         
    print(last_index)
    solution_character = ''
    solution_distance = -1
    for i, ch in enumerate(st):
        distance = last_index[ch] - i
        if distance > solution_distance:
            solution_distance = distance
            solution_character = ch

    return solution_character + str(solution_distance + 1)
    
# NOTE: I'm pretty sure whoever made this exersize doesn't understand how distances work
# like, for st="aa", the solution checker would expect result "a2" instead of "1"
# I added the 1 to the end so it would pass

