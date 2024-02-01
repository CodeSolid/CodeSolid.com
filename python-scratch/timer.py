#! python3
import sys
from datetime import datetime


if (len(sys.argv)) != 2:
	print("Usage timer <exercise_number>")
else:
	msg = "Exercise " + sys.argv[1] + " begun:  " + str(datetime.now()) + "\n"
	with open("log.timer.txt", "a") as f:
		f.writelines([msg])
	print(msg)