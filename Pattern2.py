# Pattern 2
#   A
#   B C
#   D E F
#   G H I J
#   K L M N O

ch = 65
j = 1
for i in range(5):
    for k in range(j):
        print(chr(ch),end="")
		ch += 1
	j += 1
	print()