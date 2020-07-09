#!/usr/bin/env python3

import shutil
import psutil


def chk_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free/du.total*100

	if(free>20):
		print("Disk free space is available more than 20%")
	else:
		print("Disk space is not sufficient for more storage")

	return free>20



def chk_cpu_usage():
	usage = psutil.cpu_percent(1)
	if(usage<75):
		print("cpu usage is less thn 75%")
	else:
		print("cpu using criticaley")

	return usage<75


# Magic
#chk if above two fxn will return true or false

if not chk_disk_usage("/") or not chk_cpu_usage():
	print("ERROR!")
else:
	print("Everything is ok!")