
# https://www.cnblogs.com/moonhmily/p/11119513.html

# php主要实现数据交互和网页内容提取，python使用了jieba分词、wordcloud词云两个库，jieba主要对提取的网页内容进行分词处理，wordcloud是词云图片工具的核心库，
# 导入模块
import requests                 # 获取网页的请求
from bs4 import BeautifulSoup   # 解析网址借助beautifulsoup4模块
import pandas as pd             # 保存为CSV数据

# 请求、解析、保存弹幕数据
# # 请求弹幕数据
url = 'http://comment.bilibili.com/99768393.xml'
html = requests.get(url).content
print(html)
'''
requests对象的get和post方法都会返回一个Response对象，这个对象里面存的是服务器返回的所有信息，包括响应头，响应状态码等。
其中返回的网页部分会存在.content和.text两个对象中。
两者区别在于，content中间存的是字节码，而text中存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。
直接输出content，会发现前面存在b'这样的标志，这是字节字符串的标志，而text是，没有前面的b,对于纯ascii码，这两个可以说一模一样，
对于其他的文字，需要正确编码才能正常显示。大部分情况建议使用.text，因为显示的是汉字，但有时会显示乱码，
这时需要用.content.decode('utf-8')，中文常用utf-8和GBK，GB2312等。这样可以手工选择文字编码方式。
所以简而言之，.text是现成的字符串，.content还要编码，但是.text不是所有时候显示都正常，这是就需要用.content进行手动编码。
'''

# 解析弹幕数据
html_data = str(html,'utf-8')
bs4 = BeautifulSoup(html_data,'lxml')
results = bs4.find_all('d') # 返回一个列表，列表里面是所有的符合要求的对象
comments = [comment.text for comment in results]
comments_dict = {'comments':comments}
print(comments_dict)

# 将弹幕数据保存到本地
br = pd.DataFrame(comments_dict)
print(br)
br.to_csv(r'E:\XCZG\Project\Study-Project\data\databarrage.csv',encoding='utf')
print("保存完成")




