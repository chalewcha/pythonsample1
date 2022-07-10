#identity operators
#are used to compare the objects, not if they are equal, but if they are actually the same objiect with same memory location
#is and is not
#let me see an example
list1=['chalew, shamero']
list2=['chalew, shamero']
list3=list1
print('returns false b/c list1 is not the same object with lists',list1 is list2)
print('returns true b/c list1 is the same object as list3',list1 is list3)
print(list1==list2)
print(list1 is not list3)
print(list1 is not list2)
print(list1!=list3)


#membership opretors
#in and not in
#simple note
familiy=['chalew, shamero, etagegn, tsion, bani, tesfu, amen, wbit']
print('lemlem' in familiy)
print('chalew' in familiy)
print('lemlem' not in familiy )


#simple example for str
a=' chalew shamero shanka etagen kuku tesfu !!!!!!!!!!! '
print(a)
print(len(a))
print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace('chalew', 'lemlem'))
print(a.split(','))


#if...elif...else
#conditional 
name=input('enter your name\t')
print(name)
mark = int(input('enter your grade'+" "))
if mark>90:
    grade='a'
elif mark>80:
    grdae='B'
elif mark>70:
    grade='c'
elif mark>60:
    grade='d'
else:
    grade='f'
print(grade)



#Loop
#there are 2 types of loops while and for 
#let me show an example
n=1
while n<10:
    print(n)
    n+=1
#example 2
s=1
while s<100:
    print(s)
    s+=1
    if s==50:
        break
#example 3
num=1
while num<10:
    print(num)
    num+=1
else:
    print('it is 10')
  

#for loop

