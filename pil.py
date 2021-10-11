from PIL import Image#引入PIL库中的Image类
import os#引入os 模块

picture=input("请输入图片的名称以及格式：")
image=Image.open(picture)
size=os.path.getsize(picture)/1024
width,height=image.size

ima=input("请输入修改后的图片名称和格式：")
while True:
    if size>10:
        width,height=round(width*0.9),round(height*0.9)#去掉浮点，防报错
        image=image.resize((width,height),Image.ANTIALIAS)
        image.save(ima)
        size=os.path.getsize(ima)/1024
    else:
        break
print(size)
