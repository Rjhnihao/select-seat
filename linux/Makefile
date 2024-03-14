PWD=$(shell pwd)

start:
	@nohup python3 test.py &
stop:
	@lsof +D $(PWD) | awk 'NR>1 {print $$2}' | sort -u | xargs -r kill
