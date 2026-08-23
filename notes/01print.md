# 有关print

## 格式
![img.png](../assets/img01.png)
[基础格式代码](/code/01_1.py)

### 字符串连接
![img_1.png](../assets/img01_1.png)
*hello后或world前没有空格，所以单词会挨在一起*

### 单双引号转义
-字符串用单双引号裹着都可以，效果在绝大多数情况下都一样
![img_3.png](../assets/img01_3.png)
![img_4.png](../assets/img01_4.png)
第二个双引号和第一个配对，后面的内容回暖报错
![img_5.png](../assets/img01_5.png)
![img_6.png](../assets/img01_6.png)
外单内双、外双内单不会报错。
![img_2.png](../assets/img01_2.png)
如图，字符串内要有多个引号的情况。
在字符串里的引号前面加上反斜杠 \ ——转义符 ，代表引号是字符串内容的一部分，并不表示字符串的结束

### 换行
![img_7.png](../assets/img01_7.png)
![img_8.png](../assets/img01_8.png)
**注意：每个print默认另起一行**

### 三引号跨行字符串
![img_9.png](../assets/img01_9.png)
用三引号（单引号双引号都可以）裹住文字，python会把新一行当作内容的换行，而不是代码语句的结束或不完整。**适用于打印跨行多的内容**

[实操代码](/code/01_2.py)