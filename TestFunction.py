import TextPreprocess
import Process
import Features
import Similarity
import sys

def test_main(filename_s, filename_e, filename_a):
    wordlist_s = TextPreprocess.Tokens(filename_s)
    wordlist_e = TextPreprocess.Tokens(filename_e)

    dict_s = Process.DictBiulder(wordlist_s)
    dict_e = Process.DictBiulder(wordlist_e)

    Fin_dict = Process.MergeDict(dict_s, dict_e)

    V1 = Features.GetVector(dict_s, Fin_dict)
    V2 = Features.GetVector(dict_e, Fin_dict)

    ans = Similarity.CosineSimilarity(V1, V2)
    with open(filename_a, 'w') as f_obj:
        temp = str(ans)
        contents = ''
        for i in range(0, 4):
            contents = contents + temp[i]
        f_obj.write(contents)
    print(contents)