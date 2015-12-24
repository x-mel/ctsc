from Tkinter import *
import math

# The root window
root = Tk()

# In this part we will initialize some lists that will serve us later
# so that we don't have to enter each value alone. This saves LOTS of
# valuable time especially if you want to expand the program

list= ["Radius of the Primary", "Radius of the Secondary","Distance between the 2 mirrors", "Distance between the Focal point and Primary", "Distance between the Focal point and Secondary", "Focal length", "Position of the 1st Nodal Point","Position of the 2nd Nodal Point" ,"Position of the 1st Principle Point", "Position of the 2nd Principle Point"]

# This is the list of Labels that consitute the First Column in the 
# window 
label= []

# This is the list of entries where you can input numbers, located as the second column in the window
entry= []

# This is the list of results (they are acutally list of variable labels)
# that depend on valabel[] list down there.
result=[]

# This is a list of variable text, that contains the results, and used
# with result[] to set the output
valabel=[StringVar() for i in range(len(list))]

# tac is the welcome message, it is a variable because
# it was intended to change if the input was wrong or 
# inconvenient so it can help diaognise the problem
# I named it tac because I was listening to Mashrou' Leila
# Guess what song? :P
tac=StringVar()

# This is the welcome label, based on the text included in tac
l=Label(root, textvariable=tac, width=70, fg="white", bg="dark grey")
l.grid(row=0, columnspan=3)
tac.set("WELCOME, Please enter 3 non null values, then Go For It")

# In this section we will be creating most of the widgets
# in the window. You can see how short is the code, usually
# this should've taken at least 100 lines!
for i, n in enumerate(list):
    # For each value in list[] we will be adding a label to label[]
    label.append(Label(root, text=n, width=40))
    # Here we actually display the label inside the window
    label[i].grid(row=i+1, column=0)
    if i<6:
        # We configure the entry widgets for our paramenters
        entry.append(Entry(root, width=10))
        entry[i].grid(row=i+1, column=1)
    # This is the 3rd column where we can add the output    
    result.append(Label(root, textvariable=valabel[i], width=15, relief='sunken',bg='light blue'))
    result[i].grid(row=i+1, column=2)

