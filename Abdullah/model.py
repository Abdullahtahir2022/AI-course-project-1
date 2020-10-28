from PIL import Image,ImageFilter
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import random
#Read image
pop=[]
fit=[]
img1 = Image.open('groupGray.jpg')
img2 = Image.open('boothiGray.jpg')
img1_array=np.array(img1)
img2_array=np.array(img2)
width, height = img1.size
width1, height1 = img2.size


def population():
    size=int(((width*height)*10)/100000)
    for i in range(size):
        x=random.randint(0,width)
        y=random.randint(0,height)
        if(x<(width-width1)and y<(height-height1)):
            pop.append([x,y])



def fittness(x,y):
    if(x<(width-width1)and y<(height-height1)):
        slice=img1_array[y:y+height1,x:x+width1]
        fit.append((scipy.stats.kendalltau(img2_array, slice).correlation,x,y))

def display(x,y):
    '''slice=img1_array[y:y+height1,x:x+width1]'''
    fig,ax = plt.subplots(1)
    rect = patches.Rectangle((x,y),width1,height1, edgecolor='b', facecolor="none")

    ax.imshow(img1_array,cmap="gray")
    ax.add_patch(rect)
    plt.show()

def cross_and_mutate(fit):
    pop.clear()
    list1=[0,1]
    list2=[5,-5]
    for i in range(0,len(fit)-1,2):
        pop.append([fit[i+1][1],fit[i][2]])
        pop.append([fit[i][1],fit[i+1][2]])
        if(random.choice(list1)==0):
            x1=pop[i][0]+random.choice(list2)
            x2=pop[i+1][0]+random.choice(list2)
            if(x1>=0 and x2>=0 and x1<(width-width1) and x2<(width-width1)):
                pop[i][0]=x1
                pop[i+1][0]=x2
        if(random.choice(list1)==1):
            y1=pop[i][1]+random.choice(list2)
            y2=pop[i+1][1]+random.choice(list2)
            if(y1>=0 and y2>=0 and y1<(width-width1) and y2<(width-width1)):
                pop[i][1]=y1
                pop[i+1][1]=y2
    fit.clear()


j=0
correlation=0.5
population()
print("Generation: ", j)
for i in pop:
    fittness(i[0],i[1])
fit.sort(key = lambda x: x[0], reverse=True)
while(fit[0][0]<correlation):
    cross_and_mutate(fit)
    for i in pop:
        fittness(i[0],i[1])
    fit.sort(key = lambda x: x[0], reverse=True)
    j+=1
    print("Generation: ", j)


print("found in ",j, "Generation")
display(fit[0][1],fit[0][2])
