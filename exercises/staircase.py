#!/bin/python

def staircase(n):
    lines = []
    last_line = '#' * n

    for i in range(n):
        lines.append(last_line.replace('#', ' ', i))

    lines.reverse()
    return lines

def main():
    n = int(input().strip())
    lines = staircase(n)
    for l in lines:
        print(l)

if __name__ == '__main__':
    main()


