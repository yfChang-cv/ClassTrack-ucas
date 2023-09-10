# 国科大课程表时间信息
import requests as req
import re
from bs4 import BeautifulSoup as bf

from data import Course, Geo

WEEK = {
    '星期一': 1,
    '星期二': 2,
    '星期三': 3,
    '星期四': 4,
    '星期五': 5,
    '星期六': 6,
    '星期日': 7
}

# 果壳教学楼信息
UCAS_GEO = {
    '教一楼': Geo("教学楼1", 40.25, 116.41),
    '教二楼': Geo("教学楼2", 40.25, 116.41),
    '雁栖湖东区礼堂': Geo("教学楼2", 40.25, 116.41),
    '运动场东区体育馆-篮球': Geo("运动场东区体育馆", 40.25, 116.41)
}


def format_course_period(s: str):
    # 前半部分是星期几
    s = s.split('：')
    # 切片，到数字，分割，确定第几节课
    m = re.search(r'\d[、\d]*', s[1])
    lesson = s[1][m.start():m.end()].split('、')
    lesson = list(map(int, lesson))
    return [s[0], lesson]


# 获取课程主讲教师
# 输入课程时间url(coursetime)
def get_course_teacher(url: str):
    url = url.replace('coursetime', 'courseplan')
    resp = req.get(url)
    html = resp.text
    bs_obj = bf(html, "html.parser")
    teacher_tag = bs_obj.select('#main-content > div > div > div.m-cbox.m-lgray > div.mc-body > p:nth-child(2) > '
                                'span:nth-child(6)')
    teacher = bf(str(teacher_tag), "html.parser")
    if teacher.text == '[]':
        return ' '
    return teacher.text.split("：")[1][0:-1]


def add_course(urls):
    courses = []
    course_time_urls = urls
    for url in course_time_urls:
        # 获取课程主讲老师名字
        teacher = get_course_teacher(url)
        # 获取课程时间相关信息
        resp = req.get(url)
        html = resp.text
        bs_obj = bf(html, "html.parser")
        # 1.获取课程名称
        course_title = bs_obj.select('#main-content > div > div > div.m-cbox.m-lgray > div.mc-body > p:nth-child(1)')
        course_title = bf(str(course_title), "html.parser")
        course_title = course_title.text.split("：")[1][0:-1]
        # 2.课程安排所在table
        tag = bs_obj.select('#main-content > div > div > div.m-cbox.m-lgray > div.mc-body > table')
        item_bs = bf(str(tag), "html.parser")
        info = item_bs.find_all('td')
        for i in range(0, len(info), 3):
            # 2.1上课时间（星期，课次）
            course_time = format_course_period(info[i].text)
            # 2.2上课教室(楼号，教室号)
            course_class = info[i + 1].text
            # 2.3上课所在楼
            try:
                building_no = course_class[0: re.search(r'\d', course_class).start()]
            except AttributeError:
                building_no = course_class
            # 2.4上课周次
            course_week = list(map(int, info[i + 2].text.split('、')))
            # 生成Course对象
            tmp = Course(course_title, teacher, course_class, UCAS_GEO[building_no], WEEK[course_time[0]], course_week,
                         course_time[1])
            courses.append(tmp)
    return courses
