#Using IS and IS NOT identity operator
a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a
d = b
if c is a:
    print('1. True')
if d is b:
    print('2. True')
if a is not b:
    print('3. True')
    
#Using IN and NOT IN membership operator
e = 'Hello World'
f = 'hell'
g = 'world'
h = 'World'
if f in e:
    print('4. True')
else:
    print('4. False')
if g not in e:
    print('5. True')
else:
    print('5. False')
if h in e:
    print('6. True') 
else:
    print('6. False')