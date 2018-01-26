# regular expression
# coding = utf-8

import re

line = "booooooooooooobby123"

regex_str = "^b.*"
#    *代表可以重复任意次
regex_str = "^b.*3$"

if re.match(regex_str, line):
    print("yes")

"""*************************************************************************

^ 以尖括号开头 代表以这个开头
$ 美元符号，以这个字符结尾   X$
* 乘号 表示字符有很多歌.*表示中间任意字符
（贪婪匹配、非贪婪匹配）
? 非贪婪匹配
+ 前面的字符至少出现一次
| 或的关系
[] 任意一个就可以
|和[]要加括号

+ and * and {2}/{2，5}/{2，}都是限定词，限定之前的字符出现了多少次

[]中^为非的含义，中括号里没有上述含义

.代表任意字符

\s 代表空格的意思
\S 代表不为空格都可以
\w = [A-Za-z0-9_]
\W 非\w的全部

[\u4E00-\u9F5A]表示汉字

()代表里面的词子组的

\d代表数字类型



*************************************************************************"""

regex_str1 = [".*(b.*b).*", ".*?(b.*b).*", ".*?(b.*?b).*"]
print(regex_str1[1])
match_obj =[]
for x in range(len(regex_str1)):
    match_obj.append(re.match(regex_str1[x],line))

    if match_obj[x]:
        print(match_obj[x].group(1))

line = "18782902222"

number = "1[34578][0-9]{9}" # 正则表达电话号码


school = "I study in 南方科技大学"

pick = ".*?([\u4E00-\u9FA5]+大学)"

match_1 = re.match(pick, school)
if match_1:
    print(match_1.group(1))

school1 = "刘麒麟出生于1995年6月1日"

pick1 = ".*(\d{4}[年/-]\d{1,2}[月/-](\d{1,2}日|$|\d{1,2}))"

match_2 = re.match(pick1, school1)
if match_2:
    print(match_2.group(1))