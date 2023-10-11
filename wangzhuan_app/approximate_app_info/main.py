# _*_coding:utf-8 _*_
# @Time　　 : 2020/1/13   1:38
# @Author　 : zimo
# @File　   :2鼠标事件.py
# @Software :PyCharm
# @Theme    :
import os
from anxz import get_app_url as anxz_get_app_url
from fs import get_app_url as fs_get_app_url
from pc6 import get_app_url  as pc6_get_app_url

keyword_list=['星卫tv','金桔影视','九州影院','青影2.0','热气球视频','少年直播','tuneinradio','tv鼠直播','彬彬影视','测试直播','大众电视（diy)','更省影视','捷视直播','老虎影视','雷达tv','秒看电视','神马直播','视频电影','thepodcastplayer(又名:listen)','战斧直播','天王星直播','天空直播','港人话电视','冬瓜直播','呈祥tv','新电视直播','骡马tv影院','橙子影院','酷点iptv','一个tv','小小电视','星蕾tv','优看tv','绿野直播','老柏直播','星河tv','feeddlerrssnewsreader','feedme','newsjet','dailyfeed','精通rss(又名：rsssavvy)','rsspod','人人网','pods','audecibel','radio.net','soaeo','podme','procast','podcastapp','podcast+1','podbox','leela','audionow','番茄','爱爱你直播','bobo直播','91短视频','嗨森约玩','wionnews','腾浪跨境浏览器','威行浏览器','kuai500加速','yivster','hubl','worldnews','오디오랄란','tv.nu','劲达投资','小肚皮','popi']
for keyword in keyword_list:
    anxz_app_info = anxz_get_app_url(keyword)
    fs_app_info = fs_get_app_url(keyword)
    pc6_app_info = pc6_get_app_url(keyword)
    channels_app_result=[anxz_app_info,fs_app_info,pc6_app_info]
    valid_channels_app_result=[c for c in channels_app_result if c]
    if valid_channels_app_result:
        for v in valid_channels_app_result:
            print(list(v.values())[1]['app_name'],list(v.values())[1]['developer'])
            with open(os.path.join(os.getcwd(),'channels_app_info.txt'),'w') as f:
                f.write(str(v))