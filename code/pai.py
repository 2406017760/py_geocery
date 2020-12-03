import math
from tqdm import tqdm
from random import random
import time
DARTS=1000000000
hits=0
start=time.perf_counter()
for i in tqdm(range(1,DARTS+1)):
   x,y=random(),random() 
   dist=pow(x**2+y**2, 0.5)
   if dist<=1:
        hits=hits+1
end=time.perf_counter()
t=end-start
pi=4*(hits/DARTS)
print("Pi值是{}.".format(pi))
print("运行时间:%.2f秒"%t)
