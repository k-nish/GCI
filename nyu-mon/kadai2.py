#coding: utf8
i = int(raw_input())
if i%4 == 0:
	if i%100 == 0:
		if i%400 == 0:
			print str(i) + "年は閏年です。"
		else:
			print str(i) + "年は閏年ではありません。"
	else:
		print str(i) + "年は閏年です。"
else:
	print str(i) + "年は閏年ではありません。"
