# -*- coding: UTF-8 -*-

import re
log = open('/private/var/log/install.log').read()

#   使用?P<>来对分组命名
print(re.sub('(?P<hour>\d{2}):(?P<min>\d{2}):(?P<sec>\d{2})', r'\g<hour>/\g<min>/\g<sec>',log ))
#   使用相对位置\1 \2 \3来区分分组      记得加原始字符  r' '
print(re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1',log ))