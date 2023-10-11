# coding:utf-8


def get_id_link_mapping():
    import os,json
    dir=os.getcwd()
    js_path=os.path.join(dir,'SoftLinkType.js')
    id_link={}
    with open(js_path,'r',encoding='utf-8') as f:
        s=f.read().replace('AddressList =','')
        s_to_dict=json.loads(s)
        for k,v in s_to_dict.items():
            id_link[k.replace('siteId_','')]=v.split('||')[1].split(',')[0]
    return id_link

if __name__ == '__main__':
    print(get_id_link_mapping())