# ValueError: listdir: embedded null character in path，因为在windows下书写路径时，常用为”\"，将其改为“/”即可
#文件路径中若包含‘\0’、’\t’ 等特殊转义字符时要特别注意,路径前需要加"r"，防止识别为转义字符，也可以用”\\"表示
#endswith()函数
#描述：判断字符串是否以指定字符或子字符串结尾。

import os
from os import listdir

my_path = r'F:\Python\python全套（推荐）\09-django框架v5.0\第1节  redis安装配置'
new_path=my_path+'\\'

for file_name in listdir(my_path):

    if file_name.endswith('.ev4'):
        new_path=new_path+file_name
        os.remove(new_path)
