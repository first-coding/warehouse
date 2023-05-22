import requests
from lxml import etree
from bs4 import BeautifulSoup
from urllib import request
import re
import os
import shutil
import time

def get_data(mid,pn):
    url = "https://api.bilibili.com/x/space/wbi/arc/search"
    params = {
        "mid":mid,
        "ps":30,
        'tid':0,
        'pn':pn,
        'keyword':'',
        'order':'pubdate',
        'platform':'web',
        'web_location':1550101,
        'order_avoided':'true',
        'w_rid':'f203883eccab0389d78a1edc6d5181e0',
        'wts':'1682922868'
    }
    header = {
        "cookie":"buvid3=9EF91E31-4B3D-4A30-FE7D-5D76BE03D9E327371infoc; b_nut=1674285927; _uuid=21B42DFA-31FE-87E1-9512-12F95299A75A27643infoc; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=|(k|k)Y)mJ)R0J'uY~Rk)Y|YJ; i-wanna-go-back=-1; b_ut=5; hit-new-style-dyn=0; hit-dyn-v2=1; header_theme_version=CLOSE; home_feed_column=5; CURRENT_QUALITY=112; buvid4=CEEADE42-25AF-AECE-D530-764A770777A828760-023012115-c8mC4VtaIp%2BYz8JESbGfsg%3D%3D; buvid_fp_plain=undefined; LIVE_BUVID=AUTO4016792195519835; CURRENT_PID=4c13d250-c91f-11ed-9c02-8d69ae93ec42; FEED_LIVE_VERSION=V8; bp_video_offset_283470100=785058960366370800; browser_resolution=1536-714; SESSDATA=9cf06065%2C1698421018%2C52d13%2A41; bili_jct=c04ea463fb03630f415490e24915af55; DedeUserID=96917526; DedeUserID__ckMd5=9976e0758470471c; sid=502a3o2f; bsource=search_bing; bp_video_offset_96917526=790567333275893800; fingerprint=bdb93d286701b889041fa2e6415f8d80; buvid_fp=bdb93d286701b889041fa2e6415f8d80; PVID=2; innersign=1; b_lsid=46FFA10D8_187D5E38BD0",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    }
    data = requests.get(url=url,headers=header,params=params).json()
    return data

def dowload(data):
    for i in data['data']['list']['vlist']:
        url = "https://www.bilibili.com/video/"+i['bvid']+"/?spm_id_from=333.999.0.0&vd_source=1044410fba936cd01d24526cd1edef1a"
        print(url)

def get_page(mid):
    page_url = "https://api.bilibili.com/x/space/navnum?mid="+mid
    header = {
        "cookie":"buvid3=9EF91E31-4B3D-4A30-FE7D-5D76BE03D9E327371infoc; b_nut=1674285927; _uuid=21B42DFA-31FE-87E1-9512-12F95299A75A27643infoc; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=|(k|k)Y)mJ)R0J'uY~Rk)Y|YJ; i-wanna-go-back=-1; b_ut=5; hit-new-style-dyn=0; hit-dyn-v2=1; header_theme_version=CLOSE; home_feed_column=5; CURRENT_QUALITY=112; buvid4=CEEADE42-25AF-AECE-D530-764A770777A828760-023012115-c8mC4VtaIp%2BYz8JESbGfsg%3D%3D; buvid_fp_plain=undefined; LIVE_BUVID=AUTO4016792195519835; CURRENT_PID=4c13d250-c91f-11ed-9c02-8d69ae93ec42; FEED_LIVE_VERSION=V8; bp_video_offset_283470100=785058960366370800; browser_resolution=1536-714; SESSDATA=9cf06065%2C1698421018%2C52d13%2A41; bili_jct=c04ea463fb03630f415490e24915af55; DedeUserID=96917526; DedeUserID__ckMd5=9976e0758470471c; sid=502a3o2f; bsource=search_bing; bp_video_offset_96917526=790567333275893800; fingerprint=bdb93d286701b889041fa2e6415f8d80; buvid_fp=bdb93d286701b889041fa2e6415f8d80; PVID=2; innersign=1; b_lsid=46FFA10D8_187D5E38BD0",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    }
    response = requests.get(url=page_url,headers=header).json()
    if response['data']['video']%30!=0:
        return int(response['data']['video']/30)+1
    else:
        return int(response['data']['video']/30)

