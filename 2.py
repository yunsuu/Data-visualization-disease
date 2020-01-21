import pymysql
import csv

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='ljsql934',
    db='datavisual',
    charset='utf8'
)
cursor = conn.cursor()  #데이터 배이스에 연결된 객체

def insertResultDic(results, input_code):
    if input_code in results:
        target = results[input_code]
        target['num'] += 1
    else:
        results[input_code] = {'num':1, 'avg':0, 'efficiency':0}

def calculateAvg(results, input_code, waste):
    if input_code in results:
        target = results[input_code]
        total_num = target['num']
        waste = int(waste)
        devide_avg = round(waste / total_num, 1)
        target['avg'] += devide_avg


result_dic = { }

#배열로 카운팅
cnt = 0
f = open('C:/Users/lg/Desktop/건강/국민건강보험공단_진료내역정보_2017.csv', 'r')
rdr = csv.reader(f)

#사전추가
for line in rdr:
    #if(cnt == 1000):
    #    break;
    if (cnt == 0):
        cnt += 1
        continue
    insertResultDic(result_dic, line[9])
    print(line[9])
    cnt += 1
f.close()


#평균
cnt = 0
f = open('C:/Users/lg/Desktop/건강/국민건강보험공단_진료내역정보_2017.csv', 'r')
rdr = csv.reader(f)
for line in rdr:
    #if(cnt == 1000):
     #   break;
    if (cnt == 0):
        cnt += 1
        continue
    print(line[9], line[14]) #14는 총액 15는 본인부담
    calculateAvg(result_dic, line[9], line[14])
    cnt += 1

f.close()
#excute할 튜플 배열 만들기
sql_excute_arr = []
sorted_result = sorted(result_dic.items(), key=lambda x: x[1]['num'], reverse=True)
print(sorted_result)
for element in sorted_result:
    if element[1]['num'] == 0 or element[1]['avg'] == 0:
        continue
    print(element)
    print(element[0], element[1]['num'], element[1]['avg'], int(element[1]['num']/int(element[1]['avg'])))
    input_tuple = (element[0], element[1]['num'], element[1]['avg'], int((element[1]['num'])* int(element[1]['avg']/10000)))
    sql_excute_arr.append(input_tuple)
for i in range(0,3):
    print(sql_excute_arr[i])

sql = """insert into homework2_realcost(dis_code,num,cost, efficiency)
         values (%s, %s, %s, %s)"""

print("총 데이터 개수는 :", cnt)
print("총 질병코드 개수는 :", len(sql_excute_arr))
cursor.executemany(sql, sql_excute_arr)
conn.commit()