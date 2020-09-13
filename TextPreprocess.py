import jieba

def Tokens(contents):
    "对初始文本进行分词、去停用词,返回分词列表"
    text = jieba.lcut(contents)

    with open("stopwords.txt", encoding = "utf-8") as f_obj:
        lines = f_obj.readlines()
    stopword_set = set()
    for line in lines:
        stopword_set.add(line.strip().encode('utf-8').decode('utf8'))

    seg = []
    for word in text:
        if word not in stopword_set:
            seg.append(word)
    return seg