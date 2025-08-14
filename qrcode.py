import qrcode as qr
from PIL import Image

qr =qr.QRCode(version = 1, error_correction= qr.constants.ERROR_CORRECT_H,box_size = 10,border = 4)
qr.add_data("https://in.linkedin.com/in/aswathi-viswam-6b94871b8")
qr.make(fit = True)
img = qr.make_image(fill_color = "blue",back_color = "white")
img.save("linkedin_qrcode.png")