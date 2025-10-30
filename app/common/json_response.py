#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023-11-08 9:54
# @Author : Ther
#统一的json返回格式
class JsonResponse(object):
    def __init__(self, code, msg,data):
        self.code = code
        self.msg = msg
        self.data = data

    #指定一个类的方法作为类方法，通常用self来传递当前类的实例--对象，cls传递当前类。
    @classmethod
    def success(cls,code=200,msg='success',data=None):
      return cls(code,msg,data)

    @classmethod
    def fail(cls, code=400,msg='fail',data=None):
        return cls(code,msg,data)


    def to_dict(self):
        return {
            'code':self.code,
            'msg':self.msg,
            'data':self.data
        }