from PIL import Image,ImageFilter
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import random

def random1(x):
    if(x>0.5):
        t=(33/100)*len(x)
        ran4=random.randint(t,len(x)-1)
    elif(x>0.0 and x<0.5):
        t=(50/100)*len(x)
        ran4=random.randint(t,len(x)-1)
    elif(x<0.0):
        t=(50/100)*len(x)
        ran4=random.randint(0,t)
    return ran4


class MODEL:

    def __init__(self, big_img, small_img):
       self.Generation_count=0
       self.big=0
       self.small=0
       self.pop=[]
       self.size = 0
       self.fit=[]
       self.img1 = Image.open(big_img)
       self.img2 = Image.open(small_img)
       self.img1_array=np.array(self.img1)
       self.img2_array=np.array(self.img2)
       self.width, self.height = self.img1.size
       self.width1, self.height1 = self.img2.size

    def population(self,s):
        self.size=s
        for i in range(self.size):
            x=random.randint(0,self.width-self.width1)
            y=random.randint(0,self.height-self.height1)
            self.pop.append([x,y])

        print("Generation: ", self.Generation_count)
        return self.pop


    def fittness(self,pop):
        for x in pop:
            print(x[0],x[1])
            slice=self.img1_array[x[1]:x[1]+self.height1,x[0]:x[0]+self.width1]
            self.fit.append((scipy.stats.kendalltau(self.img2_array, slice).correlation,x[0],x[1]))
        self.Generation_count+=1
        print("Generation: ", self.Generation_count)
        self.fit.sort(key = lambda x: x[0], reverse=True)
        return self.fit




    def display(self,x,y):
        '''slice=img1_array[y:y+height1,x:x+width1]'''
        fig,ax = plt.subplots(1)
        rect = patches.Rectangle((x,y),self.width1,self.height1, edgecolor='b', facecolor="none")

        ax.imshow(self.img1_array,cmap="gray")
        ax.add_patch(rect)
        plt.show()

    def crossover(self,fit):
        print(len(pop),"pop")
        print(len(fit),"fit")
        self.pop.clear()
        for i in range(0,len(self.fit),2):
            self.pop.append([fit[i+1][1],fit[i][2]])
            self.pop.append([fit[i][1],fit[i+1][2]])
        return self.pop


    def mutation(self,pop):
        print("hello")
        for f in range(0,len(self.pop),1):




        print("-------------------------------------------")
        print(len(pop),"pop")
        print(len(fit),"fit")
        print("--------------------")
        self.fit.clear()
        return self.pop






obj=MODEL('groupGray.jpg','boothiGray.jpg')
correlation=0.5



pop=obj.population(52)
fit=obj.fittness(pop)

while(fit[0][0]<correlation):
    new_pop=obj.crossover(fit)
    variation=obj.mutation(new_pop)
    fit=obj.fittness(variation)




obj.display(fit[0][1],fit[0][2])
