str='hello this is new era of human being'
#capitalize() method by using this first character of string convert to upper case
capital=str.capitalize()
print(capital)
# casefold() method by using it it will convert whole string in small letter or lower case
str_low='HELLO WORLD '
low=str_low.casefold()
print(low)
#center() by using this method string will place in center
str_center='this is an apple'
p=str_center.center(20)
print(p)
#count() this method count the number of occurrance of a particular value
str_count='this si new paragraph of my file'
c=str_count.count('a')
print(c)
#title() this method is used to make every word of string capital
str_title='this is my title method '
t=str_title.title()
print(t)
 #pattern in python
for i in range(5):
    for j  in range(i):
        print(j+1,end=' ')
    print()
for i in range(5):
    for j  in range(i):
        print(end=' ')
    print()
str='hello world'
print(str)
str1="hello world"
print(str1)
str2="""hello world"""
print(str2)
str3='''hello world'''
print(str3)