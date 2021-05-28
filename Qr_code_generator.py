import pyqrcode
from pyqrcode import QRCode

s = input('Enter the URL you want to convert to QR code: ')

#Generating the QR code
url= pyqrcode.create(s)

url.svg('myqr.svg', scale =8)