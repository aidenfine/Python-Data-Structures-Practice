# most simple 
class Tweet:
    pass

# calling the class
a = Tweet()
b = Tweet()
 
a.message = "Hello, World! "
b.message = "not the same"



print(a.message) # output -> "Hello, World!"
print(b.message) # output -> "not the same"

class Send:
    def __init__(self):
        print("Hello")

a = Send() # output -> "Hello"


class Trumpet():
    def __init__(self, sound):
        self.x = sound

a = Trumpet() # THROWS ERROR 

a = Trumpet("Something here")

print(a.x)
# output --> "something here"

b = Trumpet("Peace")
print(b.x) #  output -- > Peace 