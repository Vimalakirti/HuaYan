"""
八十卷《大方廣佛華嚴經》有幾個字呢？
"""
from utils import Lines_in_sutra
count = 0
for volume in range(1, 81):
    readdata = Lines_in_sutra(volume)
    for row in range(9, len(readdata)):
        line = readdata[row]
        count+=len(line)-1 # 去掉換行符

print("《大方廣佛華嚴經》總字數：{}字。".format(count))