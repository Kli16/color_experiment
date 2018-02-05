import random as r

def create_image ():

    f = open('image.ppm','w')
    f.write('P3 600 600 255 ')

    for i in range(600):
        for j in range (600):
            f.write("%d %d 155 " % (155 - i, 255 - j))

    f.close()

if __name__  == "__main__":
    create_image()
