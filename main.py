from os import stat
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_praktikum"
)

dbcursor = mydb.cursor()

root = Tk()
root.title("Praktikum DPBO")


# Fungsi untuk mengambil data
def getMhs():
    global mydb
    global dbcursor

    dbcursor.execute("SELECT * FROM mahasiswa")
    result = dbcursor.fetchall()

    return result


# Window Input Data
def inputs():
    # Hide root window
    global root
    root.withdraw()

    top = Toplevel()
    top.title("Input")
    dframe = LabelFrame(top, text="Input Data Mahasiswa", padx=10, pady=10)
    dframe.pack(padx=10, pady=10)

    # Input 1
    label1 = Label(dframe, text="Nama Mahasiswa").grid(
        row=0, column=0, sticky="w")
    input_nama = Entry(dframe, width=30)
    input_nama.grid(row=0, column=1, padx=20, pady=10, sticky="w")

    # Input 2
    label2 = Label(dframe, text="NIM").grid(row=1, column=0, sticky="w")
    input_nim = Entry(dframe, width=30)
    input_nim.grid(row=1, column=1, padx=20, pady=10, sticky="w")

    # Input 3
    options = ["Filsafat Meme", "Sastra Mesin",
               "Teknik Kedokteran", "Pendidikan Gaming"]
    input_jurusan = StringVar(root)
    input_jurusan.set(options[0])
    label4 = Label(dframe, text="Jurusan").grid(row=2, column=0, sticky="w")
    input4 = OptionMenu(dframe, input_jurusan, *options)
    input4.grid(row=2, column=1, padx=20, pady=10, sticky='w')

    # Radio Button Frame
    frame3 = LabelFrame(dframe, borderwidth=0)
    frame3.grid(row=3, column=1, sticky="w")

    # Input 4
    label5 = Label(dframe, text="Jenis Kelamin").grid(
        row=3, column=0, sticky="w")
    input_gender = StringVar()
    input_gender.set("Laki-laki")
    Radiobutton(frame3, text="Laki-laki", value="Laki-laki",
                variable=input_gender).grid(row=0, column=0, padx=20, pady=10, sticky="w")
    Radiobutton(frame3, text="Perempuan", value="Perempuan",
                variable=input_gender).grid(row=0, column=1, padx=20, pady=10, sticky="w")

    # Checkbox Frame
    frame4 = LabelFrame(dframe, borderwidth=0)
    frame4.grid(row=4, column=1, sticky="w")

    # Checkbox
    '''hobi = []
    listHobi = ["Bernyanyi", "Bermain Game", "Jalan-jalan", "Ngoding"]
    row = 0
    col = 0
    for i in range(len(listHobi)):
        h = StringVar()
        if col == 2:
            col = 0
            row = row + 1
        c = Checkbutton(frame4, text=listHobi[i], onvalue=listHobi[i],
                        offvalue=False, variable=h)
        c.deselect()
        c.grid(row=row, column=col, padx=20, pady=10, sticky="w")
        if h.get():
            hobi.append(h.get())
        col = col + 1
    input_hobi = hobi[0]
    i = 1
    for i in range(len(hobi)):
        input_hobi = input_hobi + "," + hobi[i]'''
    hobi1 = StringVar()
    hobi2 = StringVar()
    hobi3 = StringVar()
    hobi4 = StringVar()
    c = Checkbutton(frame4, text="Bernyanyi", onvalue="Bernyanyi",
                    offvalue="False", variable=hobi1)
    c.deselect()
    c.grid(row=0, column=0, padx=20, pady=10, sticky="w")
    c = Checkbutton(frame4, text="Bermain Game", onvalue="Bermain Game",
                    offvalue="False", variable=hobi2)
    c.deselect()
    c.grid(row=0, column=1, padx=20, pady=10, sticky="w")
    c = Checkbutton(frame4, text="Jalan-jalan", onvalue="Jalan-jalan",
                    offvalue="False", variable=hobi3)
    c.deselect()
    c.grid(row=1, column=0, padx=20, pady=10, sticky="w")
    c = Checkbutton(frame4, text="Ngoding", onvalue="Ngoding",
                    offvalue="False", variable=hobi4)
    c.deselect()
    c.grid(row=1, column=1, padx=20, pady=10, sticky="w")
    # input_hobi = hobi1.get()
    '''input_hobi = input_hobi + str(hobi1.get()) if hobi1 != False else 'hehe'
    input_hobi = input_hobi + "," + \
        str(hobi2.get()) if hobi2 != False else "hihi"
    input_hobi = input_hobi + "," + \
        str(hobi3.get()) if hobi3 != False else "huhu"
    input_hobi = input_hobi + "," + \
        str(hobi4.get()) if hobi4 != False else "hoho"'''

    # Button Frame
    frame2 = LabelFrame(dframe, borderwidth=0)
    frame2.grid(columnspan=2, column=0, row=10, pady=10)

    # Submit Button
    btn_submit = Button(frame2, text="Submit Data", anchor="s", command=lambda: [
                        insertData(top, input_nama.get(), input_nim.get(), input_jurusan.get(), input_gender.get(), [hobi1.get(), hobi2.get(), hobi3.get(), hobi4.get()]), top.withdraw()])
    btn_submit.grid(row=3, column=0, padx=10)

    # Cancel Button
    btn_cancel = Button(frame2, text="Gak jadi / Kembali", anchor="s",
                        command=lambda: [top.destroy(), root.deiconify()])
    btn_cancel.grid(row=3, column=1, padx=10)

