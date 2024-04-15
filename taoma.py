import qrcode
my_text = """{
    "key1": "abcddddddd",
    "key2": "abcddddd",
    "key3": "abcd",
    "key4": "abcd",
    "key5": "abcd"
}"""
qr = qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(my_text)
qr.make(fit=True)
img = qr.make_image(fill ='black',back_color = 'white')
img.save("choma.png")

