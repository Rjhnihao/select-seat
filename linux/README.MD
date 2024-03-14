# 下载项目
```shell
git clone 
```
# 安装指南：
## python需匹配的环境：
````
urllib3=1.26.18
selenium==3.141.0
````
安装环境:
```shell
pip3 install urllib3==1.26.18
pip3 install selenium==3.141.0
pip3 install schedule
pip3 install datetime
```


## 安装google:
现已提供ChromeDriver的版本:122.0.6261.128
```shell
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i ./google-chrome-stable_current_amd64.deb
```
安装若失败，则输入以下命令，用于安装所需的依赖并再次安装：
```shell
sudo apt-get install -f
sudo dpkg -i ./google-chrome-stable_current_amd64.deb
```
安装成功后，查看Chrome版本:
```shell
google-chrome --version
```
给ChromeDriver添加权限:
```shell
chmod +x chromedriver
chmod +x Makefile
```
# 开始运行:
```shell
nohup python3 test.py &
```
这条命令会使得test.py在后台运行，nohup会将输出重定向到一个名为nohup.out的文件中。
## 查看nohup.out文件
```shell
cat nohup.out
```
## 终止当前目录下所有进程:
```shell
lsof +D $(pwd) | awk 'NR>1 {print $2}' | sort -u | xargs kill
```


# 自动预约图书馆的项目