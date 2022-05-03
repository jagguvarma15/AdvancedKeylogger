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
    <h3>CREATING FILES AND APPENDING TO FILES</h3>
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
    
    <p>To log keys using python, we will be using the pynput module.</p>
Module to install:<br>
    <code>from pynput.keyboard import Key, Listener</code><br>
    
    <p>To add an email functionality, we will be using the email module.</p>
Modules to install:<br>
    <code>from email.mime.multipart import MIMEMultipart</code><br>
    <code>from email.mime.text import MIMEText</code><br>
<code>from email.mime.base import MIMEBase</code><br>
<code>from email import encoders</code><br>
<code>import smtplib</code><br>
    
    
  </body>
  </html>
