# Gathering various information using a Spyware Program
<html>
<body>
    <h3><b>Getting Started : Python, PyCharm and Modules</h3></b> 

<p>Before starting to write the code you really need to install the requirements mentioned below.</p>

Requirements :<br>
     1.Latest vesion of Python<br>
     2.PyCharm Software<br>
     3.Python Modules

  <b>Python Modules</b><br>
    <ul>
        <li>win32clipboard</li>
        <li>pynput</li>
        <li>scipy</li>
        <li>cryptography</li>
        <li>requests</li>
        <li>pillow</li>
        <li>sounddevice</li>
        <li>email</li>
        <li>os</li>
        <li>time</li>
        <li>multiprocessing</li>
        <li>socket</li>
        <li>smtplib</li>
  </ul>
    <h2>CREATING FILES AND APPENDING TO FILES</h2>
<p>For multiple parts of the keylogger, we will be appending data to files. Before we append data to files,
we must first create variables with the proper extensions. Here are the variables you will need with the
    proper extensions.</p>
<code>system_information = "system.txt"</code><br>
<code>audio_information = "audio.wav"</code><br>
<code>clipboard_information = "clipboard.txt"</code><br>
<code>screenshot_information = "screenshot.png"</code><br>
    <code>keys_information = "key_log.txt"</code><br>
<br>
<p>We will also need 3 addition files for encryption, I simply used the e_file_name syntax for each file.</p>
<br>
    <code>system_information_e = 'e_system.txt'</code><br>
    <code>clipboard_information_e = 'e_clipboard.txt'</code><br>
    <code>keys_information_e = 'e_keys_logged.txt'</code><br>
<br>
    <p>To open and append to files, use the with <code>open(file_path, “a”) as f</code></p>
    <p>To write to the file, simply use the <code>f.write(data)</code> method</p>
<h2>Keystrokes</h2>   
<h4>To log keys using python, we will be using the pynput module.</h4>
Module to install:<br>
    <code>from pynput.keyboard import Key, Listener</code><br>
<h2>E-Mail</h2>    
<h4>To add an email functionality, we will be using the email module.</h4>
Modules to install:<br>
    <code>from email.mime.multipart import MIMEMultipart</code><br>
    <code>from email.mime.text import MIMEText</code><br>
<code>from email.mime.base import MIMEBase</code><br>
<code>from email import encoders</code><br>
<code>import smtplib</code><br>

<h2>System</h2>
<h4>To gather computer information, we will use socket and platform modules.</h4>
Modules to install:<br>
<code>import socket</code><br>
<code>import platform</code>

<h2>Clipboard</h2>
<h4>To get the clipboard information, we will be using the win32clipboard module, which is a submodule of
pywin32.</h4>
Module to install:<br>
<code>import win32clipboard</code>

<h2>Microphone</h2>
<h4>To record with microphone, we will be using the sounddevice module and writing to a .wav file using the
scipy.io.wavefile module.</h4>
Module to install:<br>
<code>from scipy.io.wavfile import write</code><br>
<code>import sounddevice as sd</code>

<h2>Screenshot</h2>
<h4>To take a screenshot, we will use the ImageGrab from the Pillow Module</h4>
Modules to install:<br>
<code>from multiprocessing import Process, freeze_support</code><br>
<code>from PIL import ImageGrab</code>

<h3>Build a Timer !</h3>
 <h4>To build a timer which goes through a certain number of iterations before the keylogger ends, we will be using the
     timer function</h4>
<h5>Use the following process:</h5>
1. Create an iterations variable and set its value to zero (iterations = 0)<br>
2. Create an end_iterations variable which sets to a certain amount of iterations before ending the
keylogger (end_iterations = 5)<br>
3. Get the current time using the time.time() function, set this equal to a variable (currentTime =
time.time())<br>
4. Create a time_iteration variable which collects the keylogs for a certain period of time in seconds
(time_iteration = 15)<br>
5. Get the stoppingTime by adding the time.time() function + time_iteration to stop, set this equal to a
variable (stoppingTime = time.time() + time_iteration)<br>
6. while iterations is less than (<) the ending_iterations… log keys<br>
7. If the current time is greater than (>) the stopping time.<br>
<ul>    
    <li>Take a screenshot</li>
    <li>Send screenshot to email</li>
    <li>Gather clipboard contents</li>
    <li>Add 1 to iterations variable</li>
    <li>Get new current time</li>
    <li>Get new stopping time</li>
</ul>

<h2>Encryption-Decryption</h2>
<h4>To encrypt files, we will use the cryptography.fernet module</h4>
Module to import:<br>
    <code>from cryptography.fernet import Fernet</code>

  </body>
  </html>
