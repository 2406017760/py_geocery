import random
import hero_name
import tkinter 
import time
hero_name.sp_name.append(hero_name.ssr_name)
i=random.uniform(0,100)
def get():
   if (59<i<=60):
      return ("哇！在抽签中获得了"+random.choice(hero_name.sp_name))
   if (i<=19):
      return ("恭喜你 ！ 获得了 SR 式神"+random.choice(hero_name.sr_name))
   else:
      return ("恭喜你 ！ 获得了 R 式神"+random.choice(hero_name.r_name))

def ten_get():
   s=""
   for a in range(0,10):
      i=random.uniform(0,100)
      if (59<i<=60):
         s+= ("\n>>===阴阳师鸿运当头，召唤出了"+random.choice(hero_name.sp_name)+"！！！===<<\n")
      elif (i<=19):
         s+= ((" SR "+random.choice(hero_name.sr_name)))
      else:
         s+= ((" R "+random.choice(hero_name.r_name)))
   return s
window =tkinter.Tk()
window.title("阴阳师")
window.geometry("800x300")
var1=tkinter.IntVar()
var1=9999
b1=tkinter.Label(window,text="阴阳师抽符系统" ,fg='black', font=('Arial', 10),height=2,width=20)
b1.pack()
var=tkinter.StringVar()
l=tkinter.Label(window,justify="left",textvariable=var,wraplength='800',bg='pink', fg='black', font=('Arial', 12), width=90, height=5)
l.pack()
on_hit =False
def hit():
   global on_hit,var1
   if on_hit == False:
      on_hit = True
      var.set(get())
   else:
      on_hit = False
      var.set(get())
b = tkinter.Button(window, text='单抽', font=('Arial', 12),bg="RoyalBlue", width=6, height=4, command=hit)
b.place(x=250,y=150)
on_hit1 =False
def ten_hit():
   global on_hit1,var1
   if on_hit1 == False:
      on_hit1 = True
      var.set(ten_get())
   else:
      on_hit1 = False
      var.set(ten_get())
   var1.set(var1-10)
c = tkinter.Button(window, text='十连抽', font=('Arial', 12),bg="RoyalBlue", width=6, height=4, command=ten_hit)
c.place(x=450,y=150)

window.mainloop()