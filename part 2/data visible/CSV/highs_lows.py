import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "C:/Users/36132/Desktop/python learning/Python crash course/part 2/data visible/CSV/sitka_weather_2021_full.csv"
with open(filename) as f:   #将结果文件对象储存在f中
    reader=csv.reader(f)    #调用csv.reader()，并将存储的文件对象传递给它
                            #从而创建一个与该文件相关联的reader对象
    
    header_row=next(reader) #模块csv包含next()函数，调用它并传递给它阅读器对象时,其将返回文件的下一行，
                            #这里它读完了第一行并跳过，后续数据读取将从第二行开始
    #print(header_row)

    #for index,column_header in enumerate(header_row):  #对列表调用enumerate()以获取每个元素的索引及其值
    #   print(index,column_header)

    #获取最高、最低气温和日期
    highs=[]
    dates=[]
    lows=[]
    for row in reader:       #遍历每一行数据(从第二行开始)
    #    if row[7]!='':
    #        highs.append(int(row[7])) #默认为字符串格式
    #    else:
    #        highs.append(highs[-1])
    #    lows.append(int(row[8]))
    #    dates.append(datetime.strptime(row[2],"%Y-%m-%d"))
    
    #处理错误数据
        try:
            current_date=datetime.strptime(row[2],"%Y-%m-%d")
            high=int(row[7])
            low=int(row[8])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig=plt.figure(dpi=128,figsize=(10,6))   #创建一个新的图形并设置尺寸和分辨率
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5) #绘制两条曲线；alpha表示透明度，为0表示完全透明，为1表示完全不透明
plt.fill_between(dates,highs,lows,facecolor='green',alpha=0.1) #方法fill_between()接受一个x值系列和两个y值系列
                                                               #并填充两个y值系列之间的空间
                                                               #实参facecolor指定填充区域的颜色

plt.title("Daily high temperatures, 2021",fontsize=24)
plt.xlabel("",fontsize=16)
fig.autofmt_xdate()  #绘制斜的日期标签以免彼此重叠
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

plt.show()