# Untuk memasukan data


def insertData(parent, nama, nim, jurusan, gender, data_hobi):
    top = Toplevel()
    # Get data
    # nama = nama.get()
    # nim = nim.get()
    # jurusan = jurusan.get()
    # hobi = ",".join(data_hobi)
    hobi = ''
    for i in range(len(data_hobi)):
        if data_hobi[i] != "False":
            hobi = hobi + data_hobi[i]
            if i < len(data_hobi) - 1:
                hobi = hobi + ","

    # Input data disini
    if nama != "" and nim != "" and hobi != "":
        btn_ok = Button(top, text="Syap!", anchor="s", command=lambda: [
                        top.destroy(), root.deiconify()])
        btn_ok.pack(padx=10, pady=10)

        global mydb
        global dbcursor

        sql = "INSERT INTO mahasiswa (nim, nama, jurusan, jenis_kelamin, hobi) VALUES (%s, %s, %s, %s, %s)"
        val = (nim, nama, jurusan, gender, hobi)
        dbcursor.execute(sql, val)

        mydb.commit()
    else:
        btn_err = Button(top, text="Ada yg kosong!", anchor="s",
                         command=lambda: [top.destroy(), parent.deiconify()])
        btn_err.pack(padx=10, pady=10)

# Window Semua Mahasiswa


