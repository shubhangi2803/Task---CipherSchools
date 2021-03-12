# Pattern 2
#   A
#   B C
#   D E F
#   G H I J
#   K L M N O

ch = 65 # ASCII Value of: 'a'
j = 1
for i in range(5):
    for k in range(j):
        # Printing alphabet
        print(chr(ch),end="")
        # Increasing the ASCII Value for next alphabet
		ch += 1
	j += 1
	print()