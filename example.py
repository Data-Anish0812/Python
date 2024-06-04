data={"id":101, "name":"ajit", "branch":"comp",
      ("chem","phy","maths"):[85,95,88],
      "name":"suyash"}
print(type(data))
print(data)

data["perc"]=85.67
print(data)
data["branch"]:"it"
print(data)

d2={1:'a',2:"b",3:"C"}
data.update(d2)
print(data)

for num in data.items():
      print(num)
      
for key in data.keys():
      print(key)
      
      
d=("id":101,"name":sachin, "perc":78.23)
for value in d.values():
      print(value)