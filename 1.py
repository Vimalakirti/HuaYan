"""
〈世主妙嚴品第一之一〉（第一卷）有幾位大德（除佛世尊）呢？
"""

import re

count = 0

with open('T0279/T0279_001.txt') as f:
    readdata = f.readlines()
    for i in range(31, 110):
        line = readdata[i]
        m = re.search("：(.+?)……", line)
        if m:
            bhadanta = m.group(1).split("、")
            print(bhadanta)
            count += len(bhadanta)

print("總共有{}位大德。".format(count))