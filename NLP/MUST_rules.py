# -*- codeing = utf-8 -*-
# @Time : 8/21/2022 11:21 PM
# @Author : Shao
# @File : MUST_rules.py
# @Software : PyCharm
import requests
import spacy

from utils import config

nlp = spacy.load("en_core_web_sm")


# for sents in list_:
#     doc = nlp(sents)
#     for token in doc:
#         if str(token.pos_) == 'VERB' and str(token.lemma_) in ['trigger', 'suupport', 'fire', 'emit']:
#             for child in token.children:
#                 if str(child) == 'MUST':
#                     print(sents)

def all_must():
    for i in config.DATASET_INDEX:
        path = '../Dataset/Raw-data/' + str(i) + '.xml'
        file_ = open(path, encoding='utf-8')
        sentences = []
        j = 0
        for sentence in file_:
            sentences.append(sentence)
        for sents in sentences:
            doc = nlp(sents)
            for token in doc:
                if str(token) == 'MUST':
                    if j == 0:
                        j += 1
                        print(path)
                    print(sents)
                    break


# MUST trigger Staked event.
def must_rule1():
    # file_ = open('../Dataset/must.txt', encoding='utf-8')
    # rule1_ = []
    for i in config.DATASET_INDEX:
        path = '../Dataset/Raw-data/' + str(i) + '.xml'
        file_ = open(path, encoding='utf-8')
        for sents in file_:
            doc = nlp(sents)
            event = None
            m = False
            obj = False
            for token in doc:
                r = []
                if str(token) == 'MUST':
                    m = True
                elif str(token) == 'when':
                    obj = True
            if m and obj:
                print(path)
                print(sents, end='')
                # if str(token.pos_) == 'VERB' and str(token.lemma_) in ['trigger', 'suupport', 'fire', 'emit']:
                # if str(token.pos_) == 'VERB':
                #     for child in token.children:
                #         if str(child.dep_) == 'advmod' and str(child).lower() == 'when':
                #             print(path)
                #             print(sents, end='')
                #     if str(child) == 'MUST':
                #         m = True
                #     if str(child.dep_) == 'dobj' and str(child).lower() == 'event':
                #         obj = True
                #         for c in child.children:
                #             if str(c.dep_) in ['compound', 'amod']:
                #                 event = str(c)
                # if m and obj:
                #     print(sents, end='')
                # r.append(str(token))
                # r.append(event)
                # rule1_.append(r)
                # if event is None:
                #     print(sents, end='')
        #return rule1_


# MUST be triggered when a resolver is added.
def must_rule2():
    file_ = open('../Dataset/must.txt', encoding='utf-8')
    for sents in file_:
        m = False
        obj = False
        doc = nlp(sents)
        for token in doc:
            if str(token.pos_) == 'VERB' and str(token.lemma_) in ['trigger', 'suupport', 'fire', 'emit']:
                for child in token.children:
                    if str(child) == 'MUST':
                        m = True
                    if str(child.dep_) == 'auxpass' and str(child).lower() == 'be':
                        obj = True
        if m and obj:
            print(sents)


def must_rule3():
    file_ = open('../Dataset/must_1_1.txt', encoding='utf-8')
    ve = []
    for sents in file_:
        m = False
        obj = False
        doc = nlp(sents)
        for token in doc:
            if str(token.pos_) == 'VERB':
                for child in token.children:
                    if str(child) == 'MUST':
                        m = True
                    if str(child.dep_) == 'dobj' and str(child).lower() == 'event':
                        obj = True
                if m and obj:
                    m = False
                    obj = False
                    if not ve.__contains__(str(token)):
                        ve.append(str(token))
    for t in ve:
        print(t)


if __name__ == '__main__':
    must_rule1()
    # for r in result:
    #     print(r)
#    all_must()
