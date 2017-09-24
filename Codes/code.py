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

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')
print(len(b'ABC'))
print(len('ABC'.encode('ascii')))
print(len('中文'.encode('utf-8')))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('ABC'))
print(len('中文'))
print('Hello, %s %d years' % ('world', 10000))
print('Hello, {:s} {:d} years'.format('world', 10000))
print('{:2d}-{:02d}'.format(3, 1))
print('{:.2f}'.format(3.1415926))
print('Age: {:d}. Gender: {:s}'.format(25, 'Male'))
print('growth rate: {:d}%'.format(7))
print('{:.1f}%'.format((85-72)/72*100))