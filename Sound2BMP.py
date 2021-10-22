import os

sound= open("sound.wav", 'rb')
if os.path.isfile("soundimage.bmp")==True:
    os.remove("soundimage.bmp")
soundimage = open("soundimage.bmp", 'ab')

headerbytes= b'BM\x8a\xb0\x04\x00\x00\x00\x00\x00\x8a\x00\x00\x00|\x00\x00\x00\xf0\x00\x00\x00\x80\x02\x00\x00\x01\x00\x10\x00\x03\x00\x00\x00\x00\xb0\x04\x00#.\x00\x00#.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\xe0\x07\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00BGRs\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc69iJ\x8aJ\xabR\xabR\xabR\xcbRIB\xe5\x18\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x84\x10\xa4\x10\x84\x10\x84\x10\x84\x10\xa4\x10\x83\x10\xa4\x10\x84\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x08\xa4\x10\xa4\x10\xa4\x10\xa3\x10\x84\x10\x84\x10\xa4\x10\xc4\x10\xa4\x10\xa4\x10\x84\x10\xa4\x10\x84\x10\x84\x10\x83\x08c\x08\x83\x08\xa4\x10\xe5\x18\xe5\x10\xe5\x10\xe5\x10\xc5\x10\xc5\x10\xc5\x10\xc5\x10\xc5\x10\xc5\x10\xc5\x10\xc5\x10\xc5\x10\xc5\x10\xe5\x10\xe6\x10\xe6\x18\xe6\x18\xe5\x18\xe5\x10\xe5\x10\xe5\x10\xe5\x10\x05\x11\x05\x11\x06\x19\xe5\x18\xe6\x18\xe6\x18\xe6\x18\x06\x11\x06\x11\xe6\x10\x06\x11\x06\x11\x06\x11\x06\x11\x06\x11\x06\x11\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\xe6\x18\x06\x19\x06\x19\x06\x19\x06\x11\x06\x11\x06\x11\xe6\x10\xe6\x18\xe6\x18\xe6\x18\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19&\x19\x06\x19\x06\x19\x06\x19\x06\x19\xe6\x18\x06!KRU\xa5\xda\xd6\xfa\xde\xfa\xde\xfa\xde\xfa\xde\xfa\xde\xfa\xde\xfa\xde\xfa\xde\xfa\xde\xfa\xde\xda\xde\xda\xde\xfa\xde\xfa\xde\xda\xde\xd9\xde\xd9\xd6\xd9\xd6\xd9\xd6\xb9\xd6\xb9\xd6\xb9\xd6\xb9\xd6\xb8\xd6\x98\xd6\x98\xce\x98\xce\x98\xcex\xcex\xcex\xc6X\xc6W\xc67\xc67\xbe\x17\xbe\x16\xbe\xf6\xb5\xf6\xb5\xf6\xb5\xd6\xb5\xd6\xad\xb5\xad\x95\xad\x95\xad\x95\xa5t\xa5t\xa5T\x9dT\x9d4\x9d3\x9d3\x9d\x13\x9d\x13\x9d\xf2\x9c\xf2\x94\xd2\x94\xd2\x94\xd2\x94\xd2\x94\xd1\x94\xb1\x94\xb1\x94\xb1\x94\x91\x94\x91\x8c\x90\x8c\x90\x8cp\x8co\x8co\x8cO\x8cO\x84O\x84.\x84.\x84.\x84\x0e\x84\r|\r|\xed{\xed{\xcc{\xcc{\xcc{\xac{\xac{\xab{\x8b{\x8bs\xe79IJ\xaaR\xabR\xabR\xabR\xcbR\x08:\xc4\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x83\x10\x84\x10\x84\x10\x84\x10\x84\x10\x84\x10\x84\x10\xa4\x10\x84\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\x84\x08\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa3\x10\x83\x10\x84\x10\x84\x10\xa4\x10\xc4\x10\xc5\x10\xc4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\xa4\x10\x84\x08c\x08\x84\x10\xc5\x10\xe5\x10\xe5\x10\xe5\x10\xe5\x10\xc5\x10\xc5\x10\xc5\x10\xc5\x10\xc5\x10\xc5\x10\xa5\x10\xc5\x10\xc5\x10\xc5\x10\xe5\x10\xe6\x18\xe6\x18\xe6\x18\x06\x19\xe6\x18\x05\x19\xe5\x10\xe5\x10\x05\x11\x06\x19\xe6\x18\xe6\x18\x06\x19\x06\x19\x06\x11\x06\x11\x06\x11\xe6\x10\x06\x11\x06\x11\x06\x11\x06\x11\x06\x11\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x19\x06\x11\xe6\x18\xe6\x18\xe6\x18\xe6\x18\x06'
soundimage.write(headerbytes)
sound.seek(44)

for pixels in range (1,1600044):
    bytep=sound.read(1)
    soundimage.write(bytep)
sound.close
soundimage.close
    
    