# -*- codeing = utf-8 -*-
# @Time : 9/18/2022 9:22 PM
# @Author : Shao
# @File : MUST_when.py
# @Software : PyCharm
# MUST trigger Staked event.

import spacy

nlp = spacy.load("en_core_web_sm")


def must_rule1():
    file_ = open('../Dataset/must_when.txt', encoding='utf-8')
    rule1_ = []
    for sents in file_:
        doc = nlp(sents)
        event = []
        m = False
        obj = False
        ca = False
        for token in doc:
            if str(token) == 'MUST':
                m = True
            elif str(token) == 'when':
                obj = True
            elif str(token.pos_) == 'VERB':
                event.append(str(token))
        if m and obj:
            print(sents, end='')
            print(event)


def must_rule2():
    file_ = open('../Dataset/must_when.txt', encoding='utf-8')
    i = 1
    lis = {}
    for sents in file_:
        if i % 2 == 1:
            if not lis.__contains__(sents):
                lis.append(sents)
        i += 1
    for lq in lis:
        print(lq, end='')


if __name__ == '__main__':
    must_rule2()
