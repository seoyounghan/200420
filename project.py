from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()

window.title("아마추어를 위한 타구 분석 프로그램")
window.geometry("740x500")
window.resizable(False, False)

mainMenu = Menu(window)
window.config(menu=mainMenu)

#야구장 이미지 사진
photo = PhotoImage(file="야구장사진.gif")
label_image = Label(window, image=photo)

#변수설정
pitcherName =None
pitcherType =None
pitchType =None
batterName =None
xPoint =None
yPoint =None
pitcherTypetext=None
pitchTypetext=None

#데이터베이스 설정

#캔버스 설정
canvas = Canvas(window, bd=2, width=550, height=400)
canvas.create_image(280, 250, image = photo)

canvas.pack(fill="both", side=LEFT)


#그림 클릭
def clickLeft(event) :
    print(event.x, event.y)
    canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="red")
    global xPoint
    xPoint=event.x
    global yPoint
    yPoint=event.y

#버튼 클릭
def clickbutton4(): #투수 이름
    global pitcherName
    pitcherName=entry1.get()
    print(entry1.get())

def clickbutton5(): #좌투
    global pitcherType
    pitcherType=1
    global pitcherTypetext
    pitcherTypetext="좌투"
    print(pitcherType)
    print(pitcherTypetext)


def clickbutton6(): #우투
    global pitcherType
    pitcherType = 2
    global pitcherTypetext
    pitcherTypetext="우투"
    print(pitcherType)
    print(pitcherTypetext)


def clickbutton7(): #직구
    global pitchType
    pitchType=1
    global pitchTypetext
    pitchTypetext="직구"
    print(pitchType)
    print(pitchTypetext)

def clickbutton8(): #슬라이더
    global pitchType
    pitchType=2
    global pitchTypetext
    pitchTypetext="슬라이더"
    print(pitchType)
    print(pitchTypetext)

def clickbutton9(): #타자 이름
    global batterName
    batterName=entry2.get()
    print(entry2.get())


##데이터 select(고정값: 타자 이름/ 변수: 투수포지션/구종/투수이름)

##select함수
def selectData(sql):
    XPOINT, YPOINT = [], []
    con = sqlite3.connect("C:/Users/82102/sqlite-tools-win32-x86-3310100/userData")
    cur = con.cursor()
    cur.execute(sql)
    while (True):
        row = cur.fetchone()
        if row == None:
            break;
        XPOINT.append(row[0])
        YPOINT.append(row[1])

    print(XPOINT, YPOINT) ##출력확인용
    con.close()

##좌투sql
def analyse_Leftpitcher():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName='" + batterName + "' AND pitcherType=1"
    selectData(sql)

##우투sql
def analyse_Rightpitcher():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName='" + batterName + "' AND pitcherType=2"
    selectData(sql)

##직구sql
def analyse_Fastball():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName='" + batterName + "' AND pitchType=1"
    selectData(sql)

##슬라이더(변화구)sql
def analyse_Slider():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName='" + batterName + "' AND pitchType=2"
    selectData(sql)

##투수이름sql
def analyse_pitcher():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName='" + batterName + "' AND pitcherName='" + pitcherName +"'"
    selectData(sql)

##수비 추천
def recoDefence():
    sql = ""
    sql = "SELECT xPoint, yPoint, pitcherType, pitchType FROM userData WHERE batterName='" + batterName + "' AND pitcherName='" + pitcherName + "'"

    XPOINT, YPOINT, manType, ballType = [], [], [], []
    con = sqlite3.connect("C:/Users/82102/sqlite-tools-win32-x86-3310100/userData")
    cur = con.cursor()
    cur.execute(sql)
    while (True):
        row = cur.fetchone()
        if row == None:
            break;
        XPOINT.append(row[0])
        YPOINT.append(row[1])
        manType.append(row[2])
        ballType.append(row[3])

    xaver = averXpoint(XPOINT)
    yaver = averYpoint(YPOINT)
    manaver = avermanType(manType)
    ballaver = averballType(ballType)



##x좌표 평균값
def averXpoint(XPOINT):
    Xsum = 0
    Xaver = 0
    for x in range(0, len(XPOINT)):
        Xsum += XPOINT[x]
    Xaver = Xsum/len(XPOINT)
    return Xaver

##y좌표 평균값
def averYpoint(YPOINT):
    Ysum = 0
    Yaver = 0
    for y in range(0, len(YPOINT)):
        Ysum += YPOINT[y]
    Yaver = Ysum/len(YPOINT)
    return Yaver

##투수정보 확률
def avermanType(manType):
    leftType = manType.count(1)/len(manType)
    rightType = manType.count(2)/ len(manType)

    if leftType > rightType:
        return leftType
    else:
        return rightType

##구종 확률
def averballType(ballType):
    fastball = ballType.count(1)/len(ballType)
    slider = ballType.count(2)/len(ballType)

    if fastball > slider:
        return fastball
    else:
        return slider


def resetVari():
    global pitcherName
    global pitcherType
    global pitchType
    global batterName
    global xPoint
    global yPoint
    global pitcherTypetext
    global pitchTypetext

    pitcherName = None
    pitcherType = None
    pitchType = None
    batterName = None
    xPoint = None
    yPoint = None
    pitcherTypetext = None
    pitchTypetext = None

#맨 위 입력 버튼으로 데이터베이스에 데이터 저장


