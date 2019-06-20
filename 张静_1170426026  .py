import urllib.request
headers = {'Cookie':'ft=1; BAIDUID=7FB0EBF5FCC18B54678A364DD0841825:FG=1; s_ht_pageid=15; v_pg=normal; hz=0; Hm_lvt_0703cfc0023d60b244e06b5cacfef877=1560991129,1560991145,1561014315; Hm_lpvt_0703cfc0023d60b244e06b5cacfef877=1561014315; hword=20; tnwhiteft=XzFYUBclcWbsP1DYrHn3gv99Udqsuzc_cMw1cWCkPHmknjDYn10zxf; BAIDU_SSP_lcr=http://123.aaaabh.com/; __bsi=7667202040715637345_00_23_R_R_5_0303_c02f_Y'}
url = 'http://www.hao123.com/get'
proxy_handle=[{'http':'http://183.51.190.51:33913'},{'http':'http://119.191.79.46:80'}]
for i in range(2):
    proxy_ = random.sample(proxy_handle,1)
    proxy = urllib.request.ProxyHandler(proxy_)
    opener = urllib.request.build_opener(proxy)
    response = opener.open(url)
    print(urllib.request.getproxies())
    if response.status != 200:
        proxy_ = random.sample(proxy_handle,1)
    elif len(proxy_)=len(proxy_handle):
    print('爬取失败')







