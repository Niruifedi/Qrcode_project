#import the module Qrcode
import qrcode

#creating a QRcode object
obj_qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)

#using the add_data() function
obj_qr.add_data("https://github.com/Niruifedi")

#using the make_image() function
qr_img = obj_qr.make_image(fill_color = "red", back_color = "black")
#save the file in jpg format for easy access
qr_img.save("gitprofile.jpg")
