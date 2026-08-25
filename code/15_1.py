# 定义一个学生类
# 要求：
# 1. 属性包括学生姓名、学号，以及语数英三科成绩
# 2. 能够设置学生某科目的成绩
# 3. 能够打印该学生的所有科目成绩

class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        # self.grade_c=grade_c
        # self.grade_m = grade_m
        # self.grade_e = grade_e
        self.grades={"语文":0,"数学":0,"英语":0}

    # def set_grade_c(self,grade_c):
    #     self.grade_c=grade_c
    #
    # def set_grade_m(self,grade_m):
    #     self.grade_m=grade_m
    #
    # def set_grade_e(self,grade_e):
    #     self.grade_e=grade_e
    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course]=grade

    def print_grade(self):
        # print(f"学生{self.name}(学号：{self.id})的语文成绩为：{self.grade_c},数学成绩为：{self.grade_m},英语成绩为：{self.grade_e}")
        print(f"学生{self.name}(学号：{self.id})的成绩为：")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")

chen=Student("小陈","10086")
zeng=Student("小曾","10088")
print(chen.name)
print(zeng.grades)

zeng.set_grade("语文",90)
print(zeng.grades)

zeng.set_grade("数学",97)
zeng.print_grade()