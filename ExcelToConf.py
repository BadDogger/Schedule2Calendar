# coding: utf-8
#!/usr/bin/python

import sys
import json
import xlrd

__author__ = 'badDogger'
__site__ = 'https://github.com/BadDogger'

# 指定信息在 xls 表格内的列数
_colOfClassName = 0
_colOfStartWeek = 1
_colOfEndWeek = 2
_colOfWeekday = 3
_colOfClassTime = 4
_colOfClassroom = 5

def main():
	# 读取 excel 文件
	data = xlrd.open_workbook('classInfo.xlsx')
	table = data.sheets()[0]
	# print table.cell(1,0).value
	# 基础信息
	numOfRow = table.nrows  #获取行数,即课程数
	numOfCol = table.ncols  #获取列数,即信息量
	headStr = '{\n"classInfo":[\n'
	tailStr = ']\n}'
	classInfoStr = ''
	classInfoArray = []
	# 信息列表
	# lengthOfList = numOfRow-1
	classNameList = []
	startWeekList = []
	endWeekList = []
	weekdayList = []
	classTimeList = []
	classroomList = []

	# 确定配置内容
	info = "\n Welcome \n"
	info += "ClassName: " + str(_colOfClassName) + "Colume\n"
	info += "StartWeek: " + str(_colOfStartWeek) + "Colume\n"
	info += "EndWeek: " + str(_colOfEndWeek) + "Colume\n"
	info += "Weekday: " + str(_colOfWeekday) + "Colume\n"
	info += "ClassTime: " + str(_colOfClassTime) + "Colume\n"
	info += "Classroom: " + str(_colOfClassroom) + "Colume\n"
	# print (info)
	# info += "输入 0 继续，输入 1 退出："
	option = raw_input("0 to continue, 1 to quit")
	if option == "1":
		sys.exit()
	

	# 开始操作
	# 将信息加载到列表
	i = 1
	while i < numOfRow :
		index = i-1

		classNameList.append(((table.cell(i, _colOfClassName).value)))
		startWeekList.append(str(int((table.cell(i, _colOfStartWeek).value))))
		endWeekList.append(str(int((table.cell(i, _colOfEndWeek).value))))
		weekdayList.append(str(int((table.cell(i, _colOfWeekday).value))))
		classTimeList.append(str(int((table.cell(i, _colOfClassTime).value))))
		classroomList.append(str(((table.cell(i, _colOfClassroom).value))))
		
		i += 1
	i = 0
	itemHeadStr = '{\n'
	itemTailStr = '\n}'

	classInfoStr += headStr
	for className in classNameList:
		itemClassInfoStr = ""
		itemClassInfoStr  = itemHeadStr + '"className":"' + className + '",'
		itemClassInfoStr += '"week":{\n"startWeek":' + startWeekList[i] + ',\n'
		itemClassInfoStr += '"endWeek":' + endWeekList[i] + '\n},\n'
		itemClassInfoStr += '"weekday":' + weekdayList[i] + ',\n'
		itemClassInfoStr += '"classTime":' + classTimeList[i] + ',\n'
		itemClassInfoStr += '"classroom":"' + classroomList[i] + '"\n'
		itemClassInfoStr += itemTailStr
		classInfoStr += itemClassInfoStr
		if i!=len(classNameList)-1 :
			classInfoStr += ","
		i += 1
	classInfoStr += tailStr
	# print classInfoStr
	with open('conf_classInfo.json','w') as f:

		f.write(classInfoStr)
		f.close()
	print("\nALL DONE !")

reload(sys);
sys.setdefaultencoding('utf-8');
main()