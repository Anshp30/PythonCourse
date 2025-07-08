# Two Types Of Modules in Python:
# -Built in Modules
# -External Modules
# Built in Modules in python https://docs.python.org/3/py-modindex.html

import math
import mymodules
import requests

print(math.sqrt(16))
mymodules.hello()
r = requests.get("https://www.google.com")
print(r.text)