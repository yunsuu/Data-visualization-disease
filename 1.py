import pymysql
import csv

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='',
    charset='utf8'
)
cursor = conn.cursor()  #데이터 배이스에 연결된 객체

result_arr = [
    #9개
    [0] * 22,
    [0] * 22,
    [0] * 22,
    [0] * 22,
    [0] * 22,
    [0] * 22,
    [0] * 22,
    [0] * 22,
    [0] * 22,

]

age_arr = [0]*9

def judgeDisCode(dis_code):
    dis_idx = dis_code[0]
    if dis_idx == 'A' or dis_idx == 'B':
        return 0
    elif dis_idx == 'C':
        return 1
    elif dis_idx == 'D':
        if(dis_code[1] == '_'):
            tmp = 0
        else:
            tmp = int(dis_code[1:3])
        if(tmp<=48):
            return 1
        else:
            return 2
    elif dis_idx == 'E':
        return 3
    elif dis_idx == 'F':
        return 4
    elif dis_idx == 'G':
        return 5
    elif dis_idx == 'H':
        if (dis_code[1] == '_'):
            tmp = 0
        else:
            tmp = int(dis_code[1:3])
        if (tmp <= 59):
            return 6
        else:
            return 7
    elif dis_idx == 'I':
        return 8
    elif dis_idx == 'J':
        return 9
    elif dis_idx == 'K':
        return 10
    elif dis_idx == 'L':
        return 11
    elif dis_idx == 'M':
        return 12
    elif dis_idx == 'N':
        return 13
    elif dis_idx == 'O':
        return 14
    elif dis_idx == 'P':
        return 15
    elif dis_idx == 'Q':
        return 16
    elif dis_idx == 'R':
        return 17
    elif dis_idx == 'S' or dis_idx == 'T':
        return 18
    elif dis_idx == 'V' or dis_idx == 'Y':
        return 19
    elif dis_idx == 'Z':
        return 20
    elif dis_idx == 'U':
        return 21

def insertResultDic(arr, age_arr, age_code, dis_code):
    age_idx = int(age_code)*5 // 10
    dis_idx = judgeDisCode(dis_code)
    if not (age_idx>=0 and age_idx <= 8):
        return
    arr[age_idx][dis_idx] += 1
    age_arr[age_idx] += 1


#배열로 카운팅
cnt = 0
f = open('C:/Users/lg/Desktop/건강/국민건강보험공단_진료내역정보_2017.csv', 'r')
rdr = csv.reader(f)

#사전추가
for line in rdr:
    #if(cnt == 10):
     #   break;
    if (cnt == 0):
        cnt += 1
        continue
    insertResultDic(result_arr,age_arr, line[4], line[9])
    print(line[4], line[9])
    cnt += 1
f.close()

print(age_arr)

i = 0
j = 0
while i < 9:
    print(i, '0 대')
    j = 0
    while j < 22:
        print(j+1, ' : ', result_arr[i][j])
        j = j + 1
    print('-----------------')
    i = i + 1


conn.commit()