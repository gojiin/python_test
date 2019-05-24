# cx_Oracle 패키지 모듈들을 import
import cx_Oracle as oci

# Oracle 서버와 연결(Connection 맺기)
conn = oci.connect('SYSTEM/manager@localhost:1522/xe')

# Connection 확인
print(conn.version)

# Oracle DB의 test_member 테이블 검색(select)
cursor = conn.cursor() # cursor 객체 얻어오기

# print("이름")
# inputName = input()
# print("키")
# inputKey = input()
# sql_insert = 'INSERT INTO BPS_USERS VALUES(:NAME, :KEY, :BALENCE)'
# cursor.execute(sql_insert, NAME=inputName, KEY=inputKey, BALENCE=0)
# conn.commit()
# a = cursor.execute('SELECT * FROM BPS_USERS') # SQL 문장 실행


# class Block:
# # 블록번호, 현재해쉬 , 타임스탬프, 트랜잭션 데이터, 현재 해쉬, 작업증명 -> 이게 나중에 블록체인 csv파일 컬럼
# def __init__(self, index, previousHash, timestamp, data, currentHash, proof):
#     self.index = index
#     self.previousHash = previousHash
#     self.timestamp = timestamp
#     self.data = data
#     self.currentHash = currentHash
#     self.proof = proof
#
#
# class txData:
#     # 커밋되었어 안됬어, 누가(어떤기기) 보냈어, 양, 수신처, 고유번호
#     def __init__(self, commitYN, sender, amount, receiver, uuid):
#         self.commitYN = commitYN
#         self.sender = sender
#         self.amount = amount
#         self.receiver = receiver
#         self.uuid = uuid
#
# def moneyTransferService():
#     print("moneyTransferService")
#     tempHash = calculateHash(0, '0', timestamp, "Genesis Block", 0) #"Genesis Block"는 임의의 문자열을 뜻해. 최초 블록이라 넣을게 없거든
#     print(tempHash)
#     return Block(0, '0', timestamp, "Genesis Block",  tempHash,0)

# def
# print(a)
# print(type(a))
# sql_select = 'SELECT * FROM BPS_USERS where username = \'aa\''
# cursor.execute(sql_select, NAME=inputName, KEY=inputKey, BALENCE=0)
# conn.commit()

## txData는 무조건 다 받아준다.
## 다만 블록 값에 넣기전에 유효거래와 무효거래를 나누어준다.


# 이름 키 이름 키 날려서 들어오면 여기다 보내고 없으면 안 맞다. // 위에서 거른다. try 문. 예외처리.
def moneyTransferService(sender, amount, receiver, uuid, senderUserkey): #이름 키 이름 키 금액
    cursor.execute("SELECT balance FROM BPS_USERS where username = '{}' and userkey = '{}'" .format(sender, senderUserkey)) # 송신자, 송신자의 유져 키를 받아서 이걸로 잔고조회를 한다.
    breakpoint()break
    userrow = cursor.fetchall()
    cursor.execute("SELECT txValidity FROM BPS_TXDATA where uuid = '{}'".format(uuid)) # 개별 트랜잭션번호로 트랜잭션 유효성을 조회
    txrow = cursor.fetchall()
    if userrow[0][0] >= amount and txrow[0][0] == None: # 보내려는 금액보다 잔고가 크고 개별 트랙잭션 유효성이 null 값일 때 아래 구문 실행.
        cursor.execute("UPDATE BPS_USERS SET BALANCE = BALANCE-{} WHERE USERNAME = '{}'".format(amount, sender))
        cursor.execute("UPDATE BPS_USERS SET BALANCE = BALANCE+{} WHERE USERNAME = '{}'".format(amount, receiver))
        cursor.execute("UPDATE BPS_TxData SET txValidity = 1 WHERE uuid = '{}'".format(uuid)) # 기본은 null, 1은 유효한 거래
    elif userrow[0][0] < amount:
        cursor.execute("UPDATE BPS_TxData SET txValidity = 0 WHERE uuid = '{}'".format(uuid)) # 기본은 null, 0은 유효하지 않은 거래
    conn.commit()

moneyTransferService('AA', 300, 'CC', 12345, 'AA')

# cursor.execute("SELECT txValidity FROM BPS_TXDATA where uuid = 123")
# valid = cursor.fetchall()
# print(valid[0][0])
# sender = 'AA'
# amount = 500
# receiver = 'CC'
# uuid = 123456789
# senderUserkey = 'AA'

# cursor.execute("SELECT * FROM BPS_USERS where username = '{}' and USERKEY = '{}'".format(sender, senderUserkey))
# userrow = cursor.fetchall()

# cursor = conn.cursor()
# cursor.execute("UPDATE BPS_USERS SET BALANCE = BALANCE-{} WHERE USERNAME = '{}'".format(amount, sender))

# if userrow[0][2] >= amount:
#     cursor.execute("UPDATE BPS_USERS SET BALANCE = BALANCE-{} WHERE USERNAME = '{}'".format(amount, sender))
#     cursor.execute("UPDATE BPS_USERS SET BALANCE = BALANCE+{} WHERE USERNAME = '{}'".format(amount, receiver))
#     cursor.execute("UPDATE BPS_TXDATA SET TXVALIDITY = 1 WHERE UUID = '{}'".format(uuid))  # 기본은 null, 1은 유효한 거래
# elif userrow[0][2] < amount:
#     cursor.execute("UPDATE BPS_TXDATA SET TXVALIDITY = 0 WHERE UUID = '{}'".format(uuid))  # 기본은 null, 0은 유효한 거래

# for rs in cursor:
#     print(rs)
conn.commit()

cursor.close() # cursor 객체 닫기

# Oracle 서버와 연결 끊기
conn.close()