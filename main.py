import TextPreprocess
import Process
import Features
import Similarity
import sys


wordlist_s = TextPreprocess.Tokens(sys.argv[1])
wordlist_e = TextPreprocess.Tokens(sys.argv[2])

dict_s = Process.DictBiulder(wordlist_s)
dict_e = Process.DictBiulder(wordlist_e)

Fin_dict = Process.MergeDict(dict_s, dict_e)

V1 = Features.GetVector(dict_s, Fin_dict)
V2 = Features.GetVector(dict_e, Fin_dict)
ans = Similarity.CosineSimilarity(V1, V2)

with open(sys.argv[3], 'w') as f_obj:
    if ans == 0:
        f_obj.write("0.00")
    else:
        temp = str(ans)
        contents = ''
        for i in range(0, 4):
            contents = contents + temp[i]
        f_obj.write(contents)
