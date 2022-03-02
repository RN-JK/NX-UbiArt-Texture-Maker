import os, glob

dir = 'input/temp'

try:
    os.makedirs(dir)

except:
    pass

try:
    for dds in os.listdir("input/"):
        os.system("xtx_extract -o input/temp/"+dds.replace(".dds",".xtx")+" input/"+dds)
    
        ckdoutput=open("output_pngckd/"+dds.replace(".dds",".png.ckd"),"wb")
        ckdoutput.write(b'\x00\x00\x00\x09\x54\x45\x58\x00\x00\x00\x00\x2C\x00\x00\x20\x80\x01\x00\x01\x00\x00\x01\x18\x00\x00\x00\x20\x80\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\xCC\xCC')

        with open("input/temp/"+dds.replace(".dds",".xtx"), "rb") as f:
            xtxdata=f.read()

        ckdoutput.write(xtxdata)
        ckdoutput.close()

except:
    pass

filelist = glob.glob(os.path.join(dir, "*"))
for f in filelist:
    os.remove(f)

os.rmdir(dir)

