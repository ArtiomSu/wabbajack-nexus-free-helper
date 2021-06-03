import os
import time

try:
	import pyautogui
except ModuleNotFoundError:
	print("donwloading pyautogui")
	os.system("pip install pyautogui")
	os.system("pip install pillow")

try:
	import cv2 as cv
except ModuleNotFoundError:
	print("donwloading opencv-python")
	os.system("pip install opencv-python")

conf = 0.9

# image file names
MANUAL_DOWNLOAD_IMG = "manual.png"
ADDITIONAL_DOWNLOAD_IMG = "additional download.png"
SLOW_DOWNLOAD_IMG = "slow download.png"
BACK_IMG = "back.png"

STEP_MANUAL_DOWNLOAD = 0
STEP_ADDITIONAL_DOWNLOAD = 1
STEP_SLOW_DOWNLOAD = 2

step = STEP_MANUAL_DOWNLOAD
download_count = 0 # keep track of downloads
stuck_in_step = [0,0,0] # stuck in either step 0, 1 or 2
total_stuck = 0 # used if the browser needs to be refreshed by pressing the back button

def manual_download():
	global step, download_count, stuck_in_step, total_stuck
	manualbuttonloc = pyautogui.locateOnScreen(MANUAL_DOWNLOAD_IMG, confidence = conf)
	print('Locating manual download button...')
	if manualbuttonloc != None:
		print('Clicking manual download button!')
		manualbuttonloc = pyautogui.center(manualbuttonloc)
		# Here we check again if the button is on the same place due to the browser scrolling
		confirm_location = pyautogui.locateOnScreen(MANUAL_DOWNLOAD_IMG, confidence = conf)
		if confirm_location != None:
			confirm_location = pyautogui.center(confirm_location)
			if manualbuttonloc.x == confirm_location.x and manualbuttonloc.y == confirm_location.y:
				pyautogui.click(manualbuttonloc.x, manualbuttonloc.y)
				print("[" + str(download_count) + "] Attempted Mod Downloads")
				download_count += 1
				step = STEP_ADDITIONAL_DOWNLOAD
				total_stuck = 0
				return
	if manualbuttonloc == None:
		print('Could not locate manual download button.')

	stuck_in_step[1] = 0
	stuck_in_step[2] = 0   
	stuck_in_step[0] = stuck_in_step[0] + 1 
	if stuck_in_step[0] > 5:
	   step = STEP_ADDITIONAL_DOWNLOAD

def additional_download():
	global step, total_stuck
	additionalbuttonloc = pyautogui.locateOnScreen(ADDITIONAL_DOWNLOAD_IMG, confidence = conf)
	print('Locating additional download button...')
	if additionalbuttonloc != None:
		print('Clicking additional download button!')
		additionalbuttonloc = pyautogui.center(additionalbuttonloc)
		pyautogui.click(additionalbuttonloc.x, additionalbuttonloc.y)
		step = STEP_SLOW_DOWNLOAD
		total_stuck = 0
		return
	if additionalbuttonloc == None:
		print('Could not locate additional download button.')
	step = STEP_SLOW_DOWNLOAD

def slow_download():
	global step, download_count, stuck_in_step, total_stuck
	slowbuttonloc = pyautogui.locateOnScreen(SLOW_DOWNLOAD_IMG, confidence = conf)
	print('Locating slow download button...')
	if slowbuttonloc != None:
		print('Clicking slow download button!')
		slowbuttonloc = pyautogui.center(slowbuttonloc)
		pyautogui.click(slowbuttonloc.x, slowbuttonloc.y)
		time.sleep(6)
		step = STEP_MANUAL_DOWNLOAD
		total_stuck = 0
		return
	if slowbuttonloc == None:
		print('Could not locate slow button.')
		# check if the manual download button is still there?
		manualbuttonloc = pyautogui.locateOnScreen(MANUAL_DOWNLOAD_IMG, confidence = conf)
		if manualbuttonloc != None:
			print('Clicking manual download button!')
			manualbuttonloc = pyautogui.center(manualbuttonloc)
			pyautogui.click(manualbuttonloc.x, manualbuttonloc.y)
			print("[" + str(download_count) + "] Attempted Mod Downloads")
			download_count += 1
			step = STEP_ADDITIONAL_DOWNLOAD
			total_stuck = 0
			return

		# check if the additional button is still there
		additionalbuttonloc = pyautogui.locateOnScreen(ADDITIONAL_DOWNLOAD_IMG, confidence = conf)
		if additionalbuttonloc != None:
			print('Clicking additional download button!')
			additionalbuttonloc = pyautogui.center(additionalbuttonloc)
			pyautogui.click(additionalbuttonloc.x, additionalbuttonloc.y)
			step = STEP_SLOW_DOWNLOAD
			total_stuck = 0
			return	
	stuck_in_step[0] = 0
	stuck_in_step[1] = 0  
	stuck_in_step[2] = stuck_in_step[2] + 1
	if stuck_in_step[2] > 5:
	   step = STEP_MANUAL_DOWNLOAD	

def check_if_stuck():
	# Sometimes the browser gets stuck so click the back button
	global total_stuck
	total_stuck = total_stuck + 1	 
	if total_stuck > 20:
		back_button =  pyautogui.locateOnScreen(BACK_IMG, confidence = conf)
		if back_button != None:
			print('Clicking back button cause stuck')
			back_button = pyautogui.center(back_button)
			pyautogui.click(back_button.x, back_button.y)
			total_stuck = 0

def main():
	while True:
		time.sleep(1)
		if step == STEP_MANUAL_DOWNLOAD:
			manual_download()
		if step == STEP_ADDITIONAL_DOWNLOAD:
			additional_download()
		if step == STEP_SLOW_DOWNLOAD:
			slow_download()
		check_if_stuck()


if __name__ == "__main__":
	main()
