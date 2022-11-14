import qrcode

data = "Message Or Link"  # This is Our message or link. 
                          # Burasý, Qr Kod okutulduktan sonra gözükecek olan, bizim belirlediðimiz mesaj veya link.


qr = qrcode.make(data) # Converting data for the qr code.
                       # Burada Belirlediðimiz mesaj qr koda dönüþtürülüyor.


qr.save('test.png')    # File name and format choosing and save (The file occurs in the same folder as the project.).
                       # Bu kýsýmda oluþturulan qr kodun ismi ve dosya formatý belirlenir. (Dosya, proje ile ayný klasörde oluþur.)