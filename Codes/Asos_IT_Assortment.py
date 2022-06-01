import pandas as pd
import numpy as np
import requests
import json
import re
from datetime import datetime
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
from lxml import html
import os
import random

proxy_ips = [ "154.13.198.116","154.13.198.131","154.13.198.134","154.13.198.136","154.13.198.137","154.13.198.138","154.13.198.151","154.13.198.155","154.13.198.166","154.13.198.174","154.13.198.180","154.13.198.192","154.13.198.205","154.13.198.206","154.13.198.207","154.13.198.216","154.13.198.223","154.13.198.226","154.13.198.236","154.13.198.239","154.13.198.243","154.13.198.251","154.13.198.252","154.13.198.28","154.13.198.40","154.13.198.43","154.13.198.51","154.13.198.66","154.13.198.75","154.13.198.86","154.13.198.91","154.13.198.95","154.13.199.124","154.13.199.126","154.13.199.127","154.13.199.128","154.13.199.129","154.13.199.144","154.13.199.147","154.13.199.158","154.13.199.163","154.13.199.168","154.13.199.171","154.13.199.180","154.13.199.183","154.13.199.189","154.13.199.192","154.13.199.218","154.13.199.219","154.13.199.223","154.13.199.232","154.13.199.250","154.13.199.251","154.13.199.29","154.13.199.3","154.13.199.38","154.13.199.59","154.13.199.61","154.13.199.64","154.13.199.69","154.13.199.83","154.13.199.84","154.13.199.86","154.13.199.96","154.13.204.100","154.13.204.109","154.13.204.115","154.13.204.116","154.13.204.119","154.13.204.121","154.13.204.131","154.13.204.138","154.13.204.145","154.13.204.155","154.13.204.169","154.13.204.184","154.13.204.192","154.13.204.196","154.13.204.199","154.13.204.210","154.13.204.214","154.13.204.217","154.13.204.223","154.13.204.239","154.13.204.249","154.13.204.27","154.13.204.33","154.13.204.35","154.13.204.5","154.13.204.52","154.13.204.55","154.13.204.64","154.13.204.70","154.13.204.77","154.13.204.78","154.13.204.87","154.13.248.108","154.13.248.11","154.13.248.111","154.13.248.114","154.13.248.117","154.13.248.119","154.13.248.122","154.13.248.147","154.13.248.148","154.13.248.152","154.13.248.159","154.13.248.166","154.13.248.176","154.13.248.178","154.13.248.183","154.13.248.184","154.13.248.198","154.13.248.206","154.13.248.21","154.13.248.211","154.13.248.222","154.13.248.228","154.13.248.229","154.13.248.233","154.13.248.246","154.13.248.248","154.13.248.25","154.13.248.4","154.13.248.62","154.13.248.66","154.13.248.88","154.13.248.92","154.28.67.10","154.28.67.100","154.28.67.102","154.28.67.11","154.28.67.128","154.28.67.140","154.28.67.149","154.28.67.158","154.28.67.160","154.28.67.164","154.28.67.177","154.28.67.181","154.28.67.205","154.28.67.206","154.28.67.209","154.28.67.213","154.28.67.220","154.28.67.225","154.28.67.227","154.28.67.230","154.28.67.232","154.28.67.239","154.28.67.248","154.28.67.27","154.28.67.36","154.28.67.6","154.28.67.65","154.28.67.68","154.28.67.71","154.28.67.85","154.28.67.95","154.28.67.97","154.7.230.10","154.7.230.119","154.7.230.133","154.7.230.136","154.7.230.144","154.7.230.148","154.7.230.162","154.7.230.165","154.7.230.166","154.7.230.173","154.7.230.176","154.7.230.177","154.7.230.195","154.7.230.20","154.7.230.201","154.7.230.202","154.7.230.221","154.7.230.222","154.7.230.224","154.7.230.226","154.7.230.227","154.7.230.237","154.7.230.247","154.7.230.251","154.7.230.254","154.7.230.30","154.7.230.43","154.7.230.44","154.7.230.59","154.7.230.62","154.7.230.7","154.7.230.72","173.208.27.101","173.208.27.103","173.208.27.107","173.208.27.111","173.208.27.112","173.208.27.114","173.208.27.116","173.208.27.117","173.208.27.119","173.208.27.120","173.208.27.134","173.208.27.135","173.208.27.144","173.208.27.15","173.208.27.155","173.208.27.158","173.208.27.162","173.208.27.164","173.208.27.171","173.208.27.208","173.208.27.214","173.208.27.226","173.208.27.236","173.208.27.250","173.208.27.38","173.208.27.39","173.208.27.50","173.208.27.54","173.208.27.6","173.208.27.79","173.208.27.85","173.208.27.95","23.131.8.133","23.131.8.136","23.131.8.137","23.131.8.139","23.131.8.141","23.131.8.145","23.131.8.151","23.131.8.162","23.131.8.183","23.131.8.188","23.131.8.201","23.131.8.206","23.131.8.208","23.131.8.211","23.131.8.230","23.131.8.248","23.131.8.25","23.131.8.250","23.131.8.251","23.131.8.252","23.131.8.29","23.131.8.30","23.131.8.40","23.131.8.43","23.131.8.48","23.131.8.53","23.131.8.56","23.131.8.70","23.131.8.78","23.131.8.80","23.131.8.81","23.131.8.91","23.131.88.10","23.131.88.100","23.131.88.103","23.131.88.106","23.131.88.107","23.131.88.110","23.131.88.112","23.131.88.121","23.131.88.126","23.131.88.144","23.131.88.149","23.131.88.158","23.131.88.159","23.131.88.16","23.131.88.17","23.131.88.184","23.131.88.188","23.131.88.189","23.131.88.199","23.131.88.203","23.131.88.204","23.131.88.205","23.131.88.218","23.131.88.239","23.131.88.245","23.131.88.251","23.131.88.254","23.131.88.3","23.131.88.33","23.131.88.38","23.131.88.46","23.131.88.48","23.131.88.56","23.230.177.102","23.230.177.104","23.230.177.114","23.230.177.131","23.230.177.132","23.230.177.141","23.230.177.149","23.230.177.162","23.230.177.170","23.230.177.180","23.230.177.186","23.230.177.198","23.230.177.210","23.230.177.218","23.230.177.22","23.230.177.226","23.230.177.227","23.230.177.232","23.230.177.234","23.230.177.239","23.230.177.253","23.230.177.33","23.230.177.37","23.230.177.42","23.230.177.47","23.230.177.48","23.230.177.63","23.230.177.70","23.230.177.76","23.230.177.87","23.230.177.89","23.230.177.97","23.230.197.10","23.230.197.108","23.230.197.114","23.230.197.142","23.230.197.145","23.230.197.160","23.230.197.170","23.230.197.176","23.230.197.180","23.230.197.189","23.230.197.214","23.230.197.217","23.230.197.248","23.230.197.252","23.230.197.253","23.230.197.27","23.230.197.28","23.230.197.29","23.230.197.36","23.230.197.39","23.230.197.40","23.230.197.41","23.230.197.42","23.230.197.44","23.230.197.5","23.230.197.59","23.230.197.73","23.230.197.76","23.230.197.83","23.230.197.86","23.230.197.96","23.230.197.98","23.230.74.119","23.230.74.124","23.230.74.140","23.230.74.143","23.230.74.165","23.230.74.169","23.230.74.176","23.230.74.177","23.230.74.181","23.230.74.182","23.230.74.184","23.230.74.190","23.230.74.196","23.230.74.20","23.230.74.21","23.230.74.213","23.230.74.214","23.230.74.220","23.230.74.224","23.230.74.229","23.230.74.239","23.230.74.247","23.230.74.26","23.230.74.36","23.230.74.42","23.230.74.54","23.230.74.61","23.230.74.68","23.230.74.69","23.230.74.70","23.230.74.83","23.230.74.89","23.230.74.93","23.247.172.106","23.247.172.118","23.247.172.131","23.247.172.135","23.247.172.142","23.247.172.155","23.247.172.157","23.247.172.163","23.247.172.171","23.247.172.186","23.247.172.205","23.247.172.209","23.247.172.212","23.247.172.215","23.247.172.218","23.247.172.22","23.247.172.220","23.247.172.223","23.247.172.249","23.247.172.32","23.247.172.38","23.247.172.45","23.247.172.47","23.247.172.48","23.247.172.50","23.247.172.54","23.247.172.76","23.247.172.77","23.247.172.78","23.247.172.86","23.247.172.9","23.247.172.98","23.27.222.105","23.27.222.117","23.27.222.120","23.27.222.135","23.27.222.141","23.27.222.151","23.27.222.152","23.27.222.153","23.27.222.167","23.27.222.17","23.27.222.182","23.27.222.183","23.27.222.184","23.27.222.187","23.27.222.190","23.27.222.193","23.27.222.194","23.27.222.209","23.27.222.224","23.27.222.229","23.27.222.230","23.27.222.232","23.27.222.239","23.27.222.245","23.27.222.249","23.27.222.48","23.27.222.50","23.27.222.51","23.27.222.55","23.27.222.64","23.27.222.76","23.27.222.95","38.131.131.104","38.131.131.108","38.131.131.116","38.131.131.120","38.131.131.121","38.131.131.122","38.131.131.124","38.131.131.155","38.131.131.168","38.131.131.186","38.131.131.187","38.131.131.188","38.131.131.194","38.131.131.197","38.131.131.201","38.131.131.203","38.131.131.21","38.131.131.210","38.131.131.214","38.131.131.215","38.131.131.219","38.131.131.231","38.131.131.253","38.131.131.28","38.131.131.34","38.131.131.52","38.131.131.55","38.131.131.62","38.131.131.66","38.131.131.72","38.131.131.79","38.131.131.98","38.96.156.109","38.96.156.110","38.96.156.117","38.96.156.118","38.96.156.129","38.96.156.140","38.96.156.144","38.96.156.146","38.96.156.171","38.96.156.173","38.96.156.177","38.96.156.183","38.96.156.189","38.96.156.193","38.96.156.198","38.96.156.207","38.96.156.21","38.96.156.219","38.96.156.221","38.96.156.222","38.96.156.225","38.96.156.23","38.96.156.247","38.96.156.248","38.96.156.38","38.96.156.41","38.96.156.46","38.96.156.47","38.96.156.58","38.96.156.59","38.96.156.76","38.96.156.91","38.96.156.95","38.96.157.104","38.96.157.132","38.96.157.152","38.96.157.164","38.96.157.176","38.96.157.177","38.96.157.179","38.96.157.185","38.96.157.196","38.96.157.197","38.96.157.202","38.96.157.217","38.96.157.218","38.96.157.219","38.96.157.241","38.96.157.244","38.96.157.253","38.96.157.27","38.96.157.28","38.96.157.3","38.96.157.40","38.96.157.41","38.96.157.47","38.96.157.54","38.96.157.59","38.96.157.60","38.96.157.66","38.96.157.70","38.96.157.73","38.96.157.80","38.96.157.81","38.96.157.87","45.238.157.103","45.238.157.105","45.238.157.114","45.238.157.115","45.238.157.117","45.238.157.131","45.238.157.147","45.238.157.148","45.238.157.154","45.238.157.157","45.238.157.167","45.238.157.168","45.238.157.171","45.238.157.174","45.238.157.177","45.238.157.184","45.238.157.190","45.238.157.195","45.238.157.202","45.238.157.210","45.238.157.216","45.238.157.229","45.238.157.231","45.238.157.241","45.238.157.248","45.238.157.250","45.238.157.26","45.238.157.29","45.238.157.31","45.238.157.41","45.238.157.71","45.238.157.78","45.238.159.111","45.238.159.112","45.238.159.117","45.238.159.155","45.238.159.161","45.238.159.164","45.238.159.173","45.238.159.176","45.238.159.177","45.238.159.181","45.238.159.195","45.238.159.198","45.238.159.211","45.238.159.222","45.238.159.224","45.238.159.226","45.238.159.227","45.238.159.234","45.238.159.241","45.238.159.244","45.238.159.245","45.238.159.25","45.238.159.33","45.238.159.40","45.238.159.42","45.238.159.50","45.238.159.54","45.238.159.70","45.238.159.81","45.238.159.84","45.238.159.95","45.238.159.98","66.207.180.108","66.207.180.110","66.207.180.12","66.207.180.148","66.207.180.153","66.207.180.155","66.207.180.163","66.207.180.170","66.207.180.18","66.207.180.180","66.207.180.183","66.207.180.192","66.207.180.196","66.207.180.2","66.207.180.200","66.207.180.214","66.207.180.218","66.207.180.227","66.207.180.23","66.207.180.241","66.207.180.246","66.207.180.36","66.207.180.38","66.207.180.50","66.207.180.55","66.207.180.56","66.207.180.58","66.207.180.7","66.207.180.72","66.207.180.78","66.207.180.89","66.207.180.9","104.156.136.205","104.156.136.70","104.156.136.98","104.156.137.157","104.156.137.170","104.156.137.41","104.156.138.221","104.156.138.59","104.156.138.62","104.156.139.215","104.156.139.250","104.156.139.79","104.251.84.52","104.251.84.91","104.251.85.108","104.251.85.170","104.251.91.170","104.251.91.87","104.251.92.124","104.251.92.163","108.177.131.107","108.177.131.12","108.177.131.235","146.19.55.137","146.19.55.55","154.13.198.2","154.13.198.229","154.13.198.57","154.13.199.217","154.13.199.36","154.13.199.92","154.13.204.146","154.13.204.203","154.13.204.22","154.13.205.144","154.13.205.23","154.13.206.129","154.13.206.130","154.13.206.16","154.13.207.225","154.13.207.87","154.13.244.122","154.13.244.188","154.13.244.96","154.13.245.221","154.13.245.69","154.13.246.141","154.13.246.208","154.13.246.232","154.13.247.107","154.13.247.217","154.13.247.99","154.13.248.201","154.13.248.46","154.13.248.91","154.13.249.179","154.13.249.56","154.13.249.64","154.13.250.112","154.13.250.253","154.13.250.95","154.13.251.188","154.13.251.225","154.13.251.240","154.13.252.229","154.13.252.24","154.13.252.43","154.13.253.171","154.13.253.81","154.13.254.226","154.13.254.50","154.13.254.63","154.13.255.38","154.13.255.42","154.13.255.52","154.17.189.203","154.17.189.90","154.28.67.216","154.28.67.3","154.37.72.106","154.37.72.163","154.37.72.187","154.37.76.106","154.37.76.179","154.37.76.58","154.7.230.146","154.7.230.32","154.7.230.57","158.115.248.141","158.115.248.249","158.115.249.216","158.115.249.33","168.91.64.151","168.91.64.75","168.91.65.142","168.91.65.3","168.91.65.83","168.91.66.131","168.91.66.196","168.91.66.199","168.91.67.34","168.91.67.96","168.91.76.103","168.91.76.91","168.91.77.193","168.91.77.61","168.91.78.13","168.91.78.139","168.91.79.34","168.91.79.48","168.91.79.93","168.91.84.125","168.91.84.152","168.91.84.233","168.91.85.25","168.91.85.42","168.91.86.106","168.91.86.64","168.91.86.79","168.91.87.167","168.91.87.47","168.91.87.50","172.110.146.19","172.110.146.235","172.110.146.56","172.110.147.154","172.110.147.174","172.110.147.48","172.255.93.207","172.255.93.23","172.255.94.165","172.255.94.185","172.81.20.167","172.81.20.233","172.81.20.45","172.81.21.186","172.81.21.69","172.81.21.76","172.81.22.182","172.81.22.45","172.81.22.92","172.81.23.166","172.81.23.241","172.81.23.33","173.208.27.52","173.208.27.86","173.208.28.58","173.208.28.75","173.245.75.131","173.245.75.159","173.245.75.215","173.245.85.189","173.245.85.202","173.245.85.250","173.245.90.236","173.245.90.6","204.217.164.148","204.217.164.15"]



headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

assortment_df = pd.read_excel(r'Assortment Input.xlsx')

Asos_Assortment = pd.DataFrame()

def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

for urls in range(len(assortment_df)):
    for ij in range(10):
        try:
            urls_list = []
            c = 1
            usern_passw = str("csimonra:h19VA2xZ")
            rand_ips = random.choice(proxy_ips)
            port = "29842"

            proxy = {
                'https': "http://{}@{}:{}/".format(usern_passw, rand_ips, port),
                'http': "https://{}@{}:{}/".format(usern_passw, rand_ips, port),
            }
            response = requests.get(url = assortment_df['Category URL'][urls], headers = headers, timeout = 30, proxies = proxy)
            if response.status_code==200:
                break
        except Exception as e:
            print('retrying....')
    if response.status_code==200:
        tree = html.fromstring(response.text)

        product_Url = tree.xpath('//section[@class="_3YREj-P"]/article/a/@href')

        while len(product_Url) > 0:
            if response.url not in urls_list:
                urls_list.append(response.url)
                print(response.url)

                #RPC
                sku_list = []

                for w in product_Url:
                    RPC = re.findall(r'prd/(.*?)\?', w)
                    RPC = listToString(RPC)
                    sku_list.append('asos_it_' + RPC)

                #PageID
                page_id = assortment_df['Category_ID'][urls] + "_" + str(c)

                # time
                now = datetime.now()
                date_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")

                datazone = datetime.now()
                f_date = datazone.strftime("%d_%m_%Y")
                strdate = datazone.day
                strm = datazone.month
                stry = datazone.year
                cpid = page_id + '_' + str(strdate) + '_' + str(strm) + '_' + str(stry)
                ASS_folder = f"\\\\ecxus440\\E$\\ADIDAS_SavePages\\Asos_it\\Assortment"
                sos_date_wise_folder = ASS_folder + f"\\{f_date}"
                if os.path.exists(sos_date_wise_folder):
                    pass
                else:
                    os.mkdir(sos_date_wise_folder)
                sos_filename = sos_date_wise_folder + "\\" + cpid + ".html"
                sos_filename = sos_filename.replace("+", "_")

                page_path = sos_filename.replace('/', '')
                print(page_path)
                page_path = page_path.replace('\\\\ecxus440\\E$\\ADIDAS_SavePages\\',
                                              'https:////ecxus440.eclerx.com//cachepages//').replace('\\',
                                                                                                     '//').replace(
                    '//', '/')
                print(page_path)

                if os.path.exists(sos_filename):
                    with open(sos_filename, 'w', encoding='utf-8-sig') as f:
                        f.write(response.text)
                else:
                    with open(sos_filename, 'w', encoding='utf-8-sig') as f:
                        f.write(response.text)
                        f.close()

                for siz in range(len(product_Url)):
                    Asos_Assortment = Asos_Assortment.append({'Website': 'www.asos.com/it', 'Country': 'IT',
                                                            'Category ID': assortment_df['Category_ID'][urls],
                                                            'Page ID': page_id, 'Category URL': response.url,
                                                            'SKU_ID': sku_list[siz], 'PDP URL': product_Url[siz],
                                                            'Date_&_TimeStamp': date_time, 'Cache Page': page_path},
                                                            ignore_index = True)
                    #Asos_Assortment.to_csv('Asos_IT_Assortment_2503.csv', index=False, encoding='utf-8-sig',mode="a+")

                c += 1
                url1 = assortment_df['Category URL'][urls] + '&page=' + str(c)
                for jk in range(10):
                    try:
                        usern_passw = str("csimonra:h19VA2xZ")
                        rand_ips = random.choice(proxy_ips)
                        port = "29842"
                        proxy = {
                            'https': "http://{}@{}:{}/".format(usern_passw, rand_ips, port),
                            'http': "https://{}@{}:{}/".format(usern_passw, rand_ips, port),
                        }
                        response = requests.get(url = url1, headers = headers, proxies = proxy, timeout = 30)
                        if response.status_code==200:
                            break

                    except Exception as e:
                        print('retrying for next page url......')
                tree = html.fromstring(response.text)
                product_Url = tree.xpath('//section[@class="_3YREj-P"]/article/a/@href')

            else:
                product_Url = []

Asos_Assortment.to_csv('Asos_IT_Assortment_2503.csv', index = False, encoding = 'utf-8-sig')