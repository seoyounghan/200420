rom tkinter import*
import sqlite3

##데이터 select(고정값: 타자 이름/ 변수: 투수포지션/구종/투수이름)

##select함수
def selectData(sql):
    XPOINT, YPOINT = [], []
    con = sqlite3.connect("userData")
    cur = con.cursor()
    cur.execute(sql)
    while (True):
        row = cur.fetchone()
        if row == None:
            break;
        XPOINT.append(row[0])
        YPOINT.append(row[1])
##좌투sql
def analyse_Leftpitcher():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName=" + entry2.get() + " AND pitcherType=1"
    selectData(sql)

##우투sql
def analyse_Rightpitcher():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName=" + entry2.get() + " AND pitcherType=2"
    selectData(sql)

##직구sql
def analyse_Fastball():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName=" + entry2.get() + " AND pitchType=1"
    selectData(sql)

##슬라이더(변화구)sql
def analyse_Slider():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName=" + entry2.get() + " AND pitchType=2"
    selectData(sql)

##투수이름sql
def analyse_pitcher():
    sql = ""
    sql = "SELECT xPoint, yPoint FROM userData WHERE batterName=" + entry2.get() + " AND pitcherName=" + entry1.get()
    selectData(sql)

def recoDefence():
    sql = ""
    sql = "SELECT xPoint, yPoint, pitcherType, pitchType FROM userData WHERE batterName=" + entry2.get() + " AND pitcherName=" + entry1.get()
    selectData(sql)

    XPOINT, YPOINT, manType, ballType = [], [], [], []
    con = sqlite3.connect("userData")
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