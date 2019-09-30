import sys, tty, time
tty.setcbreak(sys.stdin)  
start_time, end_time, old_time, cur_time = 0, 0, 0, 0
file_ptr = open('test-time.txt', mode='a+')
file_ptr.write(time.ctime()+"\n")

while True:
	
	key = ord(sys.stdin.read(1))  # key captures the key-code 
	# based on the input we do something - in this case print something
	if old_time == 0:
		start_time, old_time= time.time(), time.time()

	if key==32 or key==97:
		cur_time = time.time()
		timing = str((cur_time - old_time))[:4] + ' Seconds\n'
		old_time, end_time = cur_time, cur_time
		file_ptr.write(timing)
		print(timing)
		if key==97:
			file_ptr.write('--'*10 + '\n')
			timing = str((end_time - start_time)/60) + ' Minutes\n'
			file_ptr.write('Total timing : '+timing)
			file_ptr.write('-*-'*10 + '\n')
			file_ptr.close()
			break
sys.exit(0)