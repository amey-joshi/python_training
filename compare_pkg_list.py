#!/usr/bin/python3

pip_set = set(line.strip() for line in open('piplist.txt'))
my_set = set(line.strip() for line in open('mylist.txt'))

mine_not_in_pip = my_set - pip_set
pip_not_in_mine = pip_set - my_set

print(f"There are {len(pip_set)} packages in pip list")
print(f"There are {len(my_set)} packages in my list")

print("#" * 80)
print("Packages in my list by not in pip's")
print("#" * 80)
for p in sorted(mine_not_in_pip):
    print(p)

print("#" * 80)
print("Packages in pip's list by not in mine")
print("#" * 80)
for p in sorted(pip_not_in_mine):
    print(p)

