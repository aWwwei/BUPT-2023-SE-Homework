'''
@ 文件名：ReadConfig.py
@ 文件功能描述：用户自动测试类
@ 创建日期：2020年6月11日
@ 创建人：罗阳
@ 修改描述：添加读取初始温度的静态方法
@ 修改日期：2020年6月24日
'''

import configparser


class Config:
    @staticmethod
    def getDatebase():
        cf = configparser.ConfigParser()
        cf.read("config.ini", encoding="utf-8")
        database = cf.items("DATABASE")
        database = dict(database)
        return database

    @staticmethod
    def getDispatch():
        cf = configparser.ConfigParser()
        cf.read("config.ini", encoding="utf-8")
        dispatch = cf.items("DISPATCH")
        dispatch = dict(dispatch)
        return dispatch

    @staticmethod
    def getTempcontrol():
        cf = configparser.ConfigParser()
        cf.read("config.ini", encoding="utf-8")
        tempcontrol = cf.items("TEMPCONTROL")
        tempcontrol = dict(tempcontrol)
        return tempcontrol

    @staticmethod
    def getBegintemp():
        cf = configparser.ConfigParser()
        cf.read("config.ini", encoding="utf-8")
        beginTemp = cf.items("BEGINTEMP")
        beginTemp = dict(beginTemp)
        return beginTemp

    @staticmethod
    def getTest():
        cf = configparser.ConfigParser()
        cf.read("config.ini", encoding="utf-8")
        test = cf.items("TEST")
        test = dict(test)
        return test

if __name__ == '__main__':
    print(Config.getDatebase())
