import random, os

def gen_qrcode_id():
    constant = True
    id = ''
    while constant:
        for i in range(10):
            id = id+str(random.randint(0, 9))
        if id+'.png' in os.listdir('./archives/images/qrcodes'):
            constant = True
        else:
            return id
        