def type_of_video(url):
    header = {
        "cookie":"buvid3=9EF91E31-4B3D-4A30-FE7D-5D76BE03D9E327371infoc; b_nut=1674285927; _uuid=21B42DFA-31FE-87E1-9512-12F95299A75A27643infoc; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=|(k|k)Y)mJ)R0J'uY~Rk)Y|YJ; i-wanna-go-back=-1; b_ut=5; hit-new-style-dyn=0; hit-dyn-v2=1; header_theme_version=CLOSE; home_feed_column=5; CURRENT_QUALITY=112; buvid4=CEEADE42-25AF-AECE-D530-764A770777A828760-023012115-c8mC4VtaIp%2BYz8JESbGfsg%3D%3D; buvid_fp_plain=undefined; LIVE_BUVID=AUTO4016792195519835; CURRENT_PID=4c13d250-c91f-11ed-9c02-8d69ae93ec42; FEED_LIVE_VERSION=V8; bp_video_offset_283470100=785058960366370800; browser_resolution=1536-714; DedeUserID=96917526; DedeUserID__ckMd5=9976e0758470471c; fingerprint=bdb93d286701b889041fa2e6415f8d80; buvid_fp=bdb93d286701b889041fa2e6415f8d80; PVID=3; SESSDATA=6de1a57a%2C1698507704%2C5c306%2A51; bili_jct=18644e645f19b5f5bd022e52097922a6; sid=5mgkji03; b_lsid=91066C910B_187DA94F939; bp_video_offset_96917526=790810359708516400",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    }
    response = requests.get(url, headers=header)
    type = BeautifulSoup(response.text, 'lxml').find(attrs={'property': 'og:type'})['content']
    if 'movie' in type:
        return 'movie'
    elif 'anime' in type:
        return 'anime'
    elif 'documentary' in type:
        return 'documentary'
    elif 'tv' in type:
        return 'tv'
    else:
        return 'video'
    
def get_all_url(url, type):
    header = {
        "cookie":"buvid3=9EF91E31-4B3D-4A30-FE7D-5D76BE03D9E327371infoc; b_nut=1674285927; _uuid=21B42DFA-31FE-87E1-9512-12F95299A75A27643infoc; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=|(k|k)Y)mJ)R0J'uY~Rk)Y|YJ; i-wanna-go-back=-1; b_ut=5; hit-new-style-dyn=0; hit-dyn-v2=1; header_theme_version=CLOSE; home_feed_column=5; CURRENT_QUALITY=112; buvid4=CEEADE42-25AF-AECE-D530-764A770777A828760-023012115-c8mC4VtaIp%2BYz8JESbGfsg%3D%3D; buvid_fp_plain=undefined; LIVE_BUVID=AUTO4016792195519835; CURRENT_PID=4c13d250-c91f-11ed-9c02-8d69ae93ec42; FEED_LIVE_VERSION=V8; bp_video_offset_283470100=785058960366370800; browser_resolution=1536-714; DedeUserID=96917526; DedeUserID__ckMd5=9976e0758470471c; fingerprint=bdb93d286701b889041fa2e6415f8d80; buvid_fp=bdb93d286701b889041fa2e6415f8d80; PVID=3; SESSDATA=6de1a57a%2C1698507704%2C5c306%2A51; bili_jct=18644e645f19b5f5bd022e52097922a6; sid=5mgkji03; b_lsid=91066C910B_187DA94F939; bp_video_offset_96917526=790810359708516400",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    }
    if type == 'anime' or type == 'tv' or type == 'documentary':
        response = requests.get(url, headers=header)
        text = response.text
        pattern1 = 'upInfo.*</html>'
        pattern2 = '"share_url":"(http.*?)"'
        a = re.sub(pattern1, '', text)
        result = re.findall(pattern2, a)
        return result
    else:
        return url
    

