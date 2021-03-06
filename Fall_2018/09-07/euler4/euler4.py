def Euler4():
    def IsPalindrome(s):
		return s[::-1] == s 			# Check if s stepped through backwards is the same as s
	largest = 0
	for i in range(100, 1000):			# Loop through all 3 digit numbers
		for j in range(100, 1000):		# Loop through all 3 digit numbers
			prod = i * j
			if IsPalindrome(str(prod)): 	# If the product is a palindrome
				if prod > largest: 	# And prod is bigger than our current largest product
					largest = prod 
	return largest
