try:
    from face_recognition import *
except :
    import os
    os.system('pip install face_recognition')
    os.system('pip install tkinter')
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
w = 800 # width for the Tk root
h = 300 # height for the Tk root

root = Tk()
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('تشخيص چهره')
def get_1image():
    namefile1 = askopenfile()
    namefile11 = namefile1.split('.')
    if 'jpg' in namefile11:
        try:
            file = open(namefile1,'r')
        except:
            showwarning(title='bad file!',message='هيچ فايلي انتخاب نشده است!!!')
    elif 'jpeg' in namefile11:
        try:
            file = open(namefile1,'r')
        except:
            showwarning(title='bad file!',message='هيچ فايلي انتخاب نشده است!!!')
    elif 'png' in namefile11:
        try:
            file = open(namefile1,'r')
        except:
            showwarning(title='bad file!',message='هيچ فايلي انتخاب نشده است!!!')
    elif 'ico' in namefile11:
        try:
            file = open(namefile1,'r')
        except:
            showwarning(title='bad file!',message='هيچ فايلي انتخاب نشده است!!!')
    elif 'img' in namefile11:
        try:
            file = open(namefile1,'r')
        except:
            showwarning(title='bad file!',message='هيچ فايلي انتخاب نشده است!!!')
    else:
        showwarning(title='bad file!',message='فرمت فايل غير مجاز است!\nفقط عکس انتخاب نماييد')
        print(namefile11)



    

    
def get_2image():
    namefile2 = askopenfile()
    
    if 'jpg' in namefile11:
        try:
            file2 = open(namefile2,'r')
        except:
            showwarning(title='bad file!',message='هيچ فايلي انتخاب نشده است!!!')
    elif 'jpeg' in namefile11:
        try:
            file2 = open(namefile2,'r')
        except:
            showwarning(title='bad file!',message='هيچ فايلي انتخاب نشده است!!!')
    elif 'png' in namefile11:
        try:
            file2 = open(namefile2,'r')
        except:
            showwarning(title='bad file!',message='هيچ فايلي انتخاب نشده است!!!')
    elif 'ico' in namefile11:
        try:
            file2 = open(namefile2,'r')
        except:
            showwarning(title='bad file!',message='هيچ فايلي انتخاب نشده است!!!')
    elif 'img' in namefile11:
        try:
            file2 = open(namefile2,'r')
        except:
            showwarning(title='bad file!',message='هيچ فايلي انتخاب نشده است!!!')
    else:
        showwarning(title='bad file!',message='فرمت فايل غير مجاز است!\nفقط عکس انتخاب نماييد')
def tashkhis():
    try :
        _1 = load_image_file(namefile1)
    except :
        showwarning(title='bad file!',message='مشکلي پيش امده ! ايا فايل هارا درست وارد کرده ايد؟')
    try:
        _2 = load_image_file(namefile2)
    except:
        showwarning(title='bad file!',message='مشکلي پيش امده ! ايا فايل هارا درست وارد کرده ايد؟')
    __1 = face_encodings(_1)[0]
    __2 = face_encodings(_2)[0]
    result = compare_faces(__1,__2)
    if result == '[True]' or result == [True]:
        showinfo(title='TRUE',message='چهره ها مطابقت دارد!')
    elif result == '[False]' or result == [False]:
        showinfo(title='False',message='چهره ها مطابقت ندارد!')

lab = Label(text='پروژه ي تشخيص چهره \n عکس تنها عکس يک چهره باشد اگر بيشتر از يک چهره \nباشد امکان تشخيص اشتباه وجود دارد.',font=("Arial", 25),fg='black')
but1 = Button(text='وارد کردن عکس اول',bg='red',command=get_1image)
but1.grid(row = 1, column = 3, pady = 10, padx = 100)
but2 = Button(text='وارد کردن عکس دوم',bg='red',command=get_2image)
submit = Button(text = 'تشخيص',bg='black',fg='white',command=tashkhis)
pan.add(lab)
pan.add(but1)
pan.add(but2)
pan.add(submit)
pan.pack(fill = 'both',expand=True)
root.mainloop()
