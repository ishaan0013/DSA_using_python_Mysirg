lst = [98, True, 98.9, 'Ishaan', 67, -9, 76.0, -98.9,
       {'Name': 'Ishaan', "Age": 16}, [12, 45, 78, 5], False, 'hello']

final_lst = []

for i in lst:
    if type(i) in (float, int):
        final_lst.append(i)

print(final_lst, sep=",")
# both ways are correct 👆 and 👇
[print(i, end=" ")for i in final_lst]
