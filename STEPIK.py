# def only_one_positive(*args):
#     if args == ():
#         return False
#     s = 0
#     for i in args:
#         if i > 0:
#             s += 1
#     if s == 1:
#         return True
#     else:
#         return False
#
#
# print(only_one_positive())

# st = 'Create a list of the first letters of every word in this string'
# a = [i[0] for i in st.split() if len(i) > 1]
# print(a)

# from string import ascii_uppercase
# a = ascii_uppercase
# n = int(input())
# m = [i * (a.find(i) + 1) for i in a]
# print(m[:n])

# phrase = 'Take only the words that start with t in this sentence'
# a = [i for i in phrase.split() if i[0] == 't' or i[0] == 'T']
# print(a)