def viewAll():
    global root
    root.withdraw()

    top = Toplevel()
    top.title("Semua Mahasiswa")
    frame = LabelFrame(top, borderwidth=0)
    frame.pack()
    # Cancel Button
    btn_cancel = Button(frame, text="Kembali", anchor="w",
                        command=lambda: [top.destroy(), root.deiconify()])
    btn_cancel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    # Head title
    head = Label(frame, text="Data Mahasiswa")
    head.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    tableFrame = LabelFrame(frame)
    tableFrame.grid(row=1, column=0, columnspan=2)

    # Get All Data
    result = getMhs()

    # Title
    title1 = Label(tableFrame, text="No.", borderwidth=1,
                   relief="solid", width=3, padx=5).grid(row=0, column=0)
    title2 = Label(tableFrame, text="NIM", borderwidth=1,
                   relief="solid", width=15, padx=5).grid(row=0, column=1)
    title3 = Label(tableFrame, text="Nama", borderwidth=1,
                   relief="solid", width=20, padx=5).grid(row=0, column=2)
    title4 = Label(tableFrame, text="Jurusan", borderwidth=1,
                   relief="solid", width=20, padx=5).grid(row=0, column=3)
    title5 = Label(tableFrame, text="Jenis Kelamin", borderwidth=1,
                   relief="solid", width=20, padx=5).grid(row=0, column=4)
    title6 = Label(tableFrame, text="Hobi", borderwidth=1,
                   relief="solid", width=30, padx=5).grid(row=0, column=5)

    # Print content
    i = 0
    for data in result:
        label1 = Label(tableFrame, text=str(i+1), borderwidth=1,
                       relief="solid", height=2, width=3, padx=5).grid(row=i+1, column=0)
        label2 = Label(tableFrame, text=data[1], borderwidth=1, relief="solid",
                       height=2, width=15, padx=5).grid(row=i+1, column=1)
        label3 = Label(tableFrame, text=data[2], borderwidth=1, relief="solid",
                       height=2, width=20, padx=5).grid(row=i+1, column=2)
        label4 = Label(tableFrame, text=data[3], borderwidth=1, relief="solid",
                       height=2, width=20, padx=5).grid(row=i+1, column=3)
        label5 = Label(tableFrame, text=data[4], borderwidth=1, relief="solid",
                       height=2, width=20, padx=5).grid(row=i+1, column=4)
        label6 = Label(tableFrame, text=data[5], borderwidth=1, relief="solid",
                       height=2, width=30, padx=5).grid(row=i+1, column=5)
        i += 1

# Dialog konfirmasi hapus semua data


def clearAll():
    top = Toplevel()
    lbl = Label(top, text="Yakin mau hapus semua data?")
    lbl.pack(padx=20, pady=20)
    btnframe = LabelFrame(top, borderwidth=0)
    btnframe.pack(padx=20, pady=20)
    # Yes
    btn_yes = Button(btnframe, text="Gass", bg="green",
                     fg="white", command=lambda: [top.destroy(), delAll()])
    btn_yes.grid(row=0, column=0, padx=10)
    # No
    btn_no = Button(btnframe, text="Tapi boong", bg="red",
                    fg="white", command=top.destroy)
    btn_no.grid(row=0, column=1, padx=10)

# Dialog konfirmasi keluar GUI


def exitDialog():
    global root
    root.withdraw()
    top = Toplevel()
    lbl = Label(top, text="Yakin mau keluar?")
    lbl.pack(padx=20, pady=20)
    btnframe = LabelFrame(top, borderwidth=0)
    btnframe.pack(padx=20, pady=20)
    # Yes
    btn_yes = Button(btnframe, text="Gass", bg="green", fg="white",
                     command=lambda: [top.destroy(), root.destroy()])
    btn_yes.grid(row=0, column=0, padx=10)
    # No
    btn_no = Button(btnframe, text="Tapi boong", bg="red", fg="white",
                    command=lambda: [top.destroy(), root.deiconify()])
    btn_no.grid(row=0, column=1, padx=10)


def delAll():
    top = Toplevel()
    # Delete data disini
    global dbcursor
    global mydb

    sql = "DELETE FROM mahasiswa"
    dbcursor.execute(sql)

    btn_ok = Button(top, text="Zeeb", command=top.destroy)
    btn_ok.pack(pady=20)


