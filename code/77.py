from selenium import webdriver
import random
import time
option = webdriver.ChromeOptions()
option.add_argument('headless')
url = 'https://www.wenjuan.com/s/yYFBf2I/'
t = 200
# 设置提交问卷次数

for times in range(t):
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    # 定位所有的问卷问题
    questions = driver.find_elements_by_css_selector('.matrix')
    for index,answers in enumerate(questions):
        # 定位所有问卷问题选项
        answer = answers.find_elements_by_css_selector('.icheckbox_div')
        # 定位需要填写文字的选项，并填入相关内容
        # if not answer:
        #     blank_potion = answers.find_element_by_css_selector('.blank.option')
        #     blank_potion.send_keys('没有')
        #     continue
        if index == 3 or index==4:
            choose_ans=answer[random.randint(0,4)]
            choose_ans.click()
            time.sleep(random.randint(2, 5))
        elif index==6 or index==7:
            choose_ans = answer[random.randint(0, 3)]
            choose_ans.click()
            time.sleep(random.randint(2, 5))
        elif index==5:
            for i in range(1,random.randint(1,3)):
                choose_ans = answer[random.randint(0, 5)]
                choose_ans.click()
                time.sleep(random.randint(2, 5))
        else:
            choose_ans = random.choice(answer)
            choose_ans.click()
            time.sleep(random.randint(2, 5))
    subumit_button = driver.find_element_by_css_selector('#next_button')
    subumit_button.click()
    print('已经成功提交了{}次问卷'.format(int(times)+int(1)))
    # 延迟问卷结果提交时间，以免间隔时间太短而无法提交
    time.sleep(2)
    driver.quit()
 