import qrcode

website_link = "https://youtu.be/xvFZjo5PgG0"

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()
img = qr.make_image(fill_color = 'white', back_color = 'black')
img.save('youtube_qr.png')

#import os import qrcode img = qrcode.make(the same yt link) img.save("qr.png", "PNG")