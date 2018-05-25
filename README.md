# webchat
先搭建一个BBS论坛，然后加入聊天功能
## 环境配置
### 官网下载MySQL installer (5.7)
### python配置Django框架 （Django 2.0）
### 安装python包pymysql
  pymysql是Python中操作MySQL的模块，其使用方法和MySQLdb几乎相同。但目前pymysql支持python3.x而后者不支持3.x版本。
  
  修改在django中默认的数据库访问MySQL。
  
  在项目目录下的__init__.py文件（webchat/webchat/ \_\_init\_\_.py）加入下面两句
  ```
    import pymysql
    pymysql.install_as_MySQLdb()
  ```
## Getting Started
1.创建Django project
```
$ django-admin startproject webchat
```
2.创建app 
```
$ cd webchat
$ python manage.py startapp bbs
```
3.创建template和statics
```
$ mkdir templates
$ mkdir statics
```
4.创建一个数据库实例
```
$ mysql -u root -p
mysql>create database my_bbs default charset UTF8
```
5.编辑webchat/settings.py的DATABASES、TEMPLATES、STATIC_URL 文件 (代码中已经修改)

6.进行bbs系统的开发，设计表结构；分析业务、添加表字段（补充bbs/model.py文件）

7.设置setting.py，把bbs项目加到APP中 
```
    # Application definition
 
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'bbs',
    ]
```
8.创建数据库，这里需要MySQL5.7版本，MySQL8.0版本会报错"ACCESS DENIED FOR USER 'root'@'localhost'(using password:NO)"
```
# 在该app下建立migrations目录，并记录下所有关于model.py的变动，将改动迁移到migrations这个文件下生成一个文件如：0001文件
# 但此时这个命令并没有作用于数据库
$ python manage.py makemigrations

# 执行migrate将改动作用于数据库文件，也就是执行migrations里面新改动的迁移文件更新数据库，比如创建数据表，或者增加字段属性
$ python manage.py migrate

# 注意这两个命令默认情况下是作用于全局，也就是对所有最新更改的models或者migrations下的迁移文件进行对应的操作，
# 如果要想对部分app作用，执行如下命令
$ python manage.py makemigrations appname
$ python manage.py migrate appname

# 精确到某一个迁移文件则可使用
$ python manage.py migrate appname 文件名
```
9.bbs系统的表结构设计完成，下面是后台管理

9.1 注册后台admin，先编辑bbs/admin.py文件（见代码）

9.2 注册后台管理的超级用户
```
$ python manage.py createsuperuser
```

9.3 启动服务，访问后台
```
python manage.py runserver 127.0.0.1:8000
```
10. 前端
