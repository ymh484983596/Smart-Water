#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023-11-08 10:00
# @Author : Ther
from flask import Flask,render_template,request,jsonify
from common.json_response import JsonResponse


class JsonFlask(Flask):
    def make_response(self, rv):
        # 如果返回的是json格式的数据
        if rv is None or isinstance(rv,(list,dict)):
            rv=JsonResponse.success(rv)

        if isinstance(rv,JsonResponse):
            rv=jsonify(rv.to_dict())

        return super().make_response(rv)