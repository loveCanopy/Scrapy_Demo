
#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def write2file(data):
    with open("tudou_info.json",'a') as f:
            f.write(data)

with open('tudou.json','r') as f:
    while True:
        line=f.readline()
        if line:
            data=str(line).decode("unicode-escape")
            print data
            write2file(data)
        else:
            break
