import random

pop=[]
new_pop=[]
def population():
    size=50
    for i in range(size):
        x=random.randint(0,995)
        y=random.randint(0,477)
        pop.append([x,y])
def fittness(x,y):
    if(x<(width-width1)and y<(height-height1)):
        slice=img1_array[y:y+height1,x:x+width1]
        fit.append((scipy.stats.kendalltau(img2_array, slice).correlation,x,y))

def crossover(fit):
    pop.clear()
    for i in range(0,len(pop),2):
        x1 = bin(fit[i][1])
        y1 = bin(fit[i][2])
        x2 = bin(fit[i+1][1])
        y2 = bin(fit[i+1][2])

        c1=x1[2:]+y1[2:]
        c2=x2[2:]+y2[2:]


        ran=random.randint(1,len(c1)-1)
        ran1=random.randint(1,len(c2)-1)
        x1=c1[0:ran]
        y1=c1[ran:]
        x2=c2[0:ran1]
        y2=c2[ran1:]
        while(int(x1,2)>995 or int(x2,2)> 995 or int(y1,2)>477 or int(y2,2)>477):
            ran=random.randint(1,len(c1)-1)
            ran1=random.randint(1,len(c2)-1)
            x1=c1[0:ran]
            y1=c1[ran:]
            x2=c2[0:ran1]
            y2=c2[ran1:]

        pop.append([int(x1,2),int(y1,2)])
        pop.append([int(x2,2),int(y2,2)])
    fit.clear()





population()
crossover(pop)
print(new_pop)
