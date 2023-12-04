import segno
link_code = ['https://t.me/farmasiby', 'https://t.me/Farmasiaboutproduct', 'https://www.instagram.com/farmasibelarus/']
file_name = ['d:/QR/tg.png', 'd:/QR/tg_product.png', 'd:/QR/insta.png']
# белый(white) QR на прозрачном(FFFFFF00) фоне
x = 0
while x < 3:
    qrcode = segno.make_qr(link_code[x])
    qrcode.save(file_name[x], dark="white", light="FFFFFF00", border=1, scale=30)
    x += 1