def get_downloadurl(url, type):  # 获取视频和音频的下载地址
    header = {
        "cookie":"buvid3=9EF91E31-4B3D-4A30-FE7D-5D76BE03D9E327371infoc; b_nut=1674285927; _uuid=21B42DFA-31FE-87E1-9512-12F95299A75A27643infoc; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=|(k|k)Y)mJ)R0J'uY~Rk)Y|YJ; i-wanna-go-back=-1; b_ut=5; hit-new-style-dyn=0; hit-dyn-v2=1; header_theme_version=CLOSE; home_feed_column=5; CURRENT_QUALITY=112; buvid4=CEEADE42-25AF-AECE-D530-764A770777A828760-023012115-c8mC4VtaIp%2BYz8JESbGfsg%3D%3D; buvid_fp_plain=undefined; LIVE_BUVID=AUTO4016792195519835; CURRENT_PID=4c13d250-c91f-11ed-9c02-8d69ae93ec42; FEED_LIVE_VERSION=V8; bp_video_offset_283470100=785058960366370800; browser_resolution=1536-714; DedeUserID=96917526; DedeUserID__ckMd5=9976e0758470471c; fingerprint=bdb93d286701b889041fa2e6415f8d80; buvid_fp=bdb93d286701b889041fa2e6415f8d80; PVID=3; SESSDATA=6de1a57a%2C1698507704%2C5c306%2A51; bili_jct=18644e645f19b5f5bd022e52097922a6; sid=5mgkji03; b_lsid=91066C910B_187DA94F939; bp_video_offset_96917526=790810359708516400",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    }
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            text = response.text
            title_of_series = BeautifulSoup(text, 'lxml').find(attrs={'property': 'og:title'})['content']
            if type == 'movie' or type == 'video':
                title_of_series = 'Bilibili下载视频'
                pattern_title = '.__INITIAL_STATE__.*?[tT]itle.*?:"(.*?)"'
            else:
                pattern_title = '._ __.*?[tT]itle.*?:"' + title_of_series + '.*?：(.*?)"'
            pattern_video = '"video":.+?"baseUrl".*?"(https://.*?.m4s.*?)"'
            pattern_audio = '"audio":.+?"baseUrl".*?"(https://.*?.m4s.*?)"'
            url_video = re.search(pattern_video, text)[1]
            url_audio = re.search(pattern_audio, text)[1]
            title = re.search(pattern_title, text)[1]
            urls = {
                'video': url_video,
                'audio': url_audio,
                'title': title,
                'title_of_series': title_of_series
            }
            return urls
    except ConnectionError as e:
        print(e.args)
        print('获取视频和音频的下载地址失败')
        return None
    except:
        return None
    
def merge(title, output,counts):
    cmd = 'ffmpeg -i ./download/"' + title + '.mp3" -i ./download/"' + title + '.mp4" \
    -acodec copy -vcodec copy F:/' + output + '/' + str(counts) + '/"' + title + '.mp4"'
    os.system(cmd)


def down_video(urls,counts):
    headers = {
        'referer': "https://space.bilibili.com/7801559/video?tid=0&pn="+str(counts)+"&keyword=&order=pubdate",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        'range': 'bytes=0-1000000000000',
        'cookie':"buvid3=9EF91E31-4B3D-4A30-FE7D-5D76BE03D9E327371infoc; b_nut=1674285927; _uuid=21B42DFA-31FE-87E1-9512-12F95299A75A27643infoc; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=|(k|k)Y)mJ)R0J'uY~Rk)Y|YJ; i-wanna-go-back=-1; b_ut=5; hit-new-style-dyn=0; hit-dyn-v2=1; header_theme_version=CLOSE; home_feed_column=5; CURRENT_QUALITY=112; buvid4=CEEADE42-25AF-AECE-D530-764A770777A828760-023012115-c8mC4VtaIp%2BYz8JESbGfsg%3D%3D; buvid_fp_plain=undefined; LIVE_BUVID=AUTO4016792195519835; CURRENT_PID=4c13d250-c91f-11ed-9c02-8d69ae93ec42; FEED_LIVE_VERSION=V8; bp_video_offset_283470100=785058960366370800; browser_resolution=1536-714; DedeUserID=96917526; DedeUserID__ckMd5=9976e0758470471c; fingerprint=bdb93d286701b889041fa2e6415f8d80; buvid_fp=bdb93d286701b889041fa2e6415f8d80; PVID=3; bp_video_offset_96917526=790810359708516400; b_lsid=D9963BE9_187E55350AB; SESSDATA=20d2c567%2C1698731667%2Cbb56e%2A51; bili_jct=a08ff212b6eb0c85a9634e84c122aff7; sid=6gwglu4x"
    }
    print(headers['referer'])
    if not os.path.exists('./download'):
        os.mkdir('./download')  # 创建临时文件夹以便存放音频，视频
    if not os.path.exists(urls['title_of_series']):
        os.mkdir(urls['title_of_series'])
    try:
        video = requests.get(urls['video'], headers=headers, stream=True)
        if video.status_code == 206:
            chunk_size = 1024
            content_size = int(video.headers['content-length'])
            data_count = 0
            with open('./download/' + urls['title'] + '.mp4', 'wb') as f:
                for data in video.iter_content(chunk_size=chunk_size):
                    f.write(data)
                    data_count += len(data)
                    progress = data_count * 100 / content_size
                    print('\r 正在下载视频：[%s%s] %d%%' % (int(progress) * '█', ' ' * (100 - int(progress)), progress),
                          end=' ')
    except:
        print("Error!")
        shutil.rmtree('./download')
        return False
    try:
        audio = requests.get(urls['audio'], headers=headers, stream=True)
        print(audio.status_code)
        if audio.status_code == 206:
            chunk_size = 1024
            content_size = int(audio.headers['content-length'])
            data_count = 0
            with open('./download/' + urls['title'] + '.mp3', 'wb') as f:
                for data in audio.iter_content(chunk_size=chunk_size):
                    f.write(data)
                    data_count += len(data)
                    progress = data_count * 100 / content_size
                    print('\r 正在下载音频[%s%s] %d%%' % (int(progress) * '█', ' ' * (100 - int(progress)), progress),
                          end=' ')
    except:
        print('Error!')
        shutil.rmtree('./download')
        return False
    merge(urls['title'], urls['title_of_series'],counts)
    shutil.rmtree('./download')
    return True

