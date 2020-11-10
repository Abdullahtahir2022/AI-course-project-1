from PIL import Image,ImageFilter
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import random

thisdict = {
  0.5: "Ford",
  0.0: "Mustang",

}
#Declaration of all used variables
pop=[]
fit=[]
k=0
x=[]
y=[]
avg1=[]
sum=0
img1 = Image.open('groupGray.jpg')
img2 = Image.open('boothiGray.jpg')
img1_array=np.array(img1)
img2_array=np.array(img2)
width, height = img1.size
width1, height1 = img2.size


def population(x):
    size=x
    for i in range(size):
        x=random.randint(0,width-width1)
        y=random.randint(0,height-height1)
        pop.append([x,y])
    print("Generation No." ,k )
    return pop


def fittness():
    for i in pop:
        slice=img1_array[i[1]:i[1]+height1,i[0]:i[0]+width1]
        fit.append([scipy.stats.kendalltau(img2_array, slice).correlation,i[0],i[1]])
    fit.sort(key = lambda x: x[0], reverse=True)



def fittness1(x,y):
    slice=img1_array[y:y+height1,x:x+width1]
    return scipy.stats.kendalltau(img2_array, slice).correlation


def display(x,y):
    '''slice=img1_array[y:y+height1,x:x+width1]'''
    fig,ax = plt.subplots(1)
    rect = patches.Rectangle((x,y),width1,height1, edgecolor='b', facecolor="none")

    ax.imshow(img1_array,cmap="gray")
    ax.add_patch(rect)
    plt.show()


def bits(x):
    if(10-len(x)>0):
        z=10-len(x)
        x=('0'*z)+x
    return x

def cross_bits(x1,y1,x2,y2):
    if(10-len(x1)>0):
        z=10-len(x1)
        x1=('0'*z)+x1

    if(10-len(y1)>0):
        z=10-len(y1)
        y1=('0'*z)+y1

    if(10-len(x2)>0):
        z=10-len(x2)
        x2=('0'*z)+x2

    if(10-len(y2)>0):
        z=10-len(y2)
        y2=('0'*z)+y2
    return x1,y1,x2,y2





def crossover():
    pop.clear()
    for i in range(0,len(fit),2):
        x1 = bin(fit[i][1])[2:]
        y1 = bin(fit[i][2])[2:]
        x2 = bin(fit[i+1][1])[2:]
        y2 = bin(fit[i+1][2])[2:]
        x1,y1,x2,y2=cross_bits(x1,y1,x2,y2)
        c1=x1+y1
        c2=x2+y2
        ran=random.randint(1,len(c1)-1)
        ran1=random.randint(1,len(c2)-1)
        x1=c1[0:ran]
        y1=c1[ran:]
        x2=c2[0:ran1]
        y2=c2[ran1:]
        while(int(x1,2)>width-width1 or int(x2,2)> width-width1 or int(y1,2)>height-height1 or int(y2,2)>height-height1):
            ran=random.randint(1,len(c1)-1)
            ran1=random.randint(1,len(c2)-1)
            x1=c1[0:ran]
            y1=c1[ran:]
            x2=c2[0:ran1]
            y2=c2[ran1:]

        ran2=random.randint(0,1)
        if(ran2==0):
            if(fittness1(int(x1,2),int(y2,2))>fittness1(fit[i][1],fit[i][2])):
                pop.append([int(x1,2),int(y2,2)])
            else:
                pop.append([fit[i][1],fit[i][2]])
            if(fittness1(int(x2,2),int(y1,2))>fittness1(fit[i][1],fit[i][2])):
                pop.append([int(x2,2),int(y1,2)])
            else:
                pop.append([fit[i][1],fit[i][2]])
        elif(ran2==1):
            if(fittness1(int(x2,2),int(y1,2))>fittness1(fit[i][1],fit[i][2])):
                pop.append([int(x2,2),int(y1,2)])
            else:
                pop.append([fit[i][1],fit[i][2]])
            if(fittness1(int(x1,2),int(y2,2))>fittness1(fit[i][1],fit[i][2])):
                pop.append([int(x1,2),int(y2,2)])
            else:
                pop.append([fit[i][1],fit[i][2]])
    fit.clear()

def random1(y,z,x):
    co=fittness1(y,z)
    mutation_rate=50
    if(co>0):
        t=int(len(x)-((mutation_rate/100)*len(x)))
        ran4=random.randint(t,len(x)-1)
    else:
        t=int(len(x)-((mutation_rate/100)*len(x)))
        ran4=random.randint(0,t)
    return ran4



def mutation():
    for i in range(0,len(pop)):
        ran3=random.randint(0,1)

        if(ran3==0):
            x = bin(pop[i][0])[2:]
            x=bits(x)
            ran4=random1(pop[i][0],pop[i][1],x)
            if(x[ran4]=='1'):
                x1=list(x)
                x1[ran4]='0'
                x = ''.join(x1)
            else:
                x1=list(x)
                x1[ran4]='1'
                x = ''.join(x1)
            while(int(x,2)>width-width1):
                ran4=random1(pop[i][0],pop[i][1],x)
                if(x[ran4]=='1'):

                    x1=list(x)
                    x1[ran4]='0'
                    x = ''.join(x1)
                else:
                    x1=list(x)
                    x1[ran4]='1'
                    x = ''.join(x1)
            pop[i][0]=int(x,2)




        if(ran3==1):
            y = bin(pop[i][1])[2:]
            y=bits(y)
            ran4=random1(pop[i][0],pop[i][1],y)
            if(y[ran4]=='1'):
                y1=list(y)
                y1[ran4]='0'
                y = ''.join(y1)
            else:
                y1=list(y)
                y1[ran4]='1'
                y = ''.join(y1)
            while(int(y,2)>height-height1):
                ran4=random1(pop[i][0],pop[i][1],y)
                if(y[ran4]=='1'):
                    y1=list(y)
                    y1[ran4]='0'
                    y = ''.join(y1)
                else:
                    y1=list(y)
                    y1[ran4]='1'
                    y = ''.join(y1)
            pop[i][1]=int(y,2)










size=250
correlation=0.5
pop=population(size)
fittness()
while(fit[0][0]<correlation):
    crossover()
    mutation()
    fittness()
    #for generation no.
    k+=1
    print("-----------------")
    print("Generation No. ",k)



    #for graph
    x.append(k)
    y.append(fit[0][0])
    #Average Calculation
    for l in range(len(fit)):
        sum=sum+fit[l][0]
    avg=sum/len(fit)
    avg1.append(avg)
    sum=0
    print("Average of Coorelation ",avg)
    print("-----------------")


#plots
plt.plot(avg1)
plt.plot(x, y)
#baba picture
display(fit[0][1],fit[0][2])
