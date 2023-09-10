#### description
该脚本可将国科大研究生课表导入到手机日历    
#### note

修改`https://github.com/guohaodong27/ucas_schedule.git`  
删除了自动爬取url的过程，修正了时间错误问题和课程详细页错误问题  
自动爬取url容易出现问题。

#### step

先将自己的sep账号登录，  
进入选课系统->院系课程选课->点击“课程名称”（例：矩阵分析与应用），  
进入课程时间页面，将网址粘贴到`urls.txt`文件中
例如：  

```txt
https://jwxkts2.ucas.ac.cn/course/coursetime/246298
https://jwxkts2.ucas.ac.cn/course/coursetime/246440
```

安装必要的python环境  
启动`main.py`，生成`课表.ics`，传入手机，直接点击文件，用日历打开。（必要的话，新建日历名称以备删改）  
如果出现上课地点错误，新的教学地点，在下方代码加入即可   

```python
UCAS_GEO
'教一楼': Geo("教学楼1", 40.25, 116.41),
'教二楼': Geo("教学楼2", 40.25, 116.41),
'雁栖湖东区礼堂': Geo("教学楼2", 40.25, 116.41),
'运动场东区体育馆-篮球': Geo("运动场东区体育馆", 40.25, 116.41)
}
```

