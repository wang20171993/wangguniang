import xlrd
import pymysql
import config

def getExcleValue(sheetname,hang,lie):
    '''
    读取excle表里的具体内容
    '''
    excleName = config.testdata
    data = xlrd.open_workbook(excleName)
    table = data.sheet_by_name(sheetname)
    aaa = table.cell_value(hang,lie)
    return aaa


def getDbValue(sql):
    '''
    执行并返回查询到的数据库的值
    '''
    dbinfo = config.dbinfo
    db = pymysql.connect(**dbinfo)
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    return res
