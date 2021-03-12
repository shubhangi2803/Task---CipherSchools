# Pattern 1
#      *
#     **
#    ***
#   ****
#  *****

for i in range(5):

    # For printing spaces
	for j in range(5-i-1):
		print(" ",end="")

    # For printing *
	for k in range(i+1):
		print("*",end="")
        
	print()