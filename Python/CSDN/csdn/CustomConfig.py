#!/usr/bin/python
#coding: utf-8
# 和arts一起组成博客地址
url = 'https://blog.csdn.net/h___q/article/details/'

# 代理地址
proxys = [{'http':'121.31.102.100'},{'http':'117.21.144.223'},{'http':'223.150.38.38'},{'http':'223.150.38.48'},
          {'http':'223.150.38.10'},{'http':'211.136.127.125'},{'http':'180.118.134.103'},{'http':'60.188.38.186'},
          {'http':'223.150.38.60'},{'http':'114.234.82.149'},{'http':'182.96.245.111'},{'http':'211.136.127.125'},
          {'http':'125.110.111.198'},{'http':'106.12.22.41'},{'http':'121.31.102.100'},{'http':'117.21.144.223'},
          {'http':'223.150.38.38'},{'http':'223.150.38.48'},{'http':'223.150.38.10'},{'http':'211.136.127.125'},
          {'http':'180.118.134.103'},{'http':'60.188.38.186'},{'http':'223.150.38.60'},{'http':'114.235.22.128'},
          {'http':'114.234.82.149'},{'http':'182.96.245.111'},{'http':'211.136.127.125'},{'http':'125.110.111.198'},
          {'http':'106.12.22.41'},{'http':'121.31.102.100'},{'http':'117.21.144.223'},{'http':'223.150.38.38'},
          {'http':'223.150.38.48'},{'http':'223.150.38.10'},{'http':'180.118.134.103'},{'http':'60.188.38.186'},
          {'http':'223.150.38.60'},{'http':'114.235.22.128'},{'http':'114.234.82.149'},{'http':'182.96.245.111'},
          {'http':'211.136.127.125'},{'http':'125.110.111.198'},{'http':'106.12.22.41'},{'http':'121.31.102.100'},
          {'http':'117.21.144.223'},{'http':'223.150.38.38'},{'http':'223.150.38.48'},{'http':'223.150.38.10'},
          {'http':'211.136.127.125'},{'http':'180.118.134.103'},{'http':'60.188.38.186'},{'http':'223.150.38.60'},
          {'http':'114.235.22.128'},{'http':'114.234.82.149'},{'http':'182.96.245.111'},{'http':'211.136.127.125'},
          {'http':'125.110.111.198'},{'http':'106.12.22.41'},{'http':'121.31.102.100'},{'http':'117.21.144.223'},
          {'http':'223.150.38.48'},{'http':'211.136.127.125'},{'http':'180.118.134.103'},{'http':'60.188.38.186'},
          {'http':'223.150.38.60'},{'http':'114.234.82.149'},{'http':'182.96.245.111'},{'http':'125.110.111.198'},
          {'http':'106.12.22.41'},{'http':'121.31.102.100'},{'http':'117.21.144.223'},{'http':'223.150.38.38'},
          {'http':'223.150.38.48'},{'http':'223.150.38.10'},{'http':'211.136.127.125'},{'http':'180.118.134.103'},
          {'http':'60.188.38.186'},{'http':'223.150.38.60'},{'http':'114.235.22.128'},{'http':'114.234.82.149'},
          {'http':'182.96.245.111'},{'http':'211.136.127.125'},{'http':'125.110.111.198'},{'http':'106.12.22.41'},
          {'http': '101.71.232.229'}, {'http': '47.93.3.242'}, {'http': '115.218.217.92'},
          {'http': '117.87.178.188'}, {'http': '115.218.127.67'}, {'http': '114.235.22.159'},
          {'http':'117.21.144.223'},{'http':'223.150.38.48'},{'http':'223.150.38.10'},
          {'http':'211.136.127.125'},{'http':'60.188.38.186'},{'http':'223.150.38.60'},{'http':'114.235.22.128'},
          {'http':'114.234.82.149'},{'http':'182.96.245.111'},{'http':'211.136.127.125'},
          {'http':'125.110.111.198'},{'http':'106.12.22.41'},{'http':'60.191.57.78'},
          {'http':'123.249.88.153'},{'http':'202.104.113.35'}]


# 和url一起组成博客地址
arts = ['82108238','81506230','81506104','81430853','81017392','80960239',
       '80889405','80816534','79038327','78826449','78811300','78493728',
	   '80770507','80984291','80924912','80816534','80664628','80663135',
	   '80610247','80530466','79989891','79878224','79690970','79552705','78801036','78740804','78598512','78493728','82469598','82884093','82893610','82873445','82871233','82870187','82868058','82828534','82722122','82718525','82469598']

# 伪造浏览器的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip',
    'Connection': 'close',
    # 防止防盗链
    'Referer': 'https://blog.csdn.net/'
    }
