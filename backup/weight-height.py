#!/usr/bin/env python3
h=float(input('please input you height:'))
w=float(input('please input you weight:'))
bmi=w/(h**2)
print('你的BMI值是：%.1f' %bmi) 
if bmi>32:
	print('过度肥胖')
elif bmi>28:
	print('肥胖')
elif bmi>25:
	print('过重')
elif bmi>18.5:
	print('正常')
else:
	print('过轻')