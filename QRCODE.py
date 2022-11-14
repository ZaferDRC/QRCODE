import qrcode

data = "Message Or Link"  # This is Our message or link. 
                          # Buras�, Qr Kod okutulduktan sonra g�z�kecek olan, bizim belirledi�imiz mesaj veya link.


qr = qrcode.make(data) # Converting data for the qr code.
                       # Burada Belirledi�imiz mesaj qr koda d�n��t�r�l�yor.


qr.save('test.png')    # File name and format choosing and save (The file occurs in the same folder as the project.).
                       # Bu k�s�mda olu�turulan qr kodun ismi ve dosya format� belirlenir. (Dosya, proje ile ayn� klas�rde olu�ur.)