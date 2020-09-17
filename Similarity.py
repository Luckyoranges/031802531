import numpy

def CosineSimilarity(v1, v2):
    "计算两个向量的余弦相似度"

    # 计算向量内积
    a1 = numpy.array(v1)
    a2 = numpy.array(v2)
    product = numpy.dot(a1, a2)
    
    # 计算向量模长
    mod1 = numpy.sqrt((a1*a1).sum())
    mod2 = numpy.sqrt((a2*a2).sum())
    
    mod = mod1 * mod2
    ans = float(product) / mod
    return ans
