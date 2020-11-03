# 密碼重試程式
# 密碼是a12346
# 只有三次機會!

password = "a123456"
i = 3 #剩餘機會
while True:
	pw = input('請輸入密碼: ')
	if pw == password: # 不要打"a123456", 如果上面要改好麻煩
		print('登入成功!')
		break
	else:
		i = i - 1
		print('密碼錯誤! 還有', i, '次機會') #難點出現
		if i == 0:
			print('已輸入錯誤密碼3次!!!強制結束!')
			break