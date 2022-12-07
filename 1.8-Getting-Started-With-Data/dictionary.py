"""
unordered structure called a dictionary. Dictionaries are collections 
of associated pairs of items where each pair consists of a key 
and a value. This key-value pair is typically written as key:value. 
Dictionaries are written as comma-delimited key:value pairs enclosed in curly braces. 
"""


capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])

capitals['Utah']='SaltLakeCity'
print(capitals)
# {'Iowa': 'DesMoines', 'Wisconsin': 'Madison', 'Utah': 'SaltLakeCity'}

capitals['California']='Sacramento'
print(len(capitals))

for k in capitals:
    # loop that gets the capitals then prints the assigned state
   print(capitals[k]," is the capital of ", k)