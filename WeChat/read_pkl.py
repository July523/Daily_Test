# coding=utf-8 
#@Time :2018/11/9 23:04

import pickle

f = open('itchat.pkl','rb')
info = pickle.load(f)
print(info)