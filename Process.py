from collections import defaultdict

def DictBiulder(word_list):
    "给定分词列表，得出特征词典（按照词频降序排列）"
    frequency = defaultdict(int)
    for word in word_list:
        frequency[word] += 1
    # 按词频降序排列，生成元组列表。排序的话maybe会减少一点后面遍历的时间，元组列表方便操作
    dic = sorted(frequency.items(), key=lambda t: t[1], reverse=True) 
    return dic

def MergeDict(T1,T2):
    "合并得到所有单词的列表"
    Fin_dic = []
    i = 0
    j = 0
    while i<len(T1) and j<len(T2):
        if T1[i][0] not in Fin_dic:
            Fin_dic.append(T1[i][0])
        if T2[j][0] not in Fin_dic:
            Fin_dic.append(T2[j][0])
        i = i + 1
        j = j + 1
    while i < len(T1):
        if T1[i][0] not in Fin_dic:
            Fin_dic.append(T1[i][0])
        i = i + 1
    while j < len(T2):
        if T2[j][0] not in Fin_dic:
            Fin_dic.append(T2[j][0])
        j = j + 1

    return Fin_dic
    