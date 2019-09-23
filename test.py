# 判斷 json format 是否正確

import re

josn_ls = [{"key11":"","key5":[],"key3":"453","key88":[1,2],"key99":[4,5]},
            {"key11":"","key5":[],"key3":"error","key88":[1,2],"key99":["error",5]},
            {"fdshi":1,"fsdjfiljs":"","ljdl":[],"key":["error",1]},
            {"key":"valuse","key2":"error"}]

correct = []
for j in josn_ls:
    c = str(j).find("error")
    if c == -1:
        correct += [j]
print(correct)


