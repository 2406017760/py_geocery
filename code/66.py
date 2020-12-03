import requests
import urllib.request
from fake_useragent import UserAgent
import re
import random
import time

requests.packages.urllib3.disable_warnings()
PostNum = 0

def Get_Headers():
    headers = {  
        'Host':'www.wjx.cn',
        'User-Agent': UserAgent().random,
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer':'https://www.wjx.cn/m/38072076.aspx',
        'Cookie':'UM_distinctid=169ced4487c381-0eb21ff10e540a-784a5037-144000-169ced4487e128f; CNZZDATA4478442=cnzz_eid%3D198455657-1553952914-%26ntime%3D1555839771; .ASPXANONYMOUS=b8bj7o8d1QEkAAAAZjU3NjRkOWEtYzZjNC00ZDg4LTkxZmQtODdkMWZmZmYzM2EyPkFcM46KG2F_Bo62rCi-B5EyW9M1; acw_tc=2f624a1d15539532106003838e1bce9d7d440f74597e79e5b0c885288baa35; jac38072076=19904652; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1553953297,1553953308,1553953311,1555841361; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1555841361',
        'X-Forwarded-For':Get_IP()
    }
    return headers

def Get_IP():
    headers = {
        'User-Agent': UserAgent().random
    }
    html = urllib.request.Request(url='http://www.xiladaili.com/gaoni/', headers=headers)
    html = urllib.request.urlopen(html).read().decode('utf-8')
    reg = r'<td>(.+?)</td>'
    reg = re.compile(reg)
    pools = re.findall(reg, html)[0:499:5]
    Random_IP = random.choice(pools)
    return Random_IP

def Auto_WjX():
    url = 'https://www.wjx.cn/jq/97776692.aspx'
    data = "submitdata=1$1}2$3}3$1}4$2}5$1}6$2}7$2}8$1}9$1}10$1}11$1}12$1}13$1}14$1}15$1}16$1}17$1}18$1}19$1}20$1}21$1}22$1}23$1}24$1}25$2}26$3}27$3}28$2|10|13|19}29$4|10}30$3|7}31$2}32$3}33$4}34$1}35$1}36$1}37$2}38$2}39$2}40$2}41$1}42$2}43$1}44$2}45$1}46$1}47$4}48$4}49$4}50$4}51$3}52$3}53$1}54$1}55$1}56$3}57$3}58$3}59$1}60$3}61$3"
    r = requests.post(url, headers=Get_Headers(), data=data, verify=False)
    result = r.text[0:2]
    return result

def main():
    global PostNum
    for i in range(10):
        result = Auto_WjX()
        if int(result) in [10]:
            print('[ Response : %s ]  ===> 提交成功！！！！' % result)
            PostNum += 1
        else:
            print('[ Response : %s ]  ===> 提交失败！！！！' % result)
        time.sleep(30)  # 设置休眠时间，这里要设置足够长的休眠时间
    print('脚本运行结束，成功提交%s份调查报告' % PostNum)  # 总结提交成功的数量，并打印

if __name__ == '__main__':
    main()
