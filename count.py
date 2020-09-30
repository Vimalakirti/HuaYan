"""
八十卷《大方廣佛華嚴經》有幾個字呢？
"""

count = 0
def format_num(d):
    if d//10 == 0:
        return "0{}".format(d)
    else:
        return str(d)

for j in range(1, 81):
    with open('T0279/T0279_0{}.txt'.format(format_num(j))) as f:
        readdata = f.readlines()
        for i_line in range(9, len(readdata)):
            line = readdata[i_line]
            count+=len(line)-1 # 去掉換行符

print("《大方廣佛華嚴經》總字數：{}字。".format(count))