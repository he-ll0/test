from tkinter import* 
import tkinter.messagebox 
from tkinter import ttk
import tkinter as tk #Imporing tkinter GUI library modules (Codemy.com, 2019)

def main(): #Opens welcome page window (Breuss, 2022)
    root= Tk() #Assigns 'root' to tkinter/Tk
    app= homeWindow(root) #instantiates Home Window Class

class homeWindow: #Main window: Home Window Class
    def __init__(self,master):
        self.master= master
        self.userEmailVar = StringVar()
        self.userNameVar = StringVar()
        self.userDateVar = StringVar()
        self.userTitleVar = StringVar()
        self.userPriorityVar = StringVar() #Assigning form entries to variables/attributes (My SWE Space, 2021)
        
        #Formatting Home Window:
        self.master.title("Home Window")
       
        self.master.config(bg= '#9ad1d4')
        
        self.master.geometry("1000x800+0+0")#Formatting the window(Codemy.com, 2019)
    
        self.homeWindowTitle = Label(master, text = 'TE Portal Home Window', font=('Calibri', 30,'bold'),
                              bd=1, relief="sunken",
                              bg='#80CED7', fg='#ffffff').pack(pady=0, ipady=10, ipadx=10)#Title formatting in window(Codemy.com, 2020)
        
        #Help window button:        
        self.helpWindowButton=Button(master, text="Help Window", highlightbackground= '#eeeeee',font=('Calibri',16),command=self.openHelpWindow).pack(pady=5)
        #Labels and entry boxes for request form:
        self.emailLabel= Label(master, text="Insert Requester Email:", bg='#52b69a',font=('Calibri',14)).pack()
        self.userEmail= Entry(master,width=40,font=('Calibri',14),textvariable=self.userEmailVar).pack(pady=5)
        self.nameLabel= Label(master, text="Insert Requester Name:", bg='#52b69a',font=('Calibri',14)).pack()
        self.userName= Entry(master,width=40,font=('Calibri',14),textvariable=self.userNameVar).pack(pady=5)
        self.dateLabel= Label(master, text="Insert Date of Request (DD/MM/YYYY):", bg='#52b69a',font=('Calibri',14)).pack()
        self.userDate= Entry(master,width=40,font=('Calibri',14),textvariable=self.userDateVar).pack(pady=5)
        self.titleLabel= Label(master, text="Insert Title of Request:", bg='#52b69a',font=('Calibri',14)).pack()
        self.userTitle= Entry(master,width=40,font=('Calibri',14),textvariable=self.userTitleVar).pack(pady=5)
        self.priorityLabel= Label(master, text="Insert Priority Level for Request (Low/Medium/High):", bg='#52b69a',font=('Calibri',14)).pack()
        self.userPriority= Entry(master,width=40,font=('Calibri',14),textvariable=self.userPriorityVar).pack(pady=5)
        self.requestDescriptionLabel= Label(master, text="Insert Description of Request:", bg='#52b69a',font=('Calibri',14)).pack()#Labels (Codemy.com, 2020a)
        self.userRequest= Text(master, width=80,height=10, font=('Calibri',12))
        self.userRequest.pack(pady=5)#Text box (Codemy.com, 2020b)
        #Submit Request Button:
        self.submitRequestButton= Button(master, text="Submit Request", font=('Calibri',14), command=self.requestValidation).place(x=850,y=500)
        
    def requestValidation(self): #Assigns form entries to variables
        userEmail = (self.userEmailVar.get())
        userName = (self.userNameVar.get())
        userDate = (self.userDateVar.get())
        userTitle = (self.userTitleVar.get())
        userPriority = (self.userPriorityVar.get())
        userRequestVar= self.userRequest.get(1.0,END)#Retrieving data from text box widget (Codemy.com, 2020b)

        requestList = [userEmail,userName,userDate,userTitle,userPriority,userRequestVar] #Grouping form components to a list (Pankaj, 2022)
        atSymbol = '@'
        def saveForm():
            tePortalRequestsFile = open('TePortalRequestsFileExample.txt', 'w')
            for item in requestList:
                tePortalRequestsFile.write(item+",") #Writing to an exernal file (Jana, 2022)
            
            tePortalRequestsFile.close()
            succesfullFormMessage=tkinter.messagebox.showinfo('Success Message', 'Your request form was successfully saved.') #Popup boxes (Ajay, 2020)
            
        if atSymbol not in userEmail:#'@' symbol check in email (JavaTPoint, 2021)     
            errorMessage=tkinter.messagebox.showinfo('Error Message','Email is missing an @.')

        if userRequestVar=="\n": #Presence check (JavaTPoint, 2021)
            errorMessage=tkinter.messagebox.showinfo('Error Message','Request Description box is empty.')

        for i in requestList: #Presence check (Pavitra, 2020)
            if not i:
                errorMessage=tkinter.messagebox.showinfo('Error Message', 'An input field is empty.') #Popup boxes (Ajay, 2020)

        else:
            saveForm()


            
        
    def openHelpWindow(self): #Links the Home Window to the Help Window (My SWE Space, 2021)
        self.homeWindow= Toplevel(self.master)
        self.app= helpWindow(self.homeWindow)
       
class helpWindow(object): #Second Window: Help Window Class
    def __init__(self,master):
        self.master= master
        self.master.title("Help Window")
        self.master.config(bg= '#9ad1d4')
        self.master.geometry("1000x700+0+0")#Formatting of window(Codemy.com, 2019)
    
        self.helpWindowTitle = Label(master, text = 'TE Portal Help Window', font=('arial', 30,'bold'),
                              bd=1, relief="sunken",
                              bg='#80CED7', fg='#ffffff').pack(pady=20, ipady=10, ipadx=10)#Title formatting in window(Codemy.com, 2020)
        self.helpDescriptionText= Label(master, text="[Help Description Text Inserted Here]", bg='#ffffff',font=('Calibri',14)).pack()
        

if __name__ == '__main__': #Opens main()function(Breuss, 2022)
    main()
