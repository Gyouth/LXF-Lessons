# #to run the .py file directly on Linux/Mac
# #!/usr/bin/env python3
# #type the command: chmod a+x .py, in the terminal
# # print
# print("hello, world")
# #print a space at the comma between strings
# print("The quick brown box", "jumps over", "the lazy dog")
# print(300)
# print(100 + 200)
# print("100 + 200 = ", 100 + 200)
# #input
# name = input()
# print("hello", name)
# name = input("Please enter your name")
# print("hello", name)
# print("1024 * 768 = ", 1024*768)
# print("I\'m \"Ok\"")
# print("I\'m learing\nPython")
# print("\\\n\\")
# print('\\\t\\')
# print(r'\\\t\\')
# #input in multi-line
# print('line1' \
# 	', line2' \
# 	', line3')
# #input a multi-line string
# print('''line1,
# 	line2,
# 	line3''')

# PI = 3.14159265359
# print(10 / 3)
# print(9 / 3)
# print(10 // 3)
# print(10 % 3)

# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# print(n)
# print(f)
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# print(ord('A'))
# print(ord('中'))
# print(chr(66))
# print(chr(25991))
# print('\u4e2d\u6587')
# print(len(b'ABC'))
# print(len('ABC'.encode('ascii')))
# print(len('中文'.encode('utf-8')))
# print(b'ABC'.decode('ascii'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# print(len('ABC'))
# print(len('中文'))
# print('Hello, %s %d years' % ('world', 10000))
# print('Hello, {:s} {:d} years'.format('world', 10000))
# print('{:2d}-{:02d}'.format(3, 1))
# print('{:.2f}'.format(3.1415926))
# print('Age: {:d}. Gender: {:s}'.format(25, 'Male'))
# print('growth rate: {:d}%'.format(7))
# print('{:.1f}%'.format((85-72)/72*100))

# classmates = ['Michael', 'Bob', 'Tracy']
# print(classmates)
# print(len(classmates))
# print(classmates[0])
# print(classmates[1])
# print(classmates[2])
# print(classmates[-1])
# print(classmates[-2])
# print(classmates[-3])
# classmates.append('Adam')
# print(classmates)
# classmates.insert(1, 'Jack')
# print(classmates)
# classmates.pop()
# print(classmates)
# classmates.pop(1)
# print(classmates)
# classmates[1] = 'Sarah'
# print(classmates)
# L = ['Apple', 123, True]
# print(L)
# s = ['Python', 'Java', ['asp', 'php'], 'scheme']
# print(len(s))
# t = (1)
# print(t)
# t = (1,)
# print(t)
# t = ('a', 'b', ['A', 'B'])
# t[2][0] = 'X'
# t[2][1] = 'Y'
# print(t)
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
# 	print(name)

# sum = 0
# for x in range(101):
# 	sum = sum + x
# print(sum)


# sum = 0
# n = 99
# while n>0:
# 	sum = sum  + n
# 	n = n - 2
# 	# pass
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
# 	print('Hello, ', name)

# n = 1
# while n <= 100:
# 	if n > 10:
# 		break
# 	print(n)
# 	n = n + 1
# 	# pass


# n = 0
# while n < 10:
# 	n = n + 1
# 	if n % 2 == 0:
# 		continue
# 	# pass
# 	print(n)

# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'])
# d['Adam'] = 75
# d['Jack'] = 90
# d['Jack'] = 88
# # print(d)
# # b = 'Tomas' in d
# # print(b)
# print(d.get('Tomas', -1))
# d.pop('Bob')
# print(d)

# s = set([1, 2, 3])
# s = set([1, 1, 2, 3])
# s.add(4)
# s.remove(4)
# print(s)

# s1 = set([1, 2, 3])
# s2 = set([2, 3, 4])
# s_and = s1 & s2
# print(s_and)
# s_com = s1 | s2
# print(s_com)

a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)
