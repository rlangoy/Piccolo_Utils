import socket
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft

UDP_IP = '192.168.7.2'
UDP_PORT = 7778

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

udpPackagesToRead=5  #Read two UDP Packages

data1_values=[]
for i in range(0,udpPackagesToRead):
   data1, addr = sock.recvfrom(1500)         # Wait for UDP package
   data1_values = data1_values+list(data1)   # Append Converted byte data to List values


#
Fs=500E3              #Sample rate
N=len(data1_values)   #Number of bytes recieved
n = np.arange(N)           #Create list
T = N/Fs                   # Time is number of bytes / samprate 
freq = n/T 

#Plot the recieved data
strTitle= str(udpPackagesToRead) +' - UDP packages read width ' + str(N) + ' Bytes'
strTitle=strTitle+'\n From the address ' + UDP_IP

plt.subplot(2, 1, 1)
plt.title(strTitle)

plt.xlabel('Time')
plt.ylabel('Byte Value')
plt.plot(n*Fs,data1_values)

plt.subplot(2, 1, 2)

plt.magnitude_spectrum(data1_values, Fs = Fs) 
plt.xlim(0, Fs/2)
plt.xlabel('Frequency')
plt.ylabel('Strength')
plt.show()
  