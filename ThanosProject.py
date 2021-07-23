import os,random
path="C:/Users/P.Botros/Desktop/CDSP/New folder/New folder/New folder/Universe"
all_imgs=os.listdir(path)
random_list=[]
i=0
while i<25:
    d=random.choice(all_imgs)
    if d not in random_list:
          random_list.append(d)
    i=len(random_list)
for n in random_list:
    os.remove(path+'/'+n)