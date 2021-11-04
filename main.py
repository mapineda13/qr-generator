import pyqrcode
import png
from pyqrcode import QRCode

string = "https://www.marca.com/"
url = pyqrcode.create(string)
url.svg("myqr.svg", scale=8)
url.png("myqr.png", scale=6)