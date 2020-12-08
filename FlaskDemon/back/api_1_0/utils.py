#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import make_response, jsonify


def jsonify_with_args(data, code=200, *args):
    """
    返回json数据同时修改返回状态码,etc
    :param data:
    :param code:
    :param args:
    :return:
    """

    assert isinstance(data, dict)
    # 解决 跨域
    # resp = make_response(data)
    # resp.headers['Content-Type'] = 'application/json;text/html;charset=utf-8'
    # resp.headers["Access-Control-Allow-Origin"] = '*'
    # resp.headers["Access-Control-Allow-Methods"] = 'OPTIONS,HEAD,GET,POST'
    # resp.headers["Access-Control-Allow-Headers"] = 'x-requested-with,content-type'

    return make_response(jsonify(data),code,*args)
