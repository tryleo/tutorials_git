
# coding: utf-8
# 새로운 폼으로 정리를 시도
get_ipython().magic(u'matplotlib inline')
import seaborn
import seaborn as sns

# Load one of the data sets that come with seaborn
# 데모를 위해 디폴트 데이터를 가져와서 보여준다. 
tips = sns.load_dataset("tips")
sns.jointplot("total_bill", "tip", tips, kind='reg');

# 상위 몇 개의 데이터만 출력
tips.head()


# 데이터의 긾이 출력
print len(tips), 
print len(tips)



