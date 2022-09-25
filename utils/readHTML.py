#-*- codeing = utf-8 -*-
#@Time : 8/11/2022 10:39 PM
#@Author : Shao
#@File : readHTML.py
#@Software : PyCharm

from lxml import etree
import requests


def get_protocol(url, func_index, const_index):

    resp = requests.get(url)
    page_source = resp.text
    tree = etree.HTML(page_source)

    # print(tree.xpath('//h4[@id]')[1].xpath('string(.)'))
    func = tree.xpath('//h4[@id]')[func_index].xpath('string(.)')
    # func = tree.xpath('//id[@*]')[0].xpath('string(.)')
    constraint = tree.xpath('/html/body/main/div/div/p['+str(const_index)+']')[0].xpath('string(.)')
    #constraint = tree.xpath('/html/body/main/div/div/p')[0].xpath('string(.)')
    print(len(tree.xpath('/html/body/main/div/div/p')))
    return func, constraint


def get_constraint(url):
    constraint = []
    resp = requests.get(url)
    page_source = resp.text
    tree = etree.HTML(page_source)

    for index in range(len(tree.xpath('/html/body/main/div/div/p'))):
        constraint.append(tree.xpath('/html/body/main/div/div/p')[index].xpath('string(.)'))

    return constraint


if __name__ == '__main__':
    url_ = 'https://eips.ethereum.org/EIPS/eip-20'
    index_ = 12
    for index_ in range(12):
        func_, constraint_ = get_protocol(url_, index_, index_+5)
        print(func_)
        print(constraint_)
