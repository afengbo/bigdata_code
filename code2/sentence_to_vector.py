import jieba


def sentence_to_words(sentence1, sentence2):
    """
    将句子转化成关键词列表
    :param sentence1: 句子1
    :param sentence2: 句子2
    :return: 句子1关键词列表、句子2关键词列表、关键词字典（含序号）
    """
    # 读取停用词表（百度查找）
    stop_words = set()
    with open("stop_words.txt", "r", encoding="utf-8") as f:
        for word_list in f.readlines():
            word = word_list[0]
            stop_words.add(word)

    # 对句子进行分词，排除停用词，获取关键词列表，去重(set)
    word_list1 = [x for x in jieba.cut(sentence1, cut_all=True) if x not in stop_words and x != '']
    word_list2 = [x for x in jieba.cut(sentence2, cut_all=True) if x not in stop_words and x != '']
    word_set1 = set(word_list1)
    word_set2 = set(word_list2)

    # 给每个关键词加上序号
    word_dict = dict()
    i = 0
    for word in word_set1.union(word_set2):
        word_dict[word] = i
        i += 1
    return word_list1, word_list2, word_dict


def word_to_vector(word_dict, word_list):
    """
    将关键词转化成向量值
    :param word_dict: {关键词:序号}
    :param word_list: 关键词list
    :return: 向量list
    """
    word_count = dict()
    # 限定向量长度
    s_vector = [0] * len(word_dict)
    # 计算词频
    for word in word_list:
        if not word_count.get(word):
            word_count[word] = 1
        else:
            word_count[word] += 1
    # 将词频对应到向量中
    for word, frequency in word_count.items():
        wid = word_dict[word]
        s_vector[wid] = frequency
    return s_vector


if __name__ == '__main__':
    s1 = "这只皮靴号码大了。那只号码合适"
    s2 = "这只皮靴号码不小，那只更合适"
    s1_list, s2_list, word_dict = sentence_to_words(s1, s2)
    s1_vector = word_to_vector(word_dict, s1_list)
    s2_vector = word_to_vector(word_dict, s2_list)
    print(s1_vector)
    print(s2_vector)
