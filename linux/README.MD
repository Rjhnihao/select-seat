# 下载项目
```shell
git clone https://github.com/Rjhnihao/select-seat.git
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
现已提供ChromeDriver的版本:126.0.6478.61
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
make start1
```
这条命令会使得test.py在后台运行，nohup会将输出重定向到一个名为nohup.out的文件中。
## 查看test.out文件
```shell
cat test.out
```
## 终止当前目录下所有进程:
```shell
make stop1
```
# 自动预约图书馆的项目
后续会更新位置的自定义
## 位置说明:
![位置说明](https://github.com/Rjhnihao/select-seat/blob/master/linux/%E8%87%AA%E5%AE%9A%E4%B9%89%E4%BD%8D%E7%BD%AE%EF%BC%88%E5%88%9D%E7%A8%BF%EF%BC%89.png)
