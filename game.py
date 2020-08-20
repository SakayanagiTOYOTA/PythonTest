import random

print "************************"
print "     CHO HAN GAME"
print "************************"
flg = True
while flg:
	while True:
		print "Hatta Hatta: CHO(0) HAN(1) Exit(9)"
		sw = input()
		if sw == 9:
			flg = False
			break
		elif sw == 0 or sw == 1:
			break
	if flg:
		d1 = int(random.random()*6)+1
		d2 = int(random.random()*6)+1
		print "Dice1:" + str(d1)
		print "Dice2:" + str(d2)
		if sw == (d1 + d2) % 2:
			print "ATARI!"
		else:
			print "HAZURE!!"
print "Good Bye"

