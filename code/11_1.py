# 制作一个计算器，对用户输入数字求平均值。特点是用户可以输入任意数量的数字，最后输入q表示已经输入完毕。

number=input("请输入你想要求平均值的数字（输入字母q表示结束）：")
count=0
total=0
while number!='q' :
    # total=total+float(number)
    # count=count+1
    total += float(number)
    count += 1
    number=input()

if count==0:
    print("没有接受到任何数字！")
else:
    print("输入数字的平均值为："+str(total/count))
# 若不做以上判断，若第一次输入就为q，则total/count为0/0，这在python不被允许，会报错。
