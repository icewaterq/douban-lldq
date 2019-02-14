import requests
import re
import time


headers = {
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
 'Cookie':'自行填入',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Connection': 'keep-alive',
}






for i in range(47):
    time.sleep(1)
    url='https://movie.douban.com/subject/26266893/reviews?rating=1&start={}'.format(i*20)
    res = requests.get(url, headers=headers)
    p = re.compile('https://www.douban.com/people/\w*/\" class=\"name\"')
    results = re.findall(p, res.text)
    for r in results:
        time.sleep(0.5)
        url = r.replace('" class="name"', '')
        res = requests.get(url, headers=headers)
        p = re.compile('\d{4}-\d{2}-\d{2}加入')
        result = re.findall(p, res.text)
        try:
            print(result[0],url)
        except:
            print(url)