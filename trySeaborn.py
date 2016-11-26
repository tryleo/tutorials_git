
# coding: utf-8
get_ipython().magic(u'matplotlib inline')

import seaborn
import seaborn as sns


# Load one of the data sets that come with seaborn
tips = sns.load_dataset("tips")
sns.jointplot("total_bill", "tip", tips, kind='reg');

# 항목 몇 개만 출력해 봄
tips.head()

# 길이를 출력, 한 라인에 출력시에 print문 뒤에 ',' 출력
print len(tips), 
print len(tips)




