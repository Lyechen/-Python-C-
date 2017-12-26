# _*_ coding:utf-8 _*_
import time
import os
import requests
from bs4 import BeautifulSoup
from urlparse import urlparse
import pdfkit


html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""


def parse_url_to_html(url, name):
    """
    解析URL，返回HTML内容
    :param url:解析的url
    :param name: 保存的html文件名
    :return: html
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html5lib')
        # 菜鸟正文
        body = soup.find_all(class_="article-intro")
        # 廖雪峰正文
        # body = soup.find_all(class_="x-wiki-content x-main-content")
        # 标题
        # title = soup.find_all('h1')[1].get_text()

        # 标题加入到正文的最前面，居中显示
        # center_tag = soup.new_tag("center")
        # title_tag = soup.new_tag('h1')
        # title_tag.string = title
        # center_tag.insert(1, title_tag)
        # body.insert(1, center_tag)
        h = body
        html = h[0]
        # body中的img标签的src相对路径的改成绝对路径
        # pattern = "(<img .*?src=\")(.*?)(\")"
        #
        # def func(m):
        #     if not m.group(3).startswith("http"):
        #         rtn = m.group(1) + domain + m.group(2) + m.group(3)
        #         return rtn
        #     else:
        #         return m.group(1) + m.group(2) + m.group(3)
        #
        # html = re.compile(pattern).sub(func, html)
        html = html_template.format(content=html)
        with open(name, 'wb') as f:
            f.write(html)
        return name

    except Exception as e:
        # logging.error("解析错误: " + e, exc_info=True)
        print e


def get_url_list(url):
    """
    获取所有URL目录列表
    :return:
    """
    last_position = find_last(url, "/") + 1
    tutorial_url_head = url[0:last_position]
    domain = get_domain(url) + "/"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # 菜鸟侧边栏
    menu_tag = soup.find(class_="design")
    # 廖雪峰侧边栏
    # menu_tag = soup.find(class_="x-sidebar-left-content")
    urls = []
    for a in menu_tag.find_all("a"):
        href = str(a.get('href'))
        result = href.find('/')
        if result == -1:
            url = tutorial_url_head + href
        else:
            if domain[-1] == "/" and href[0] == '/':
                href = href[1:]
            url = domain + href
        urls.append(url)
    return urls


def save_pdf(htmls, file_name):
    """
    把所有html文件保存到pdf文件
    :param htmls:  html文件列表
    :param file_name: pdf文件名
    :return:
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    pdfkit.from_file(htmls, file_name, options=options)


def find_last(string, char):
    last_position = -1
    while True:
        position = string.find(char, last_position + 1)
        if position == -1:
            return last_position
        last_position = position


def get_domain(url):
    r = urlparse(url)
    return r.scheme + "://" + r.netloc


def main(url, file):
    start = time.time()
    urls = get_url_list(url)
    file_name = u"%s.pdf" % file
    htmls = [parse_url_to_html(url, str(index) + ".html") for index, url in enumerate(urls)]
    print(htmls)
    save_pdf(htmls, file_name)

    for html in htmls:
        os.remove(html)

    total_time = time.time() - start
    print u"总共耗时：%f 秒" % total_time

if __name__ == '__main__':
    # 菜鸟
    url = "http://www.runoob.com/python3/python3-tutorial.html"
    # 廖雪峰
    # url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
    file = "runoob"
    main(url, file)
