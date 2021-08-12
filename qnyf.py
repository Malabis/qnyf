import time
import requests
import base64
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

Sno=''
Sname=''
Password=''

#调用api识别验证码
def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

if __name__ == "__main__":
    #启动浏览器
    chrome_options = Options()
    chrome_options.add_argument('--headless') 
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')  # root用户不加这条会无法运行
    driver = webdriver.Chrome(chrome_options=chrome_options)
    #访问青柠疫服登录页面
    driver.get('http://wxyqfk.zhxy.net/?yxdm=10623#/login')
    driver.set_window_size(1400,800)
    time.sleep(2)

    #进行登录
    driver.find_element_by_xpath("//input[@placeholder='请输入学号']").send_keys(Sno)
    driver.find_element_by_xpath("//input[@placeholder='请输入姓名']").send_keys(Sname)
    driver.find_element_by_xpath("//input[@placeholder='请输入密码(初始密码为学号)']").send_keys(Password)
    login=driver.find_element_by_xpath("//button[@class='sign-in-btn van-button van-button--info van-button--normal']")
    login.click()

    #休眠1秒
    time.sleep(2)

    #点击温馨提示的确认按钮
    noconfirm=driver.find_element_by_xpath("//button[@class='van-button van-button--default van-button--large van-dialog__confirm']")
    noconfirm.click()
    time.sleep(2)

    #访问青柠疫服打卡页面
    driver.get('http://wxyqfk.zhxy.net/?yxdm=10623#/clockIn')
    time.sleep(1)


    print('现在开始打卡')
    #点击去打卡按钮
    gocheck=driver.find_element_by_xpath("//button[@class='sign-in-btn go-sign-btn van-button van-button--info van-button--normal']")
    gocheck.click()
    time.sleep(1)

    #进行自诊打卡信息填写
    Tdbodystate=driver.find_element_by_xpath("//label[@for='a_10_0']")#今日身体状况
    Tdbodystate.click()
    cxzz=driver.find_element_by_xpath("//label[@for='a_11_0']")#出现症状
    cxzz.click()
    nownear=driver.find_element_by_xpath("//label[@for='a_12_0']")#当前密切接触人员情况
    nownear.click()
    isschool=driver.find_element_by_xpath("//label[@for='a_14_1']")#是否在校
    isschool.click()
    isinternship=driver.find_element_by_xpath("//label[@for='a_15_0']")#是否实习
    isinternship.click()
    nowadrrisk=driver.find_element_by_xpath("//label[@for='a_16_2']")#现居住地风险程度
    nowadrrisk.click()

    #保存验证码图片
    images=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[8]/div/img")
    img_data = images.screenshot_as_png
    imgsavepath = '/root/verfiycode/file.jpg'
    with open(imgsavepath,'wb') as fp:
        fp.write(img_data)

    #返回识别结果
    img_path = "/root/verfiycode/file.jpg"
    code = base64_api(uname='', pwd='', img=img_path, typeid=3)
    verifycode=driver.find_element_by_xpath("//input[@placeholder='请输入验证码']")#输入验证码
    verifycode.send_keys(code)

    #每日打卡
    dayliycheck=driver.find_element_by_xpath("//button[@class='sign-in-btn van-button van-button--info van-button--normal']")
    dayliycheck.click()
    time.sleep(3)
    driver.close()