if __name__ == '__main__':
    mid = input("please input mid:")
    pns = input("please input page")
    page = get_page(mid)
    base_url = "https://www.bilibili.com/video/"
    end_url = "/?spm_id_from=333.999.0.0&vd_source=1044410fba936cd01d24526cd1edef1a"
    for i in range(pns,page+1):
        lists = []
        pn_count = 0
        result = get_data(mid,i)['data']['list']['vlist']
        for j in get_data(mid,i)['data']['list']['vlist']:
            urls = base_url + j['bvid'] + end_url
            type = type_of_video(urls)
            allurls = get_all_url(urls, type)
            header_in ={
                "cookie":"buvid3=9EF91E31-4B3D-4A30-FE7D-5D76BE03D9E327371infoc; b_nut=1674285927; _uuid=21B42DFA-31FE-87E1-9512-12F95299A75A27643infoc; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=|(k|k)Y)mJ)R0J'uY~Rk)Y|YJ; i-wanna-go-back=-1; b_ut=5; hit-new-style-dyn=0; hit-dyn-v2=1; header_theme_version=CLOSE; home_feed_column=5; CURRENT_QUALITY=112; buvid4=CEEADE42-25AF-AECE-D530-764A770777A828760-023012115-c8mC4VtaIp%2BYz8JESbGfsg%3D%3D; buvid_fp_plain=undefined; LIVE_BUVID=AUTO4016792195519835; CURRENT_PID=4c13d250-c91f-11ed-9c02-8d69ae93ec42; FEED_LIVE_VERSION=V8; bp_video_offset_283470100=785058960366370800; browser_resolution=1536-714; DedeUserID=96917526; DedeUserID__ckMd5=9976e0758470471c; fingerprint=bdb93d286701b889041fa2e6415f8d80; buvid_fp=bdb93d286701b889041fa2e6415f8d80; PVID=3; SESSDATA=6de1a57a%2C1698507704%2C5c306%2A51; bili_jct=18644e645f19b5f5bd022e52097922a6; sid=5mgkji03; b_lsid=91066C910B_187DA94F939; bp_video_offset_96917526=790810359708516400",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            }
            responses = requests.get(allurls,headers=header_in).text
            s = etree.HTML(responses)
            data = s.xpath('//*[@id="multi_page"]/div[2]/ul/li')
            if len(data)!=0:
                base_url_in = "https://www.bilibili.com/video/"
                end_url_in = "&spm_id_from=333.999.0.0&vd_source=1044410fba936cd01d24526cd1edef1a"
                for z in range(1,len(data)+1):
                    urls_in = base_url_in+j['bvid']+"?p="+str(z)+end_url_in
                    type_in = type_of_video(urls_in)
                    allurls_in = get_all_url(urls_in, type_in)
                    urls_in = get_downloadurl(allurls_in, type_in)
                    data = re.findall(r"part.*?(?=,)",responses)
                    if (data[z-1].split(':')[1].strip('"'))=="防撞":
                        urls_in['title'] = data[0].split(':')[1].strip('"')+"防撞"
                    else:
                        urls_in['title'] = data[z-1].split(':')[1].strip('"')
                    try:
                        print(urls_in['title'])
                        lists.append(urls_in)
                        time.sleep(1)
                    except:
                        pass
                pn_count=pn_count+1
            else:
                try:
                    if isinstance(allurls, str):
                        urls = get_downloadurl(allurls, type)
                        pn_count = pn_count+1
                        time.sleep(1)
                        print(urls['title'])
                        lists.append(urls)
                except:
                    pn_count=pn_count+1
                    pass
            if pn_count==len(result):
                for i in range(len(lists)):
                    down_video(lists[i],pns)  
                    time.sleep(1)
                pns=pns+1
                time.sleep(5)