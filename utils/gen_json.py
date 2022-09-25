#-*- codeing = utf-8 -*-
#@Time : 9/25/2022 5:54 PM
#@Author : Shao
#@File : gen_json.py
#@Software : PyCharm

# -*- codeing = utf-8 -*-
# @Time : 9/23/2022 9:31 AM
# @Author : Shao
# @File : json.py
# @Software : PyCharm
import json
import spacy
import re

from utils import config


def write_json():
    func = [['transfer', 'transfertoken', 'transfertoken(.+)'], ['make', 'makechange', 'makechange(.+)'],
            ['make', 'makechange', 'makechange(.+)'], ['freeze', 'freezeaccount', 'freezeaccount(.+)'],
            ['create', 'createannouncement', 'createannouncement(.+)'],
            ['remove', 'removeannouncement', 'removeannouncement(.+)'],
            ['transfer', 'transfertoken', 'transfertoken(.+)'], ['transfer', 'transfertoken', 'transfertoken(.+)'],
            ['update', 'updateURI', 'updateURI(.+)'], ['transfer', 'transferownership', 'transferownership(.+)'],
            ['create', 'createidentity', 'createidentity(.+)'], ['add', 'addaddress', 'addaddress(.+)'],
            ['remove', 'removeaddress', 'removeaddress(.+)'], ['add', 'addprovider', 'addprovider(.+)'],
            ['remove', 'removeprovider', 'removeprovider(.+)'], ['add', 'addresolver', 'addresolver(.+)'],
            ['remove', 'removeresolver', 'removeresolver(.+)'], ['trigger', 'triggerchange', 'triggerchange(.+)'],
            ['trigger', 'triggerrecovery', 'triggerrecovery(.+)'],
            ['destroy', 'destroyidentity', 'destroyidentity(.+)'], ['approve', 'approveupdate', 'approveupdate(.+)'],
            ['add', 'addid', 'addid(.+)'], ['remove', 'removeid', 'removeid(.+)'], ['set', 'setscope', 'setscope(.+)'],
            ['issue', 'issuebond', 'issuebond(.+)'], ['redeem', 'redeembond', 'redeembond(.+)'],
            ['redeem', 'redeembond', 'redeembond(.+)'], ['burn', 'burnbond', 'burnbond(.+)'],
            ['transfer', 'transferbond', 'transferbond(.+)'], ['pass', 'passtransaction', 'passtransaction(.+)'],
            ['transfer', 'transfervalue', 'transfervalue(.+)'], ['change', 'changeconsumer', 'changeconsumer(.+)'],
            ['deposit', 'deposittoken', 'deposittoken(.+)'], ['withdraw', 'withdrawshare', 'withdrawshare(.+)'],
            ['change', 'changemetadata', 'changemetadata(.+)'], ['change', 'changeaddress', 'changeaddress(.+)'],
            ['upgrade', 'upgradetoken', 'upgradetoken(.+)'], ['downgrade', 'downgradetoken', 'downgradetoken(.+)'],
            ['transfer', 'transferEXP', 'transferEXP(.+)'], ['authorize', 'authorizeslot', 'authorizeslot(.+)'],
            ['revoke', 'revokeauthorization', 'revokeauthorization(.+)'], ['change', 'changeuser', 'changeuser(.+)'],
            ['terminate', 'terminaterent', 'terminaterent(.+)']]

    with open("../Rule/Rule2.json", 'a+', encoding='utf-8') as fw:
        for i in range(len(func)):
            js = {'EIP': '', 'event': '', 'emit': 'MUST WHEN', 'functions': func[i]}
            json.dump(js, fw, indent=4, ensure_ascii=False)
            fw.write(',')
            fw.write('\n')


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


def test():
    line = 'add'
    m = re.match(r'add(.+)', line)
    print(m)


if __name__ == '__main__':
    write_json()
