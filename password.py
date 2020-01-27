password = 'a123456'
turn = 3

while turn > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		turn = turn - 1
		print('密碼錯誤! 還有', turn, '次機會')
		if turn == 0:
			break
		
