import pandas as pd

inputfile = '../data/exams.csv'  # 待聚类的数据文件
df = pd.read_csv(inputfile)  # 读取数据
print(df.info())
'''
分析当前数据特征
['group C', 'group E', 'group D', 'group B', 'group A']
['some college', 'high school', 'some high school', "master's degree", "associate's degree", "bachelor's degree"]
['standard', 'free/reduced']
['none', 'completed']
'''


# race_type_list = df['race_ethnicity'].unique().tolist()
# print(race_type_list)
# parental_level_of_education = df['parental level of education'].unique().tolist()
# print(parental_level_of_education)
# lunch_list = df['lunch'].unique().tolist()
# print(lunch_list)
# test_preparation = df['test preparation course'].unique().tolist()
# print(test_preparation)


def gender(x):
    if x == 'female':
        return 1
    else:
        return 2


def race(x):
    if x == 'group C':
        return 1
    elif x == 'group E':
        return 2
    elif x == 'group B':
        return 3
    elif x == 'group A':
        return 4
    elif x == 'group D':
        return 5


def education(x):
    if x == 'high school' or x =='some high school':
        return 1
    elif x == 'some college':
        return 2
    elif x == "master's degree":
        return 3
    elif x == "associate's degree":
        return 4
    elif x == "bachelor's degree":
        return 5


def lunch(x):
    if x == 'standard':
        return 1
    elif x == 'free/reduced':
        return 2


def test_preparation(x):
    if x == 'completed':
        return 1
    else:
        return 2


def deal():
    # 将文本类数据转化为数值类
    newDf = df.loc[:, :]
    print('newDf:  ', newDf.info())
    newDf['gender'] = df.apply(lambda x: gender(x['gender']), axis=1)
    newDf['race_ethnicity'] = df.apply(lambda x: race(x['race_ethnicity']), axis=1)
    newDf['parental level of education'] = df.apply(lambda x: education(x['parental level of education']), axis=1)
    newDf['lunch'] = df.apply(lambda x: lunch(x['lunch']), axis=1)
    newDf['test preparation course'] = df.apply(lambda x: test_preparation(x['test preparation course']), axis=1)
    # print(newDf.info())

    newDf.columns = ['gender', 'race', 'parental_education', 'lunch', 'test_preparation_course', 'math', 'reading',
                     'writing']
    # print(newDf.info())
    # newDf.to_csv('./newDf.csv', index=None)
    # print(newDf[['parental_education']])
    # 需要对数据归一化，减少因为数值范围差异导致的误差
    newDf = (newDf - newDf.mean(axis=0)) / (newDf.std(axis=0))  # 简洁的语句实现了标准化变换，类似地可以实现任何想要的变换。

    # newDf['gender'] = newDf['gender'].round(4)
    # newDf['race'] = newDf['race'].round(4)
    # newDf['parental_education'] = newDf['parental_education'].round(4)
    # newDf['lunch'] = newDf['lunch'].round(4)
    # newDf['test_preparation_course'] = newDf['test_preparation_course'].round(4)
    # newDf['math'] = newDf['math'].round(4)
    # newDf['reading'] = newDf['reading'].round(4)
    # newDf['writing'] = newDf['writing'].round(4)

    newDf.to_csv('.finalDat.csv', index=None)
    return newDf

# deal()
