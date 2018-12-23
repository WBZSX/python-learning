import os
from os import path
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from scipy.misc import imread
import random

#def wc_english():
	# 获取当前文件路径
d = path.dirname(_file_) if "_file_" in locals() else os.getcwd()
	#获取文本text
text = open(path.join(d,'legend.txt')).read()
	#读取背景图片
background_Image = np.array(Image.open(path.join(d,'legend.jpg')))
	#提取背景图片颜色
img_colors = ImageColorGenerator(background_Image)
	#设置英文停止词
stopwords = set(STOPWORDS)
wc = WordCloud(margin = 2,scale = 2, max_words = 200,min_font_size = 4,stopwords = stopwords,random_state = 42, max_font_size = 150,)
wc.generate_from_text(text)
wc.recolor(color_func = img_colors)
wc.to_file('1900prol.png')
	#显示图像
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout()
	#存储图像
	#or#plt.savingfig('1900_basic.png',dpi=200)
plt.show()
