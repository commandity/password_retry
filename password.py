password = 'a123456'
turn = 3

while turn > 0:
	turn = turn - 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!')
		if turn > 0:
			print('還有', turn, '次機會')
		else:
			print('要被鎖帳號了')
			break
		
