import os
import math

file_path = "./data"

i = 0
# 获取文章和对应每篇文章的词频TF
doc_words = dict()
for filename in os.listdir(file_path):
    # 打印加载的文件数量
    if i % 100 == 0:
        print(i, 'files loaded!')
    # 统计每篇文章中的关键词词频
    with open(file_path + '/' + filename, 'r', encoding='utf-8') as f:
        word_count = dict()
        for line in f.readlines():
            words = line.strip().split(" ")
            for word in words:
                if len(word.strip()) < 1:      # 空字符、制表位、回车不做计数
                    continue
                if not word_count.get(word):
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    doc_words[filename] = word_count
    i += 1

doc_nums = float(i)

# 统计每个词在多少篇文章出现过
word_frequency = dict()
for doc in doc_words.keys():
    for word in doc_words[doc].keys():
        if not word_frequency.get(word):
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1

# 套idf公式
# 反文档频率（IDF）= log（语料库的文档总数/包含该词的文档数+1）
for word in word_frequency.keys():
    word_frequency[word] = math.log(doc_nums / float(word_frequency[word] + 1))
# print(word_frequency)

# TF-IDF = 词频（TF）*反文档频率（IDF）
print(doc_words['1yule.seg.cln.txt']['芭芭拉'])
for doc in doc_words.keys():
    for word in doc_words[doc].keys():
        doc_words[doc][word] *= word_frequency[word]
print(doc_words['1yule.seg.cln.txt']['芭芭拉'])
