
import pandas as pd
# -*- coding:'utf-8' -*-

with open('/Users/mia/Desktop/tech_kickstarter_url_wrong.txt') as  f1:#打开'weibo_train_data.txt'文件
    f11 = f1.readlines()

with open('tech_change.txt','w') as f2:
    for x in f11:
       if 'http:' in x:
           f2.write(str(x) )
          # f2.write('\t')
       else:
           f2.write('https://www.kickstarter.com/projects/' + str(x) )
