# Introduce
此脚本用于西华大学青柠疫服打卡系统**PS:此脚本实例于centos7上实现**
# Usage
## 安装依赖
### 安装selenium库
  pip install selenium
  #pip3 install selenium
### 安装google chrome浏览器
  sudo yum install google-chrome-stable_current_x86_64.rpm
### chrome路径
  which google-chrome-stable
### 做软连接
  ln -s 路径 /usr/bin/chrome
### 解决root用户不能运行Chrome
  vim /opt/google/chrome/google-chrome
  #将最后一行改写为: exec -a "$0" "$HERE/chrome" "$@" --no-sandbox $HOME
## chromedriver安装
### 验证google Chrome版本
  google-chrome-stable -version
### 下载ChromeDriver安装
  选择对应版本下载，访问：https://npm.taobao.org/mirrors/chromedriver
  wget https://npm.taobao.org/mirrors/chromedriver/72.0.3626.7/chromedriver_linux64.zip(这里的版本号需要手动更改成对应浏览器的版本)
### 解压安装包(没有zip解压，执行yum -y install zip)
  unzip chromedriver_linux64.zip
### 移动到/usr/bin目录下(或者移动到指定目录后排至软链接)
  sudo mv chromedriver /usr/bin
### 赋予Chromedriver权限
  chmod +x /usr/bin/chromedriver
### 测试chromedriver安装
  chromedriver
![image](https://user-images.githubusercontent.com/75559487/129130384-0372eecc-b662-4bdd-b232-e850b5d3e3ed.png)
## 代码使用
**PS:此代码健壮性不好，望谅解**  
代码仅需修改line8-10，以及line87中的Sno、Sname、Password 以及对应api的账号密码  
PS:此api为验证码识别，地址为http://www.ttshitu.com/  
![image](https://user-images.githubusercontent.com/75559487/129131269-b02ea940-7005-491a-99ed-866184d7adba.png)
![image](https://user-images.githubusercontent.com/75559487/129131322-9f5dc24e-a946-48e7-877c-9ad4fe31313d.png)  
更多api使用详情见开发文档  
http://www.ttshitu.com/docs/python.html#pageTitle  
## 脚本自动执行
  crontab -e  
crontab格式:  
![image](https://user-images.githubusercontent.com/75559487/129132153-77dfdaef-a075-43a6-af52-81117a502910.png)<br>

### python所在路径查看
  which python
  #which python3
### py文件路径查看
  find / -name xxx.py
### 最终格式
  0 0 * * * python所在路径 需执行的.py文件路径  
这样就实现了每天0点定时打卡



