import shutil,os
clean=['\PictureTemp','\Bike','\Blind']
for x in clean:
    shutil.rmtree(os.getcwd()+x)
    os.mkdir(os.getcwd()+x)
