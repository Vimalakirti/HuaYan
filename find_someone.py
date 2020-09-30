"""
想找《大方廣佛華嚴經》的哪一位大德嗎？
"""
from utils import Lines_in_sutra
bhadanta = input("輸入大德名稱： ")
assert type(bhadanta)==str

for volume in range(1, 81):
    readdata = Lines_in_sutra(volume)
    for row in range(9, len(readdata)):
        if bhadanta in readdata[row]:
            print("第{}卷".format(volume))
            print(readdata[row])