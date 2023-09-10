import gbk2utf8
from data import AppleMaps, Course, Geo, School
import re
from schedule import add_course

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    urls = []
    with open('urls.txt', 'r') as f:
        while f:
            try:
                url = re.search(r'http.*$', f.readline()).group()
                urls.append(url)
            except AttributeError:
                break
            else:
                print('url读取成功')
    # 获取课程列表
    courses = add_course(urls)
    # 初始化对象
    school = School(
        duration=50,  # 每节课时间为 50 分钟
        timetable=[
            (8, 30),  # 上午第一节课时间为 8:30 至 9:15
            (9, 20),
            (10, 30),
            (11, 20),
            (13, 30),  # 下午
            (14, 20),
            (15, 30),
            (16, 20),
            (18, 10),
            (19, 00),
            (20, 10),
            (21, 00)
        ],
        start=(2023, 8, 28),  # 2023 年 8 月 28 日是开学第一周星期一
        courses=courses
    )

    with open("课表.ics", "w", encoding='gbk') as w:
        w.write(school.generate())

    # 国科大网站是gbk编码，手机等使用utf8。因此需要转换编码
    gbk2utf8.trans_file_encoding()
