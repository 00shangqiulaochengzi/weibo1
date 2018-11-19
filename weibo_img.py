import requests
import os
import re
from multiprocessing import Pool
# import threadpool

SAVE_PIC_PATH = 'D:\\chenyan\\weibo\\'

headers = {
    'Cookie': 'ALF=1544012648; SCF=Al8opCZ9OzF8FX89icJ6NHt3T-us9ftc4sAsuU33bjNWGWTXOAMrXBevhiOSRGnu1Nc1Lf5RMX7mkk4kWP3cSiA.; SUB=_2A2525Ed2DeRhGeNH7FoZ-CrOyDuIHXVSJ2k-rDV6PUJbktANLXKskW1NSmvuLoPRAjooQNqHGXQxFwF0NII94WGq; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFm3LGvgfcoGPSBZ_96oSPp5JpX5K-hUgL.Fo-4S0nR1hBEe0M2dJLoI0eLxKqL1-eL1h5LxKqLBKeL1KzLxKML1-2L1hBLxKML1-eL12zLxKqLBo-LBoUkSK-fSK-t; SUHB=0OMkTXZXuC7nEP; SSOLoginState=1541420838; _T_WM=af177b4e4413340af6a367ac16d9556a',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}


def start_requests(fuid):
    try:
        list = []
        for page_num in range(1, 50):
            base_url = 'https://weibo.cn/album/albummblog?fuid=%s&page=%d'%(fuid, page_num)
            response = requests.get(base_url, headers=headers)
            if response.status_code == 200:
                pattern = r'<img src="([\s\S]*?)"'
                p = re.compile(pattern)
                img_list = p.findall(response.text)
                for img_url in img_list:
                    if '.jpg' in img_url:
                        list.append(img_url.replace('wap180', 'large'))
                # pool_1 = threadpool.ThreadPool(4)
                # reqs = threadpool.makeRequests(download, list)
                # [pool_1.putRequest(req) for req in reqs]
                # pool_1.wait()
                download(list, fuid)
    except Exception as e:
        print(e)
        pass


def download(list, fuid):
    try:
        for i in list:
            if not os.path.exists(SAVE_PIC_PATH + fuid):
                os.mkdir(SAVE_PIC_PATH + fuid)
            response = requests.get(i, headers=headers)
            img_json = {}
            img_json['website'] = 'weibo'
            img_json['img_url'] = response.url
            if not os.path.exists(SAVE_PIC_PATH + fuid + '\\' + i.split('/')[-1]):
                with open(SAVE_PIC_PATH + fuid + '\\' + i.split('/')[-1], 'wb') as f:
                    f.write(response.content)
                    print('图片下载完成')
                # with open(SAVE_PIC_PATH + fuid + '\\' + i.split('/')[-1].replace('.jpg', '.json'), 'w') as f:
                #     f.write(str(img_json))
    except Exception as e:
        print(e)
        pass


if __name__ == '__main__':
    fuids = ['1259110474', '1223178222', '1195242865', '1730726637', '1574684061', '3261134763']
    pool = Pool(4)
    for fuid in fuids:
        pool.apply_async(start_requests, (fuid,))
    pool.close()
    pool.join()
