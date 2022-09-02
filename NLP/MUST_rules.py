# -*- codeing = utf-8 -*-
# @Time : 8/21/2022 11:21 PM
# @Author : Shao
# @File : MUST_rules.py
# @Software : PyCharm
import requests
import spacy

from utils.config import DATASET_INDEX, INDEX

nlp = spacy.load("en_core_web_sm")

list_ = []
file_ = open('../Dataset/must.txt', encoding='utf-8')
for sentence in file_:
    list_.append(sentence)
for sents in list_:
    doc = nlp(sents)
    for token in doc:
        if str(token) == 'MUST':
            print(sents)
            for token1 in doc:
                if str(token1.dep_) == 'ROOT':
                    print(token1)

# for i in INDEX:
#     list_ = []
#     file_ = open('../Dataset/'+str(i)+'.xml', encoding='utf-8')
#     for sentence in file_:
#         list_.append(sentence)
#     for sents in list_:
#         doc = nlp(sents)
#         for token in doc:
#             if str(token) == 'MUST':
#                 print('../Dataset/'+str(i)+'.xml')
#                 print(sents)
#                 break

# doc = nlp("MUST trigger when an announcement is removed")
#
# for token in doc:
#     if str(token.dep_) == 'ROOT':
#         print(token)
#         for child in token.children:
#             print(child)
