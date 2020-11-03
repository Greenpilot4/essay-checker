import string 
import sys

# Check for arguments
argv = sys.argv
if len(argv) == 1:
  print("Usuage: python main.py file")
  quit()

text = open(argv[1], "r") 

# Create word lists
dwlist = ['so', 'fun', 'cute', 'really', 'things', 'interesting', 'very', 'nice', 'good', 'great', 'dumb', 'boring', 'exciting', 'neat', 'a lot', 'alot', 'stuff', 'awesome']
bvlist = ['is', 'was', 'were', 'am', 'are', 'be', 'being', 'been']

# Create an empty dictionary 
d = dict() 
b = dict()

# Loop through each line of the file 
for line in text: 
	# Remove the leading spaces and newline character 
	line = line.strip() 

	# Convert the characters in line to 
	# lowercase to avoid case mismatch 
	line = line.lower() 

	# Remove the punctuation marks from the line 
	line = line.translate(line.maketrans("", "", string.punctuation)) 

	# Split the line into words 
	words = line.split(" ") 

	# Iterate over each word in line 
	for word in words: 
		# Check if the word is already in dictionary 
		if word in d: 
			# Increment count of word by 1 
			d[word] = d[word] + 1
		elif word in dwlist: 
			# Add the word to dictionary with count 1 
			d[word] = 1
			
	# Iterate over each word in line 
	for word in words: 
		# Check if the word is already in dictionary 
		if word in b: 
			# Increment count of word by 1 
			b[word] = b[word] + 1
		elif word in bvlist: 
			# Add the word to dictionary with count 1 
			b[word] = 1

# Print the contents of dictionary 
if d:
  print("Dead words")
  for key in list(d.keys()):
    print(key, ":", d[key])
  print("Total dead words: ", sum(d.values()))
else:
  print("No dead words found.")

if b:
  print("\nBe verbs")
  for key in list(b.keys()):
    print(key, ":", b[key])
  print("Total be verbs: ", sum(b.values()))
else:
  print("No be verbs found.")
