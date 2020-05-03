from tkinter import*

window = Tk()

window.title("아마추어를 위한 타구 분석 프로그램")
window.geometry("700x400")
window.resizable(False, False)

mainMenu = Menu(window)
window.config(menu=mainMenu)

#야구장 이미지 사진
photo = PhotoImage(file="야구장사진.gif")
label_image = Label(window, image=photo, bg="PINK")



#캔버스 설정
canvas = Canvas(window, bd=2, width=560, height=400)
canvas.create_image(280, 200, image = photo)
canvas.pack(fill="both", side=LEFT)

#마우스 클릭
def clickLeft(event) :
    print(event.x, event.y)
    if event.x<=560: #야구장에 입력되야하는 범위 x<=560으로 지정
        canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="red")


#메뉴 설정
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="입력")
fileMenu.add_separator() #메뉴 구분선
fileMenu.add_command(label="분석")

#입력 정보
button1=Button(window, text="입력", relief="groove", bg="skyblue")
button1.place(x=570, y=20)
button2=Button(window, text="분석", relief="groove", bg="red")
button2.place(x=610, y=20)

label1=Label(window, text="투수 정보", relief="groove")
label1.place(x=570, y=70)
label1=Label(window, text="타구 정보", relief="groove")
label1.place(x=570, y=120)
label1=Label(window, text="타자 정보", relief="groove")
label1.place(x=570, y=170)

entry1=Entry(window, width=16) #투수정보
entry1.place(x=570, y=90)
entry2=Entry(window, width=16) #타구정보
entry2.place(x=570, y=140)
entry3=Entry(window, width=16) #타자정보
entry3.place(x=570, y=190)


i=1 #list 순서
ls=Listbox(window, width=140, height=400, relief="sunken") #리스트 크기 지정
ls.insert(1, "ㅇㅇㅇ") #리스트 뜨는지 안뜨는지

#list 추가, 삭제 함수
def insert(number, name, i):
    ls.insert(i, name)
    i=i+1
def delete(i):
    ls.delete(ANCHOR) #ANCHOR 첫번째가 지워짐
    i=i-1


window.bind("<Button-1>", clickLeft)


#label_image.pack(side=LEFT)
#ls.pack(side=RIGHT)


window.mainloop()
