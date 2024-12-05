from os import chdir, path, rename, listdir, makedirs
from PIL import Image

dir_path = path.dirname(path.realpath(__file__))
chdir(dir_path)
thesefiles = listdir()
target = ".png"
target_size = 970 # max dimension of image, < 1 means no resize
new = ".jpg"
colorspace = 'RGB' # 'L' is black and white, 'RGB' is color

# filename = input("node name: ") # set to "" to not rename files
filename = "FledgelingPeripheral"

offset = 51 #47 #43 #35 #26


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
                newdim = (int(d*scale) for d in cursize)
                image = image.resize(newdim)
        if len(filename):
            name = filename + str(i+offset) + new
        else:
            name = f[:-tlen] + new
        if False:#True: #move the originals to the backup folder
            m = newdir + f
            try: rename(f, m)
            except: pass
        image.save(name)
        #image.save(imagesfolder + name)
        print("processed", f)
    else:
        pass
        #print(f)

f = open("ImageFormatConverterSequence.py","r")
scriptText = f.read()
f.close()
newoff = offset + i
print(newoff)
scriptText = scriptText.replace(f"offset = {offset}",f"offset = {newoff} #{offset}")
f = open("ImageFormatConverterSequence.py","w")
f.write(scriptText)
f.close()

