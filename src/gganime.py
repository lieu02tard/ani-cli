#Search anime by name
import requests
import re
import sys
#URLs
mainurl     = "https://gogoanime.pe"
titlepat    = "<a href=/category/"
searchpat   = f"{mainurl}/search.html?keyword="
epipat      = f"{mainurl}/category"

#Color codes
c_red       = "\033[1;31m]"
c_green     = "\033[1;32m]"
c_yellow    = "\033[1;33m]"
c_blue      = "\033[1;34m]"
c_magenta   = "\033[1;35m]"
c_cyan      = "\033[1;36m]"
c_reset     = "\033[0m"

def print_help():
	pass

def search_anime(query: str):
    search  = query.strip().strip('-')
    print(search)
    req     = requests.get(f"{searchpat}{search}")
    req.encoding = 'utf-8'
    rq      = re.findall(r"<a href=\"/category/([^\"]*)\" title=\"([^\"]*)\".*_\1_p", req.text)
    if len (rq) == 0:
        return None
    return rq

#Search episodes by animeid
def search_eps(animeid: str):
    req     = requests.get(f"{epipat}/{animeid}")
    req.encoding = 'utf-8'
    rq      = re.findall(r"/^[[:space:]]*<a href=\"#\" class=\"active\" ep_start/{s/.* '\''([0-9]*)'\'' ep_end = '\''([0-9]*)'\''.*/\2/pq}", req.text)
    if len(rq) == 0:
        return None
    return rq

#Get embedded video link
def embvid_link(animeid: str, epno: str):
    req     = requests.get(f"${mainurl}/${animeid}-episode-${epno}")
    req.encoding = 'utf-8'
    rq      = re.findall(r'/^[[:space:]]*<a href="#" rel="100"/{s/.*data-video="([^"]*)".*/https:\1/pq}', req.text)
    if len(rq) == 0:
        return None
    return rq

#Get video quality
def get_vidqual(quality, evidurl, vidurl):
    req     = requests.get("${vidurl}", headers={"referer":evidurl})
    req.encoding = 'utf-8'
    available_qual = re.findall(r's/.*NAME="([^p]*)p"/\1/p', req.text)
    if quality == "best":
        return available_qual[-1]
    elif quality == "worst":
        return available_qual[0]
    else:
        video_qual = quality
        if not quality in available_qual:
            print(f"{c_red}Current video quality is not available (defaulting to highest quality){c_reset}", file = sys.stderr)
            reqqual = "best"
            video_qual = available_qual[-1]
        return video_qual

#Get link for embedded video
def get_links(quality, emb_vidurl: str):
    req     = requests.get(emb_vidurl)
    req.encoding = 'utf-8'
    vidurl  = re.findall(r"/^[[:space:]]*sources:/{s/.*(https[^'\'']*).*/\1/pq}", req.text)
    vidqual = get_vidqual(quality, emb_vidurl, vidurl[0])

    #Replace the video with highest quality video
    _return = re.findall(r"s/(.*)\.m3u8/\1." + re.escape(vidqual) + r".m3u8/p", vidurl[0])
    if len(_return) == 0:
        return None
    return _return

def open_episode(animeid, episode, is_download, quality):
	pass