def input_messageask():
    global pitcherName
    global pitcherType
    global pitchType
    global batterName
    global xPoint
    global yPoint
    global pitcherTypetext
    global pitchTypetext

    ans=messagebox.askquestion("확인", "투수 이름 : " + pitcherName  + "\n투수 정보 : " + pitcherTypetext + "\n구종 : " + pitchTypetext + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
    if ans== "yes":
        canvas.delete("all")
        canvas.create_image(280, 200, image=photo)
        print("확인") #단계별로 코드 실행되는지 확인하기 위해서 추가한 코드
        SaveLine()
        print("저장됨") #단계별로 코드 실행되는지 확인하기 위해서 추가한 코드
        PrintData() #데이터가 제대로 저장됐는지 확인하기 위해서 추가한 함수
        print("출력") #단계별로 코드 실행되는지 확인하기 위해서 추가한 코드

        resetVari()



def analyse_messageask():

    if pitcherType == 1:
        ans = messagebox.askquestion("확인", "투수 정보 : 좌투" + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            analyse_Leftpitcher()
            resetVari()

    elif pitcherType == 2:
        ans = messagebox.askquestion("확인", "투수 정보 : 우투" + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            analyse_Rightpitcher()
            resetVari()

    elif pitchType == 1:
        ans = messagebox.askquestion("확인", "구종 : 직구" + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            analyse_Fastball()
            resetVari()

    elif pitchType == 2:
        ans = messagebox.askquestion("확인", "구종 : 슬라이더" + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            analyse_Slider()
            resetVari()

    elif pitcherName != None:
        ans = messagebox.askquestion("확인", "투수 이름 : " + pitcherName + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
        if ans == "yes":
            analyse_pitcher()
            resetVari()


def recommend_messageask():
    ans = messagebox.askquestion("확인", "투수 이름 : " + pitcherName + "\n타자 이름 : " + batterName + "\n이 맞습니까?")
    if ans == "yes":
        recoDefence()


#메뉴 설정
fileMenu=Menu(mainMenu)
helpMenu=Menu(mainMenu)

mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="입력")
fileMenu.add_separator() #메뉴 구분선
fileMenu.add_command(label="분석")

mainMenu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="도움말")


#입력 정보
button1=Button(window, text="입력", relief="groove", bg="skyblue", command=input_messageask)
button1.place(x=570, y=20)
button2=Button(window, text="분석", relief="groove", bg="red", command=analyse_messageask)
button2.place(x=610, y=20)
button3=Button(window, text="수비 추천", relief="groove", bg="gray", command =recommend_messageask)
button3.place(x=650, y=20)

label1=Label(window, text="  투수 이름  ", relief="groove")
label1.place(x=570, y=80)
entry1=Entry(window, width=16) #투수정보
entry1.place(x=570, y=103)
button4=Button(window, text="입력", relief="groove", bg="gray", command=clickbutton4)
button4.place(x=690, y=100)

label2=Label(window, text=" 투수 정보 선택 ", relief="groove")
label2.place(x=570, y=150)
button5=Button(window, text="   좌투   ", relief="groove", bg="gray", command=clickbutton5)
button5.place(x=570, y=175)
button6=Button(window, text="   우투   ", relief="groove", bg="gray", command=clickbutton6)
button6.place(x=640, y=175)


label3=Label(window, text="  구종 선택  ", relief="groove")
label3.place(x=570, y=230)
button7=Button(window, text="   직구   ", relief="groove", bg="gray", command=clickbutton7)
button7.place(x=570, y=255)
button8=Button(window, text="슬라이더", relief="groove", bg="gray", command=clickbutton8)
button8.place(x=640, y=255)


label4=Label(window, text="  타자 이름  ", relief="groove")
label4.place(x=570, y=310)
entry2=Entry(window, width=16) #타자정보
entry2.place(x=570, y=333)
button9=Button(window, text="입력", relief="groove", bg="gray", command=clickbutton9)
button9.place(x=690, y=330)

#데이터베이스 설정
def SaveLine():  ##데이터베이스에 데이터 저장
    con, cur = None, None
    sql = ""

    con = sqlite3.connect("userData")  # DB가 저장된 폴더까지 지정
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")  # DB가 저장된 폴더까지 지정

    cur = con.cursor()

    sql = "INSERT INTO userData VALUES('" + str(pitcherName) + "', " + str(pitcherType) + "," + str(
        pitchType) + ", '" + str(batterName) + "', " + str(xPoint) + "," + str(yPoint) + ")"
    cur.execute(sql)

    con.commit()
    con.close()

def PrintData():
    con, cur = None, None
    sql = ""

    con = sqlite3.connect("userData")  # DB가 저장된 폴더까지 지정
    con = sqlite3.connect(r"C:\Users\Owner\Desktop\program\sqlite\userData")  # DB가 저장된 폴더까지 지정

    cur = con.cursor()

    cur.execute("SELECT * FROM userData")
    print("타자 이름     투수 정보     구종      투수 이름")
    print("-----------------------------------------------")
    data1, data2, data3, data4="","","",""
    while(True):
        row=cur.fetchone()
        if row==None:
            break;
        data1=row[0]
        data2=row[1]
        data3=row[2]
        data4=row[3]
        print("%5s   %d    %d    %15s"%(data1, data2, data3, data4))
    con.close()


canvas.bind("<Button-1>", clickLeft)

window.mainloop()