list=[]
list.append('toyota')
print(list)
list.append('benz')
list.append('cherry')
print(list)
list.append('mitsub')
list.append('bmw')
list.append('rollsroyce')
list.append('tata')
list.append('subaru')
list.append('nissan')
list.append('tesla')
print(list)
print(len(list))
list.pop()
print(list)
num=[]
num.append(12)
num.append(15)
num.append(23)
num.append(100)
num.append(123)
print(num)
list.extend(num)
print(list)
list.pop(3)
print(list)
list.remove('tata')
print(list)
list.reverse()
print(list)
pos=list.copy()
print(pos)
posi=pos.index(15)
print(posi)
pos.append('jaguar')
print(pos)
pos.append('jaguar')
print(pos)
ho=pos.count('jaguar')
print('number of times jaguar printed:',ho)
