PWD=$(shell pwd)

.PHONY: start start1 start2 stop stop1 stop2

start: start1 start2

start1:
	@nohup python3 R.py > R.log 2>&1 &

start2:
	@nohup python3 test.py > test.log 2>&1 &

stop: stop1 stop2

stop1:
	@pkill -f R.py

stop2:
	@pkill -f test.py
