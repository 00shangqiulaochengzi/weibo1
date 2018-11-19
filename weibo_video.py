import requests
import re

headers = {
    'Cookie': 'SINAGLOBAL=6165320515095.216.1541073564226; wb_view_log=1536*8641.25; un=15038147230; wvr=6; wb_view_log_5978884237=1536*8641.25; YF-Page-G0=1ffbef18656bf02c17e45a764e3d5336; ALF=1572618485; SSOLoginState=1541082486; SCF=Al8opCZ9OzF8FX89icJ6NHt3T-us9ftc4sAsuU33bjNWfVeBZiR-bBY0IQEytv_kxms0TrpCwnhV1up8_Or1BmU.; SUB=_2A252330mDeRhGeNH7FoZ-CrOyDuIHXVVrenurDV8PUNbmtBeLXL4kW9NSmvuLpmmWBLT5dX6Y3U2vJDxOK3W4MUG; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFm3LGvgfcoGPSBZ_96oSPp5JpX5KzhUgL.Fo-4S0nR1hBEe0M2dJLoI0eLxKqL1-eL1h5LxKqLBKeL1KzLxKML1-2L1hBLxKML1-eL12zLxKqLBo-LBoUkSK-fSK-t; SUHB=0vJIC8NwvNyKHO; _s_tentry=login.sina.com.cn; Apache=5298096988241.095.1541082486431; ULV=1541082486501:2:2:2:5298096988241.095.1541082486431:1541073564235; YF-V5-G0=bb389e7e25cccb1fadd4b1334ab013c1; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

def get_index_url():
    url = 'https://weibo.com/p/1006051259110474/photos?type=video'
    response = requests.get(url, headers=headers)
    pattern = r'<a target=\\"_blank\\" href=\\"([\s\S]*?)"'
    p = re.compile(pattern)
    res = p.findall(response.text)
    res = list(set(res[1:]))
    return res

def get_video(res):
    parse_url = 'https://www.weibovideo.com/controller.php'
    if 'miaopai' in res:
        print(''.join(res.split('\\')))
        # response = requests.get(''.join(res.split('\\')), headers=headers)
        # print(response.text)
        # pattern = r'video-sources="fluency=([\s\S]*?)&'
        # p = re.compile(pattern)
        # res = p.findall(response.text)
        # print(res)
    elif 'video' in res:
        url = 'https://weibo.com/tv/v/jwmwTdGQD?' + res.split('?')[-1][:-1]
        print(url)
        finally_url = requests.post(url, headers=headers)
        print(finally_url.text)

if __name__ == "__main__":
    for res in get_index_url():
        get_video(res)

