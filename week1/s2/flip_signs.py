def flip_sign(lst):
    return [-item for item in lst]

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)