# 文件路径

## 电脑操作系统的目录结构
![img.png](../assets/img17.png)
![img_1.png](../assets/img17_1.png)

## 定位文件位置的方法
1. 绝对路径：从根目录出发
- 对于类Unix操作系统
![img_2.png](../assets/img17_2.png)
- 对于Windows操作系统
![img_3.png](../assets/img17_3.png)

2. 相对路径：从一个参照位置出发，表示从那个位置来看，其他文件处于什么路径
- 用 . 表示参照文件当前所在的目录
- 用 .. 表示更上一层的父目录
![img_4.png](../assets/img17_4.png)
- ./是可以省略的,同一目录下的文件想互相用相对路径找到彼此的话,可以直接使用文件名.
![img_5.png](../assets/img17_5.png)