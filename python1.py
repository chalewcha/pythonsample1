'''print function :- to display on the screen
so this is simple explantion about print
'''
print('chalew')
print('chalew shamero')
print('chalew\tshamero')#\t for tab or spaceing
print('chalew\nshamero\nkuku')#\n for new line
print('chalew\tshamero\tshanka\tsheno\tkuku')
print('12\t13\t22\t43\t45')
print('12\t13\t22\t43\t45')
print('12\t13\t22\t43\t45')
print('12\t13\t22\t43\t45')
print('12\t13\t22\t43\t45')


#var(variable)
'''
var;- it is li a contener
it standes or asigin by alha numeric car or a-z and 0-9 and - or under score
it not start with number it starsts with letter or under score
let me show an example
'''
x="chalew"
print(x)
z=1
print(1)
_cha= 'chalew'
print(_cha)
num1=44
print(num1)
s='good'
print('food is\t' + s)
c=23
m=45
print(c+m)
print(c*m)
print(c/m)
print(c%m)
Num=23
name='chalew\n'
name2='chalew\t'
print(str(Num)+name)
print(Num*name)
print(Num*name2)
x,y,z,=12,13,14
print(x)
print(y)
print(z)
x=y=z=23
print(x)
print(y)
print(z)


#comment
'''it is not redeble part 
it expresed by has(#) and for multiple comment it used 3 double or single coutr on the up and bottom
it not display on the screen but when we asign the comment by var it is displayed and
read so one let me see an example
'''
x='''chalew
kuku
tesfu
eta
bani
tsion
bcha bzu
'''
print(x)


#Data Type
'''a type of data when that we store in a computer
there are so many data tyepes in python_branch
let me see some of the are'''
print('type\t\tdef')
print('text\t\tstr\nnumeric\t\tint,float,complex complex num are written with a "j" as the imaginary part\nsequence\t\tlis,tuple,range\nmapping\t\tdict\nset\t\tset,frozenset\nboolean\t\tbool\nbinary\t\tbytes,bytearry,memoryview')
'''there are 3 numeric type in python
-int
-flot
-str
let me show example
'''
x=23#int
s=-12222222#int
k=4327483278743284747284728#int
o=-35353354.7#flot
u=-56465634636j
p=-5353453j#complex
y=23.4#flot
z=23j#complex
l='chal!ew'
l2="chalew's book"
m=True
print('the type of the chalew is',type(l))
print('the type of the chalew book is',type(l2))
print('the type of the true is',type(m))
print('the type of the number is',type(x))
print('the type of the number is',type(y))
print('the type of the number is',type(z))
print('the type of the number is',type(k))
print('the type of the number is',type(o))
print('the type of the number is',type(p))
print('the type of the number is',type(u))
print('the type of the number is',type(s))


#Indentation simplie geba malet new
'''it expresed by (:) this 
when we see an example how to use
let me show 
'''
if(6==6):
    print('chalew')
    print('shamero')
    '''this is true agriment but in fals agrimnet the code is does not work
    #le me see in example
if(4==5):
   print('chalew')
   at this time it is not displayed or printed b/c it is false agriment
'''


#casting it mines change data type weym bamaregna data typeun mekeyer malet new
#show all examples
x=12
print('the orginal answer',x)
print(type(x))
print('casting int to flot', float(x))
print(type(float(x)))
print('casting int to complex', complex(x))
print(type(complex(x)))
y=12.111
print('the orginal answer', y)
print(type(y))
print('flot in to int', int(y))
print(type(int(y)))
print('flot in to complex', complex(y))
print(type(complex(y)))
z=22j
print('the orginal answer', z)
print('chalew shamero')
z=33333
s="chalew"
print('int in to str', str(z)+s)
print(type(str(z)))
x='32'
print('str in to int',int(x))
print(type(str(x)))
x=-23.23
print('flot in to str',str(x))
print(type(str(x)))
com=23j
print('complex in to str',str(com))
print(type(str(com)))
#there are so many examples so try it this is all about casting
#hint about ord and chr to know askiw value
print(ord('z'))#lezih chr snsetew number new miseten
print('bezih number represent yetederegew manew',chr(90))#ehe demo number snsetew chr new miseten


#short not about str
'''
string literals in python are surrounded by either single quotation marks or Double
you can assign a multiline string to a varivable by using three quote
strings are arrays
let me show some example 
'''
x='''chalew
shamero<>?":
kukusgdhshs3225425
and so this is multiple<>wet
str!!!!!!!!!!!
'''
print('this is multiple string',x)
x= '''
__________
|__c_|_c__|
|__d_|__d_|
|__x_|_x__|
|__g_|__g_|
'''
print('arryas malet coloxtion malet new yemnlew demo ehe new', x)
print('length yawetalnal',len(x))
print('ede array new mitayew',x[0:22])
print('bezih aynet meged substring mawtat echilalen',x[-22:-1])
#and to format or concatinate like this
x="your boobs is {} and yor age {}"
print('concatinate snaderg demo like bezih aynet meged new',x.format('bigg',23))











