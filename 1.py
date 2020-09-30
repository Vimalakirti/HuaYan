"""
〈世主妙嚴品第一之一〉（第一卷）有幾位大德（除佛世尊外）呢？
"""
from utils import Lines_in_sutra
import re

count = 0

readdata = Lines_in_sutra(1)
for i in range(31, 110):
    line = readdata[i]
    m = re.search("：(.+?)……", line)
    if m:
        bhadanta = m.group(1).split("、")
        print(bhadanta)
        count += len(bhadanta)

print("總共有{}位大德。".format(count))