from os import chdir, path, rename, listdir, makedirs
from PIL import Image

dir_path = path.dirname(path.realpath(__file__))
chdir(dir_path)
thesefiles = listdir()
target = ".png"
target_size = 800 # max dimension of image, < 1 means no resize
new = ".jpg"
colorspace = 'RGB' # 'L' is black and white, 'RGB' is color

filename = input("node name: ") # set to "" to not rename files


newdirname = "Original_"+target[1:].upper()+"s"
newdir = f"./{newdirname}/"
imagesfolder = "../images/"
tlen = len(target)
if not newdirname in thesefiles:
    makedirs(newdir)
i = 0
for f in thesefiles:
    if f[-tlen:] == target:
        i += 1
        image = Image.open(f)
        image = image.convert(colorspace)
        if target_size >= 1:
            cursize = (image.width, image.height)
            maxdim = max(cursize)
            scale = target_size/maxdim
            if scale < 1:
                newdim = (int(i*scale) for i in cursize)
                image = image.resize(newdim)
        if len(filename):
            name = filename + str(i) + new
        else:
            name = f[:-tlen] + new
        if True: #move the originals to the backup folder
            m = newdir + f
            try: rename(f, m)
            except: pass
        image.save(name)
        image.save(imagesfolder + name)
        print("processed", f)
    else:
        pass
        #print(f)
# update the HTML with the correct number of images

f = open("../fledgeling_game.html","r", encoding="utf-8")
text = f.read()
f.close()
text = text.replace(filename+"= new Array(0, ",filename + f"= new Array({i}, ")
f = open("../fledgeling_game.html","w", encoding="utf-8")
f.write(text)
f.close()
