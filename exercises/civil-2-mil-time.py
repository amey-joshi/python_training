#!/bin/python

def to_military(t):
    portion = t[len(t) - 2:]
    rest = t[0:len(t) - 2]
    other = rest[2:]       

    if portion == 'PM':
        hours = int(rest[0:2])
        if hours != 12:
            rest = str((hours + 12) % 24) + other
    else:
        hours = int(rest[0:2])
        if hours == 12:
            rest = "00" + other

    return rest

def main():
    t = input().rstrip()
    print(to_military(t))

if __name__ == '__main__':
    main()
