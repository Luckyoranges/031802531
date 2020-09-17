def GetVector(dic, Fin_dic):
    "计算以词频为权重的特征向量"
    TF = [0] * len(Fin_dic)
    
    for ch in range(len(Fin_dic)):
        for i in range(len(dic)):
            if dic[i][0] == Fin_dic[ch]:
                TF[ch] = dic[i][1]
                break

    return TF