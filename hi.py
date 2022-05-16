
# from threading import *
# from tkinter import *
# import os


# window=Tk()
# window.title("msg")
# window.geometry("350x150+300+100")


# txtYourMessage=Entry(window,width=50)
# txtYourMessage.insert(0,"")
# txtYourMessage.grid(row=1, column=0, pady=10)


# server=Entry(window,width=50)
# server.insert(0,"")
# server.grid(row=1, column=0, pady=10)


# def message():
#     os.system("msg * /server:%sserver% %txtYourMessage")

# btnSendMessage=Button(window, text="send", width=20, command=Message)
# btnSendMessage.grid(row=1, column=0, pady=10)

# window.mainloop()

# from email.mime import text
# from tkinter import*

# root=Tk()
# root.title("Chat box")
# root.geometry("300x300")
# lable=Label(root,text="My New GUI App!").grid(row=1,column=0)

# send=()
# i=0
# while i<=4:
#     a=input("enter the quation")
#     if a=="Hello"or a=="hello" or a=="Hi":
#         t=(END,"\n"+"Me -> Hi")
#     elif a=="How are you?"or "how are you?"or"HOW ARE YOU?":
#         t=(END,"\n"+"Me -> I am Fine")
#     elif a=="What are you doing in studies ?"or "what are you doing in studies?"or "what are you doing":    
#         t=(END,"\n"+"Me -> I am doing Softwer Engineering")    
#     elif a=="Now what do you want to do in future":
#         t==(END,"\n"+"I want to become a frontend devoloper" )       
#     i=i+1           
# t=Text(root)
# t.grid(row=0,column=0,columnspan=2)
# e=Entry(width=150)
# send=Button(root,text="Send",command=send).pack()
# e.grid(row=1,column=0)
# root.mainloop()
# from email.mime import text
# from tkinter import*

# root=Tk()
# root.title("Chat box")
# lable=Label(text="My New GUI App!",fg="blue",)
# lable.pack(side="top")
# def send():
#     send="You ->"+e.get()
#     t.insert(END,"\n"+send)
#     if (e.get()=="Hello"or e.get()=="hello" or e.get()=="Hi" or e.get()=="hi"):
#         t.insert(END,"\n"+"Me -> Hi")
#     elif(e.get()=="How are you?"or e.get()=="how are you?"or e.get()=="HOW ARE YOU?"):
#         t.insert(END,"\n"+"Me -> I am Fine")
#     elif(e.get()=="What are you doing in studies ?"or e.get()== "what are you doing in studies?"or e.get()== "what are you doing"):    
#         t.insert(END,"\n"+"Me -> I am doing Softwer Engineering")    
#     elif (e.get()=="Now what do you want to do in future"):
#         t.insert(END,"\n"+"I want to become a frontend devoloper" )    
#     else:
#         t.insert(END,"\n"+"Sorry i didnt get you")
#     e.delete(0,END)       
# t=Text(root)
# t.pack(padx=60,pady=20)
# e=Entry(width=150,bg="spring green",fg="black",relief="raised")
# send=Button(root,text="Send",fg="red",command=send).pack(side="right")

# e.pack()
# root.mainloop()


# from email.mime import text
# from tkinter import*

# root=Tk()
# root.title("Chat box")
# lable=Label(text="My New GUI App!",fg="blue",font="top")
# lable.pack
# def send():
#     send="You ->"+e.get()
#     t.insert(END,"\n"+send)
#     if (e.get()=="Hello"or e.get()=="hello" or e.get()=="Hi" or e.get()=="hi"):
#         t.insert(END,"\n"+"Me -> Hi")
#     elif(e.get()=="How are you?"or e.get()=="how are you?"or e.get()=="HOW ARE YOU?"):
#         t.insert(END,"\n"+"Me -> I am Fine")
#     elif(e.get()=="What are you doing in studies ?"or e.get()== "what are you doing in studies?"or e.get()== "what are you doing"):    
#         t.insert(END,"\n"+"Me -> I am doing Softwer Engineering")    
#     elif (e.get()=="Now what do you want to do in future"):
#         t.insert(END,"\n"+"I want to become a frontend devoloper" )    
#     else:
#         t.insert(END,"\n"+"Sorry i didnt get you")
#     e.delete(0,END)       
# t=Text(root)
# t.grid(row=0,column=0,columnspan=2)
# e=Entry(width=150,bg="spring green",fg="black")
# send=Button(root,text="Send",fg="red",command=send).grid(row=1,column=1)
# e.grid(row=1,column=0)
# root.mainloop()








