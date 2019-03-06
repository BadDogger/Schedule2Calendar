# Schedule2Calendar

课程表导入日历工具，生成.ics文件用于建立日历。

使用方法：

1. 打开 conf_classTime.json 文件, 设置好课程时间
2. 打开 classInfo.xlsx 文件, 设置好学期课表
3. 使用 python2 运行 main.py, 输入0即可
4. 同目录下生成的 class.ics 文件就是标准日历格式的课程表，Windows和Android系统可以直接用日历程序打开
5. 如果是ios系统，可采用的一种方法是用附件的形式发送 class.ics， 在iPhone 或者iPad中打开这封邮件，点开附件就可以自动加入到系统日历中

