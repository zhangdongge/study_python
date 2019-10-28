# 接下来，对保存好的弹幕数据进行深加工
# 制作词云，用到wordcloud模块、matplotlib模块，jieba模块。
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import jieba

# 读取文本信息(弹幕数据)，进行分词并连接起来
# 读取文件内容
br = pd.read_csv(r'E:\XCZG\Project\Study-Project\data\databarrage.csv',header=None)
print(br)
# 进行分词，并用空格连起来
text = ''
for line in br[1]:
    text +=' '.join(jieba.cut(line,cut_all=False)) # 返回生成器，遍历生成器即可获得分词的结果

# 解析背景图片
mask_img = plt.imread(r'E:\XCZG\Project\Study-Project\code\xin.png')
'''设置词云样式'''
wc = WordCloud(
    # 设置字体
    font_path = 'SIMYOU.TTF',
    # 允许最大词汇量
    max_words=2000,
    max_font_size=80,
    # 设置使用的背景图片
    mask = mask_img,
    background_color = None,mode="RGBA",
    # 设置与多少种随机生成状态，即有多少种配色方案
    random_state=30)
# 生成词云
wc.generate_from_text(text)
#改变字体颜色
img_colors = ImageColorGenerator(mask_img)
#字体颜色为背景图片的颜色
wc.recolor(color_func=img_colors)
# 显示词云图
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 将图片保存到本地
wc.to_file(r"E:\XCZG\Project\Study-Project\code\Garbage_classification.png")
print(f'生成词云成功!')