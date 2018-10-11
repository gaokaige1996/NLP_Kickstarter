# -*- coding:utf-8 -*-
import os
import os.path #文件夹遍历函数
#获取目标文件夹的路径
filedir = '/Users/mia/PycharmProjects/risk_chanllenge/techtxtfile'
#获取当前文件夹中的文件名称列表
filenames=os.listdir(filedir)
#打开当前目录下的result.txt文件，如果没有则创建
f=open('techresult.txt','w')
#先遍历文件名
for i in range(1,1891):
    filepath = filedir+'/'+str(i)+'.txt'
    #遍历单个文件，读取行数
    size = os.path.getsize(filepath)
    if size == 0:
        l = 'None'
        f.writelines(l)
        f.write('\n')
    else:
        for line in open(filepath):
            #print(line)
            f.writelines(line)
            f.write('\n')

#关闭文件
#f.close()