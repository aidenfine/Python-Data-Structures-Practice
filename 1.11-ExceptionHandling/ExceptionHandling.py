import math

num = -212
try:
    print(math.sqrt(num))
except:
    print("error")
    print("")

if num < 0:
    raise RuntimeError("cant use neg number")
else:
    print(math.sqrt(num))