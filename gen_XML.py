#-*- codeing = utf-8 -*-
#@Time : 8/13/2022 5:19 PM
#@Author : Shao
#@File : gen_XML.py
#@Software : PyCharm

from xml.dom.minidom import Document
doc = Document()
people = doc.createElement("Rules")
doc.appendChild(people)
aperson = doc.createElement("EIP-20")
people.appendChild(aperson)
url = doc.createElement("URL")
aperson.appendChild(url)
url_name = doc.createTextNode("https://eips.ethereum.org/EIPS/eip-20")
url.appendChild(url_name)
name = doc.createElement("name")
aperson.appendChild(name)
personname = doc.createTextNode("Annie")
name.appendChild(personname)
typee = doc.createElement("type")
name.appendChild(typee)
personname1 = doc.createTextNode("Anniess")
typee.appendChild(personname1)
rule = doc.createElement("rules")
name.appendChild(rule)
# personname = doc.createTextNode("Annie")
# name.appendChild(personname)
filename = "rules.xml"
f = open(filename, "w")
f.write(doc.toprettyxml(indent=" "))
f.close()
