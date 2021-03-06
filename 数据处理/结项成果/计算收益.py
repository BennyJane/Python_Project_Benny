#!/user/bin/env Python
#coding=utf-8

import pandas as pd

#将第二段段代码生成的文件（包含4列的文件）路径拷贝到下方
#该文件包含了圆点-三角形点的时间和价格
FirstResult_filepath="E:/编程接单/2019-4-14/Second_data16_422.csv"
df=pd.read_csv(FirstResult_filepath)
# print(df)
df.rename(columns={'exchange_time':'Extremity', 'means':'Start_price', 'exchange_time.1':'confirm_point','means.1':'End_price'}, inplace = True)

# print(df)
finalfilepath="E:/编程接单/2019-4-14/Sales02_422.csv"

Sales=pd.DataFrame(columns=["confirm_point","income"])


#求总收益，每2行一组，需要判断第一行为买进操作，还是卖出操作
sum=0
nums=df.shape[0]
print(nums)

j=0
i=0
# 第一行为升，此刻选择卖出
while True:
    if i < nums:
        Now_time=df.iloc[j,2]
        # 需要判断每天的开始的第一行是升，还是降
        if (df.iloc[j, 3] - df.iloc[j, 1]) >= 0:
            try:
                Start_time1=df.iloc[i, 2]
                Start_time2 = df.iloc[i+1, 2]
            except Exception as e:
                Start_time1='2019-03-01'
                Start_time2 = '2019-10-02'
                print(e)
            if Start_time1[6:11]==Now_time[6:11]:
                if Start_time2[6:11]==Now_time[6:11]:
                    try:
                        End_price01 = df.iloc[i, 3]
                        End_price02 = df.iloc[i + 1, 3]
                    except Exception as e:
                        End_price01 = 0
                        End_price02 = 0
                    # print(End_price01-End_price02)
                    sum=sum+(End_price01-End_price02)
                    Day = Start_time2
                    Sales.loc[Sales.shape[0] + 1] = [Day, sum]
                    i=i+2
                else:
                    j=i+1
                    i=i+1
                    sum = 0
                    # continue
            else:
                j=i
                sum=0
                # continue

        else:
            try:
                Start_time1=df.iloc[i, 2]
                Start_time2 = df.iloc[i+1, 2]
            except Exception as e:
                Start_time1=df.iloc[i, 2]
                Start_time2 = '2019-10-02'
                print(e)
            if Start_time1[6:11]==Now_time[6:11]:
                if Start_time2[6:11]==Now_time[6:11]:
                    try:
                        End_price01 = df.iloc[i, 3]
                        End_price02 = df.iloc[i + 1, 3]
                    except Exception as e:
                        End_price01 = 0
                        End_price02 = 0
                    # print(End_price01 - End_price02)
                    sum = sum + (End_price02 - End_price01)
                    # print(sum)
                    Day = Start_time2
                    Sales.loc[Sales.shape[0] + 1] = [Day, sum]
                    i=i+2
                else:
                    j=i+1
                    i+=1
                    sum = 0
                    # continue
            else:
                j = i
                sum=0
                # continue
    else:
        break

#sales 求的是当前时间之前的累计收益；每一天的最后一条信息里的金额，就是当天的总收益
print(Sales)
Newdf=pd.merge(df, Sales, how="left",on="confirm_point")
print(Newdf)
# Newdf.to_csv(finalfilepath,index=None)
