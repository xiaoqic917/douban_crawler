# -*-coding = utf-8 -*-
# @Time: 2021/1/14 11:29
# @Author:Xiaoqi CHAI
# @File: teat_Cloud.py
# @Software: PyCharm
import jieba #participle make one sentence to multiple words
from matplotlib import pyplot as plt # drawing data visualization
from wordcloud import WordCloud # word cloud, mask
from PIL import Image #process image
import numpy as np # matrix operation
import sqlite3 #database

# word cloud is ready
con=sqlite3.connect("movies.db")
cur=con.cursor()
sql="select intro from movie250"
data=cur.execute(sql)
text=""
for item in data:
    #print(item[0])
    text=text+item[0]
cur.close()
con.close()

#participle
cut=jieba.cut(text)
string =' '.join(cut)

img=Image.open(r'static\assets\img\tree.jpg')
img_array=np.array(img)# img to array
wc=WordCloud(
    background_color="white",
    mask=img_array,
    font_path="msyh.ttc"

)
wc.generate_from_text(string)

# draw img
fig=plt.figure(1)
plt.imshow(wc)
plt.axis("off")# not show axis
#plt.show()

#exporter the img as file
plt.savefig(r'static\assets\img\word.jpg',dpi=500)