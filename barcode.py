#import the module Qrcode
import qrcode
#declare a variable to hold the qr function make()
img = qrcode.make("https://github.com/Niruifedi")
#save the file in jpg format for easy access
img.save("gitprofile.jpg")
