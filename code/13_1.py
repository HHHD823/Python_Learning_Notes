# 写一个计算BMI的函数，函数名为calculate_BMI。
# 1.可以计算任意体重和身高的BMI值
# 2.执行过程中打印一句话，“您的BMI分类为：xx”
# 3.返回计算的BMI值

# BMI=体重/（身高**2） 米、千克
#BMI分类
# 偏瘦：user_BMI ＜=18.5
# 正常：18.5＜user_BMI＜=25
# 偏胖：25＜user_BMI＜=30
# 肥胖：user_BMI＞30

def calculate_BMI(weight,height):
    bmi=weight/(height**2)
    if bmi<=18.5:
        print("您的BMI分类为：偏瘦")
    elif bmi <= 25:
        print("您的BMI分类为：正常")
    elif bmi <= 30:
        print("您的BMI分类为：偏胖")
    else:
        print("您的BMI分类为：肥胖")

    return bmi

result=calculate_BMI(50,1.5)
print(result)