def testf(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

# Calc() is the function that defines the job of the button Go For It    
def calc():
    # error is the variable used to diagnize and see if the user doesn't
    # troll and enter stupid values like strings and 0
    error=0
    # we put -4 because we only want it to run for the number of entries    
    for i in range(len(list)-4):
        # we check if the input is actually a number
        # if(bool((entry[i].get()).isdigit())==False):
        # we didn't use isdigit(), it doesn't work on negative numbers
        if testf(entry[i].get())==False:
            # If not it will check if the user entered a character by
            # examining the length of the input
            if(len((entry[i].get()))!=0):
                # If the user entered a character, it means he's trolling
                # So we stop the program
                error=-2
                break
            # If not it means it was empty so we increase the error
            else:
                error= error + 1
        # If the input was a digit we check if it was a zero
        else:
            # If it was a zero, the user is trolling again so we stop
            # the program
            if(int(entry[i].get())==0):
                error=-1
                break
    # Here depending on the value of error, we set the welcome message
    # to guide the user in case of an error        
    if error>3:
        l.config(fg="red")
        tac.set('Please enter at LEAST 3 values, I am not not Michel Hayek')
    elif error==-2:
        l.config(fg="red")
        tac.set('Please enter 3 NUMERICAL VALUES, how can I calculate with a character!')        
    elif error==-1:
        l.config(fg="red")
        tac.set("Please enter 3 NON NULL Numbers, really Zeros aren't that helpful")
         
#####################################################
# If everything is alright then we start the program!
#           Alright, Alright, Alright ...
#####################################################
    
    else:
        l.config(fg="white")
        tac.set("Thanks for using me :)" )
        
        # we save the input which is a string in a list a[]
        a= [entry[i].get() for i in range(len(list)-4)]
        
        # j helps us defining m which is the james bond of our program
        j=2
        m=0
        for i, v in enumerate(a):
    # we could use if bool(v)==true instead of len(v)        
            if (len(v)!=0):
                a[i]=float(v)
                m=(i+1)*10**j+m
                j=j-1
                
    # m is a smart index ;)
    # what is m?
    # check your papers! Too long to explain here
    
        #m1=m
        
        # So basically now based on m, we have simplified our program
        # it runs without iterating and defines all the other values!
              
        if(m>200):
            if m==234:
                a[0]= (a[1]*a[3] + 2*a[2]*a[3]) / (a[3]-0.5*a[1]-a[2])            
            elif m==235:
                a[0]= (a[1]*a[4] + 2*a[2]*a[4] + a[1]*a[2]) / (a[4]+0.5*a[1])        
            elif m==236:
                a[0]= (2*a[2]*a[5] + a[5]*a[1]) / (a[5]+ 0.5*a[1])            
            elif m==245:
                a[0]= (-a[1]**2 - a[1]* math.sqrt(a[1]**2 -8*a[3]*(2*a[4] + a[1])))/(4*a[4] + 2*a[1])
            elif m==256:
                a[0] = (a[5]*a[1]) / (a[4]+0.5*a[1])
            elif m==246:
                a[0]= -a[3]*a[1] / (a[5] + 0.5*a[1])
            elif m==346:
                a[0]= (2*a[2]*a[3]) / (a[5] + a[3] -a[2])
            elif m==356:
                a[0]= (2*a[2]*a[5]) / (a[5]-a[4])
            elif m==456:
                a[0]= (2*a[4]*a[3] + 2*a[5]**2) / (a[5]-a[4])
            elif m==345:
                a[0]=((-2*a[2]*(a[2]-2*a[3]))+math.sqrt((-2*a[2]*(a[2]-2*a[3]))**2 -4*(a[4]+a[3]-a[2])*(4*a[3]*a[2]**2)))/(2*(a[4]+a[3]-a[2])) 
                        
            # Since for some cases of m, the next value of the variables
            # cannot be defined if we can't change m, so we do it!
            if m>300:
                m=int(str(m).replace(str(m)[0], '1'))
                
        if (m<200):
            if m==134:
                a[1]= (a[0]*a[3]-2*a[2]*a[3]-a[0]*a[2])/(a[3]+0.5*a[0])
            elif m==135:
                a[1]= (-2*a[2]*a[4] + a[0]*a[4])/ (a[4]+a[2]-0.5*a[0])
            elif m==136:
                a[1]= (2*a[2]*a[5]-a[5]*a[0])/(0.5*a[0]-a[5])
            elif m==145:
                a[1]= (-a[0]**2 + a[0]* math.sqrt(a[0]**2 -8*a[4]*(2*a[3] + a[0])))/(4*a[3] + 2*a[0])
            elif m==146:
                a[1]= -2*a[0]*a[5]/(2*a[3]+a[0])
            elif m==156:
                a[1]= 2*a[0]*a[4]/(2*a[5]-a[0])                
            
            # Same as above
            if m>140:
                m=int(str(m).replace(str(m)[1], '2'))
                
        if (m<130):
            if m==124:
                a[2]= (a[0]*a[3]-a[1]*a[3]- 0.5*a[0]*a[1])/(2*a[3]+ a[0])
            elif m==125:
                a[2]= (a[0]*a[4]-a[1]*a[4]+ 0.5*a[0]*a[1])/(2*a[4]+ a[1])
            elif m==126:
                a[2]= (a[0]*a[5]-a[1]*a[5]+ 0.5*a[0]*a[1])/(2*a[5])
      
        # So after we determined the first 3 variables, we can get the
        # the others from the elements of the matrix of ray tracing
        # from previous homework (check your dropbox folder)
        
        C= (2*a[0]-4*a[2]-2*a[1])/(a[0]*a[1])
        D= (a[1]+2*a[2])/a[1]
        A= (a[0]-2*a[2])/a[0]
        
        a[3]=D/C
        a[4]=-A/C
        a[5]=-1/C
        
        # To get the last 3 values, we have to extend a[] because
        # it included previously only the value of the entries
        a.extend(((D-1)/C, -(1+A)/C, (D+1)/C, (1-A)/C))
        
        # And finally now we set the values saved in a[] to the labels
        for i in range(len(list)):
            valabel[i].set(round(a[i],5))

# This is the function of the button clear        
def clear():
    for i in range(len(list)):
        valabel[i].set('')

# We place the buttons on the window
Button(root, text="Go for it", bg="white", relief='raised', command=calc, width=7).grid(row=len(list)+1,column=1)

Button(root, text="Clear", bg="light grey", relief='raised', command=clear, width=12).grid(row=len(list)+1, columnspan=2, column=2)    

root.mainloop()




"""
______  _________________ 
___   |/  /__  ____/__  / 
__  /|_/ /__  __/  __  /  
_  /  / / _  /___  _  /___
/_/  /_/  /_____/  /_____/

"""
