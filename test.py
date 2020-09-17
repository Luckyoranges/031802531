import unittest
import TestFunction

class TextTestCase(unittest.TestCase):

    def test_self(self):
        print("orig.txt的文本相似度如下：\n")
        TestFunction.test_main("orig.txt", "testfile\orig.txt", "ans1.txt")
    
    def test_orig_add(self):
        print("orig_0.8_add.txt的文本相似度如下：\n")
        TestFunction.test_main("orig.txt", "testfile\orig_0.8_add.txt", "ans2.txt")

    def test_orig_dis1(self):
        print("orig_0.8_dis_1.txt的文本相似度如下：\n")
        TestFunction.test_main("orig.txt", "testfile\orig_0.8_dis_1.txt", "ans3.txt")

    def test_orig_dis3(self):
        print("orig_0.8_dis_3.txt的文本相似度如下：\n")
        TestFunction.test_main("orig.txt", "testfile\orig_0.8_dis_3.txt", "ans4.txt")

    def test_orig_dis7(self):
        print("orig_0.8_dis_7.txt的文本相似度如下：\n")
        TestFunction.test_main("orig.txt", "testfile\orig_0.8_dis_7.txt", "ans5.txt")

    def test_orig_dis10(self):
        print("orig_0.8_dis_10.txt的文本相似度如下：\n")
        TestFunction.test_main("orig.txt", "testfile\orig_0.8_dis_10.txt", "ans6.txt")

    def test_orig_dis15(self):
        print("orig_0.8_dis_15.txt的文本相似度如下：\n")
        TestFunction.test_main("orig.txt", "testfile\orig_0.8_dis_15.txt", "ans7.txt")
    
    def test_orig_mix(self):
        print("orig_0.8_mix.txt的文本相似度如下：\n")
        TestFunction.test_main("orig.txt", "testfile\orig_0.8_mix.txt", "ans8.txt")
    
    def test_orig_rep(self):
        print("orig_0.8_rep.txt的文本相似度如下：\n")
        TestFunction.test_main("orig.txt", "testfile\orig_0.8_rep.txt", "ans9.txt")

unittest.main()