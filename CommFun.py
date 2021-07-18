#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import time
import struct
import re
import math
#模块导入

#支持转换为 int 类型的，仅有 float、str、bytes，其他类型均不支持
def float_to_int(num):
    return int(num)
def str_to_int(st):
    return int(st)
def bytes_to_int(byt):
    return int(byt)

#支持转换为 float 类型的，仅有 int、str、bytes，其他类型均不支持
def int_to_float(num):
    return float(num)
def str_to_float(st):
    return float(st)
def bytes_to_float(byt):
    return float(byt)

#仅支持 int、float、str 转换成 complex 类型    
def int_to_complex(num):
    return complex(num)
def str_to_complex(st):
    return complex(st)
def float_to_complex(fl):
    return complex(fl)

#print(str(''.join(['a','b'])))

def stlist_to_str(li):
    return str(''.join(li))


def bytes_to_str(byt,encoding = 'utf-8'):
    #byt.decode()
    return str(byt,encoding)
'''print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode())
b= b'hello'
print(type(b),b)
print(bytes_to_str(b))'''

def str_to_bytes(st,encoding='utf-8'):
    #st.encode()
    return bytes(st, encoding)

#print(str_to_bytes('中国'))

#字节转list,按count字节组list
def hexbytes_to_list(byt,count=1):
    data_len=math.ceil(len(byt)/count)
    print(data_len)
    i=0
    li = []
    while(i<data_len):
        btype = byt[i*count:(i+1)*count]
        stype = bytes.decode(btype)
        htype = int(stype,16)
        li.append(htype)
        i+=1
    return li

'''b = b'123456'
print(hexbytes_to_list(b,4))'''


def str_to_hex(s):
    """
    字符串 转 16进制
    :param s:
    :return:
    """
    return ' '.join([c.encode().hex() for c in s])
#print(str_to_hex("1234"))

def hex_to_str(s):
    """
    16进制转 str
    :param s:
    :return:
    """
    return bytes.fromhex(s).decode()
#print(hex_to_str('1234'))

def int_to_binascii(data,bits):
  return binascii.b2a_hex(data.to_bytes(bits,byteorder='little', signed=False))


def bytesToHexString(bs):
  hex_str = ''
  for item in bs:
    hex_str += str(hex(item))[2:].zfill(2).upper() + " "

  return hex_str
  #return ''.join(['%02X' % b for b in bs])

#print(bytesToHexString(b'1234'))



#时间戳转换为日期:0转换为2000-01-01 00:00:00
def TimestampToData(time_sj):
    time_sj+=946656000 #1970-01-01 00：00：00 ~2000-01-01 00：00：00 的时间戳
    data_sj = time.localtime(time_sj)
    return data_sj
#日期转换为时间戳:2000-01-01 00:00:00转换为0
def DataToTimestamp(time_sj):
    # 转换成时间数组
    timeArray = time.strptime(time_sj, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = int(time.mktime(timeArray))-946656000
    return timestamp
#print(hex(DataToTimestamp('2020-01-01 00:01:01')))

