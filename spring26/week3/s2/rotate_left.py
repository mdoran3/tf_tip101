def rotate_left(s, n):
    return s[n:] + s[:n]

s = "rotation"
print(rotate_left(s, 2))

# Example Output: tationro