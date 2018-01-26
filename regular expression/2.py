# -*- coding: UTF-8 -*-
import re
school = "I study in 南方科技大学"

pick = ".*?([\u4E00-\u9FA5]+大学)"

match_1 = re.match(pick, school)
if match_1:
    print(match_1.group(1))