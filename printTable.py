def printtable(table):
    colwid=[0]*len(table)
    for col in range(len(table)):
        for row in table[col]:
            if colwid[col]<len(row):
                colwid[col]=len(row)
    for row in range(len(table[0])):
        for col in range(len(table)):
            print(table[col][row].rjust(colwid[col]),end='')
        print()

table=[
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
]
printtable(table)