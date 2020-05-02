import os
import sys
os.system("clear")
banner = """

            ___________________

            [01] Youtube
            [02] Facebook
            __________________
 """
menu = """
            [99] Back to main menu
            [00] Exit

"""
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def returntomenu_option():
	print(menu)
	back = raw_input("carlx: ")
	if back == "99":
		restart_program()
	elif back == "00":
		sys.exit()
	else:
		print("\nERROR: Wrong Input")
		#time.sleep(2)
		restart_program()

print ("             [WELCOME TO CARLX DOWNLOADER]        ")
print banner

choose = raw_input("Download from: ")

if choose == "01" or choose == "1":
    print "[01] mp3(MUSIC ONLY)"
    print "[02] mp4(VIDEO AND AUDIO ONLY)"
    download_from = raw_input("Download using: ")
    if download_from == "01" or download_from == "1":
        link = raw_input("Enter your music link here: ")
        os.system('youtube-dl -x --audio-format mp3 -o "Youtube_Music/%(title)s.%(ext)s" '+link)
        returntomenu_option()
    elif download_from == "02" or download_from == "2":
	link = raw_input("Enter your video link here: ")

	os.system('youtube-dl -f 18 -o "Youtube_video/%(title)s.%(ext)s" '+link)
    else:
        print "unknown input"
elif choose == "02" or choose == "2":
    print "[01] mp3(MUSIC ONLY)"
    print "[02] mp4(VIDEO AND AUDIO ONLY)"
    download_from = raw_input("Download using: ")
    if download_from == "01" or download_from == "1":
        link = raw_input("Enter your music link here: ")
        os.system('youtube-dl -x -c --audio-format mp3 -o "FB_Music/%(title)s.%(ext)s" '+link)
    elif download_from == "02" or download_from == "2":
        link = raw_input("Enter Your Facebook link (VIDEO/MP4): ")
        os.system('youtube-dl -c -f dash_hd_src  -o "FB_Video/%(title)s.%(ext)s" '+link)
    else:
        print "unknown input"
