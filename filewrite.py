def addlines(startline,endline):
    f = open('a.txt', "a")
    for line_n in range(startline):
        f.write('\n')
    for line in range(startline,endline):
        f.write('aaaaaaaaaa\n')
    # lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f.close()


def returnlines(startline,endline):
    lines = []
    f = open('a.txt', "a")
    for line_n in range(startline):
        lines.append('\n')
    for line in range(startline,endline):
        lines.append('aaaaaaaaaa\n')
    # lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f.close()
    return lines

startline_init = 3
endline_init = 8
addlines(startline_init-1,endline_init)

startline_add1 = 9
endline_add1 = 13
if startline_add1 > endline_init:
    f2 = open('a.txt', "r", encoding="utf-8")
    lines_2 = f2.readlines()
    f2.close()
    addlines(startline_add1,endline_add1)
    for line,num in enumerate(lines):


    


# with open('a.txt', "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     for num,row in enumerate(lines):
#         if num == 2:
#             # f.write('3番目')
#             print(row)

# lines.insert(0, '\n')
# lines.insert(1, '\n')
# lines.insert(2, '\n')
# lines.insert(3, '\n')
# lines.insert(4, '\n')
# lines.insert(5, '\n')
# lines.insert(6, '\n')
# lines.insert(7, '\n')
# lines.insert(8, 'a\n')
# lines.insert(9, 'b\n')
# lines.insert(8, 'c\n')
# lines.insert(9, 'd\n')

# lines[0] = 'd\n'
# lines.insert(3, 'e\n')
# lines.insert(4, 'f\n')


# f2 = open('a.txt',"w")
# for line in lines:
#     f2.write(line)

# print(lines)