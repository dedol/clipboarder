import os
import time
import win32api
import keyboard
import winsound
import win32clipboard
from PIL import Image
from io import BytesIO

last_call = 0  # unix timestamp for last calling paste function
current = 0 # counter value for photo
sorted_files = [] # list for sorted files
drive = "" # disk letter for removable device

def paste():
	global last_call, current, sorted_files, drive

	# if more than 60 seconds elapsed between calls
	# then need to update files list
	if int(time.time()) - last_call > 60:
		drives = win32api.GetLogicalDriveStrings() # get local drives
		drives = drives.split('\000')[:-1] # get list of drives

		# find drive with path "DCIM\100NCD90" from list of drives
		drive = ""
		for letter in drives:
			if os.path.exists(letter + "DCIM\\100NCD90"):
				drive = letter

		# if not found drive
		# then beep one time and exiting from function
		if drive == "":
			winsound.Beep(2000, 100) # 2000 Hz for 100 milliseconds
			return

		# get files list in path "DCIM\100NCD90"
		files = os.listdir(drive + "DCIM\\100NCD90")

		# if found file Thumbs.db
		# then remove it
		if (files.count('Thumbs.db')):
			files.remove('Thumbs.db')

		# sort files by last modified and get sorted list
		file_date = {}
		for file in files:
			statinfo = os.stat(drive + "DCIM\\100NCD90\\" + file)
			file_date[file] = statinfo.st_mtime
		file_date = list(file_date.items())
		file_date.sort(key=lambda i: i[1], reverse=True)
		sorted_files = []
		for file in file_date:
			sorted_files.append(file[0])

		current = 0 # set index of first file in list

	last_call = int(time.time()) # update last calling timestamp

	# if list index out of range
	# then beep one time and exiting from function
	if current > len(sorted_files) - 1:
		winsound.Beep(2000, 100) # 2000 Hz for 100 milliseconds
		return

	# drive could be extracted, file could be moved
	# if path to current file does not exist
	# then beep one time and exiting from function
	if not os.path.exists(drive + "DCIM\\100NCD90\\" + sorted_files[current]):
		winsound.Beep(2000, 100) # 2000 Hz for 100 milliseconds
		return

	# set file path and convert current image to bmp
	filepath = drive + "DCIM\\100NCD90\\" + sorted_files[current]
	image = Image.open(filepath)
	output = BytesIO()
	image.convert("RGB").save(output, "BMP")
	data = output.getvalue()[14:] # bmp header file = 14 byte
	output.close()

	# put image on clipboard
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
	win32clipboard.CloseClipboard()

	# emulate paste combination
	keyboard.press_and_release('Ctrl + v')

	# inc counter
	current += 1

def restart():
	global last_call
	# reset last calling time and beep two time
	last_call = 0 
	winsound.Beep(2000, 100) # 2000 Hz for 100 milliseconds
	time.sleep(0.1) # silence 100 milliseconds
	winsound.Beep(2000, 100) # 2000 Hz for 100 milliseconds

# if press combiantion
# then do function
keyboard.add_hotkey('Ctrl + space', paste)
keyboard.add_hotkey('Ctrl + r', restart)

# combination for exiting
keyboard.wait('Ctrl + q')

# beep three time
winsound.Beep(2000, 100) # 2000 Hz for 100 milliseconds
time.sleep(0.1) # silence 100 milliseconds
winsound.Beep(2000, 100) # 2000 Hz for 100 milliseconds
time.sleep(0.1) # silence 100 milliseconds
winsound.Beep(2000, 100) # 2000 Hz for 100 milliseconds

# clean clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.CloseClipboard()
