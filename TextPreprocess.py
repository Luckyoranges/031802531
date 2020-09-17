import jieba
from collections import defaultdict
import stopwords

def Tokens(filename):
    "对初始文本进行分词、去停用词,返回分词列表"
    # 去除文本空格、空行
    with open(filename, encoding='utf=8') as f_obj:
        lines = f_obj.readlines()
        contents = ''
        for line in lines:
            contents = contents + line.strip()

    # 分词
    text = jieba.lcut(contents)

    # 导入停用词表
    stopword_list = stopwords.stopwords()

    # 去停用词
    seg = []
    for word in text:
        if word not in stopword_list:
            seg.append(word)
    return seg