def facilities():
    global root
    root.withdraw()

    top = Toplevel()
    top.title("Fasilitas Mahasiswa")

    fas1 = ImageTk.PhotoImage(Image.open("images/lab-bigdata.png"))
    fas2 = ImageTk.PhotoImage(Image.open("images/lab-jaringan.png"))
    fas3 = ImageTk.PhotoImage(Image.open("images/lab-microteaching.png"))
    fas4 = ImageTk.PhotoImage(Image.open("images/lab-multimedia.png"))
    fas5 = ImageTk.PhotoImage(Image.open("images/lab-umum.png"))

    fasImgs = [fas1, fas2, fas3, fas4, fas5]

    labelImg = Label(top, image=fas1)
    labelImg.grid(row=0, column=0, columnspan=3)

    button_prev = Button(top, text="<<", state=DISABLED)
    button_back = Button(top, text="Kembali", command=lambda: [
                         top.destroy(), root.deiconify()])
    button_next = Button(top, text=">>", command=lambda: nextImg(
        top, labelImg, button_prev, button_next, fasImgs, 1))

    button_prev.grid(row=1, column=0)
    button_back.grid(row=1, column=1)
    button_next.grid(row=1, column=2)


def nextImg(parent, labelImg, btnPrev, btnNext, imgList, imgNum):
    labelImg.grid_forget()
    labelImg = Label(parent, image=imgList[imgNum])

    button_prev = Button(parent, text="<<", command=lambda: prevImg(
        parent, labelImg, btnPrev, btnNext, imgList, imgNum-1))
    button_back = Button(parent, text="Kembali", command=lambda: [
                         parent.destroy(), root.deiconify()])
    button_next = Button(parent, text=">>", command=lambda: nextImg(
        parent, labelImg, btnPrev, btnNext, imgList, imgNum+1))
    labelImg.grid(row=0, column=0, columnspan=3)

    if imgNum == 4:
        button_next = Button(parent, text=">>", state=DISABLED)

    button_prev.grid(row=1, column=0)
    button_back.grid(row=1, column=1)
    button_next.grid(row=1, column=2)


def prevImg(parent, labelImg, btnPrev, btnNext, imgList, imgNum):
    labelImg.grid_forget()
    labelImg = Label(parent, image=imgList[imgNum])

    button_prev = Button(parent, text="<<", command=lambda: prevImg(
        parent, labelImg, btnPrev, btnNext, imgList, imgNum-1))
    button_back = Button(parent, text="Kembali", command=lambda: [
                         parent.destroy(), root.deiconify()])
    button_next = Button(parent, text=">>", command=lambda: nextImg(
        parent, labelImg, btnPrev, btnNext, imgList, imgNum+1))
    labelImg.grid(row=0, column=0, columnspan=3)

    if imgNum == 0:
        button_prev = Button(parent, text="<<", state=DISABLED)

    button_prev.grid(row=1, column=0)
    button_back.grid(row=1, column=1)
    button_next.grid(row=1, column=2)


# Title Frame
frame = LabelFrame(root, text="Praktikum DPBO", padx=10, pady=10)
frame.pack(padx=10, pady=10)

# ButtonGroup Frame
buttonGroup = LabelFrame(root, padx=10, pady=10)
buttonGroup.pack(padx=10, pady=10)

# Title
label1 = Label(frame, text="Data Mahasiswa", font=(30))
label1.pack()

# Description
label2 = Label(frame, text="Ceritanya ini database mahasiswa ngab")
label2.pack()

# Input btn
b_add = Button(buttonGroup, text="Input Data Mahasiswa",
               command=inputs, width=30)
b_add.grid(row=0, column=0, pady=5)

# All data btn
b_add = Button(buttonGroup, text="Semua Data Mahasiswa",
               command=viewAll, width=30)
b_add.grid(row=1, column=0, pady=5)

# Clear all btn
b_clear = Button(buttonGroup, text="Hapus Semua Data Mahasiswa",
                 command=clearAll, width=30)
b_clear.grid(row=2, column=0, pady=5)

# Fasilitas
b_clear = Button(buttonGroup, text="Fasilitas Mahasiswa",
                 command=facilities, width=30)
b_clear.grid(row=3, column=0, pady=5)

# Exit btn
b_exit = Button(buttonGroup, text="Exit", command=exitDialog, width=30)
b_exit.grid(row=4, column=0, pady=5)

root.mainloop()
