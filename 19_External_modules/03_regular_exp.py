import re
text = "The quick brown fox jumps over the lazy dog"

match = re.search("brown",text)

# print(match)

# Serach for pattern
# if match:
#     print("Match found")
#     print("start index:",match.start())
#     print("end index:",match.end()) 

# Find all occurence of pattern
matches = re.findall("the",text,re.IGNORECASE) # caseinsensitive serach
print("matches:",matches)

#Replace a pattern 
new = re.sub("fox","Tiger",text)
print("Repace Pattern:",new)