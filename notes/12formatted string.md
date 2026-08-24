# 格式化字符串
![img.png](../assets/img12.png)
发新年祝福 ↑
要是想把祝福内容改成这样，并且要根据实际情况替换生肖和名字
![img_1.png](../assets/img12_1.png)
那么代码可以写成这样 ↓
![img_2.png](../assets/img12_2.png)
🤔有没有觉得这段内容很繁琐稀碎不直观不连贯？

## python提供了两种方式，更加简洁优雅地格式化字符串
- format方法
1.
![img_3.png](../assets/img12_3.png)
里面的数字表示，会用format里面的第几个参数进行替换
2.
![img_4.png](../assets/img12_4.png)
3. 更简洁
![img_5.png](../assets/img12_5.png)

- f-字符串
![img_6.png](../assets/img12_6.png)
在字符串前加前缀f，花括号里的内容会被直接求值，添加到字符串内。
![img_7.png](../assets/img12_7.png)

- 数字也可以对字符串进行格式化
![img_8.png](../assets/img12_8.png)
此时，不需要手动将数字转换成字符串就可以打印信息。
![img_9.png](../assets/img12_9.png)
↑ （format方法） 保留两位小数的写法 ↓ （f-字符串）
![img_10.png](../assets/img12_10.png)