from docxtpl import DocxTemplate
import random
import datetime
import time


doc = DocxTemplate("安全生产责任制考核表-靖城路项目.docx")

def slist():

    list=["","",""]

    xb = random.choice([0,0,0,0,0,0,1,1,1,2])

    list[xb] = "☑"

    return list

def slist3():

    list2 = ["","",""]
    xb = random.choice([0,0,0,0,0,0,0,1,1,1])

    list2[xb] = "☑"

    return list2

date = datetime.datetime.now().strftime("%Y年%m月")

dic = {"date":date}

print(f"*****日期:{date}*****")
time.sleep(1)

for i in range(1,137):
    dic[f"a{i}"] = slist()
    print(f"*****正在写入{i}{slist()}*****")

for i in range(1,27):

    dic[f"b{i}"] = slist3()
    print(f"*****正在写入{i}{slist3()}*****")


content = dic


doc.render(context=content)

doc.save(f"{date}.docx")
print("****写入完成****")
time.sleep(5)