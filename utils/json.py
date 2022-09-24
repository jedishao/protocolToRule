# -*- codeing = utf-8 -*-
# @Time : 9/23/2022 9:31 AM
# @Author : Shao
# @File : json.py
# @Software : PyCharm
import json
import spacy

from utils import config


def write_json():
    tesdic1 = {
        'function': 'Tom1',
        'emit': 'MUST',
        'event': 'ds'
    }
    with open("../Rule/Rule1.json", 'w', encoding='utf-8') as fw:
        json.dump(tesdic1, fw, indent=4, ensure_ascii=False)


def get_name():
    eip = []
    result = {}
    for i in config.DATASET_INDEX:
        path = '../Dataset/Raw-data/' + str(i) + '.xml'
        nlp = spacy.load("en_core_web_sm")
        file_ = open(path, encoding='utf-8')
        event = []
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
                            for grandchild in child.children:
                                if str(grandchild.dep_) == 'compound':
                                    event.append(str(grandchild))
                    if m and obj:
                        result[str(i)] = event
    print(result)


def get_name1():
    eip = []
    result = {}
    for i in config.DATASET_INDEX:
        path = '../Dataset/Raw-data/' + str(i) + '.xml'
        nlp = spacy.load("en_core_web_sm")
        file_ = open(path, encoding='utf-8')
        event = []
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
                            for grandchild in child.children:
                                if str(grandchild.dep_) == 'compound':
                                    event.append(str(grandchild))
                    if m and obj:
                        result[str(i)] = event
    print(result)


def get_name2():
    path = '../Dataset/must_when.txt'
    nlp = spacy.load("en_core_web_sm")
    file_ = open(path, encoding='utf-8')
    i = 0
    for sents in file_:
        if i % 2 == 1:
            print(sents, end='')
        i += 1


if __name__ == '__main__':
    get_name2()
