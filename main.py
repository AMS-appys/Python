arr = ["A","N",1,1,1,2,3,3,3,"A","N"]
dict = {}

for element in arr:
  if element in dict:
    dict[element]+=1
  else:
    dict[element]=1

for key , value in dict.items():
  print(key,":",value)