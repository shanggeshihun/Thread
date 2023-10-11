# _*_coding:utf-8 _*_
# @Time     :2020/10/26 0026   上午 12:23
# @Author   : Antipa
# @File     :resourceStr_classify.py
# @Theme    :PyCharm
import os
# 资源字符串  关键词 字典
type_keyword_dict={
    '钱包（区块链）':'公钥,币种,私钥,节点,钱包,手续费,矿工,托管账户,节点,内存,区块',
    '交易所（虚拟货币）':'持仓,收盘,开盘,手续费,交易所,平仓,K线,挖矿,充币,提币,银行卡,交易账户,返佣|佣金,分红,以太坊,冻结,邀请人|邀请码|推荐人,涨跌,区块,白皮书',
    '钱包+手机银行':'持卡人证件号|持卡人身份证号|身份证,预留手机,银行理财,借记卡,签约账户,银行卡|银行卡号|银行卡管理|绑定银行卡号,储蓄卡,提现,转账,银行账号,银行预留|绑定手机|预留手机,云闪付,身份证背面,跨行转账,我的贷款,安全键盘,指纹识别,储蓄账户,收款,限额,快捷支付,手机银行,网上银行,刷卡交易,POS机,信用卡,持卡人,磁条卡,日限额,月限额',
    '贷款+p2p':'已还金额, 提前还款, 担保人|保险人, 车押标, 待收金额, 银行托管, 出借, 房押标, 已还期数, 收益率, 已垫付, 银行存管|存管账户|存管银行, 逾期|逾期罚息|逾期天数|逾期金额, 等额本息, 贷款, 等额本金, 还款日|还款利息|还款计划|还款方式, 待放款, 还款中,投标|散标, 分期金额, 担保标, 债权|债权转让, 存管账户|银行存管|存管银行, 账单利息, 期数, 年化收益, 利息|利息总额|利息复投, 银行卡, 在投金额|投资, 信用标, 还款本金|本金, 冻结|冻结金额, 持卡人签名, 年利率|收益|回报率|年化利率',
    '保险+理财':'赔案金额,理赔,保单,保险人,保费,续保,保险,超速,事故,投标,回款,银行存管|存管账户|存管银行,预留手机,理赔,债权原价,加息,保险,还款日|还款利息|还款计划|还款方式,收款账户,金融资产,银行流水,金融资产,私募,公募,调仓,基金,资金监管',
    '区块链挖矿':'邀请人|邀请码|推荐人,交易哈希,矿机,节点,静态收益,直推加速,收币,提币,算力,提币,挂单,充币,开户,USDT,持币生息,年化收益,分红,结息,认证,认购,锁仓,转锁,数字资产,糖果',
    '股票+期货+贵金属':'赚钱,散户,分红,K线,跌停,涨停,港股,美股,A股,中概股,抄底,轻仓,大盘云图,持仓,平仓,开仓,交仓,期货,开户,追缴,私募,股票,资产负债,期货,换手率,市盈率,债券,黄金,白银,贵金属,挂单',
    '区块链理财':'算力,智能合约,挖矿,区块,已放款,已认证,已还款,白皮书,币圈,币种列表,白皮书,收益曲线,兑换,USDT,冲币,提币,持币,增仓,做空,溢价,短线掘金,盯盘',
    '系统办公+生活服务':'采购商,库存,销售,客户,利润,出纳,资产负债,仓管,利润表,供应商,代理商,商圈,身份验证,发票抬头,经销商,招商,批发',
    '社交聊天':'禁言,群管理,退群|退出群,群公告,群收费,群助手,群聊,群号,群设置,工会,管理员,玩伴,周榜,日榜,连麦,打赏,贡献榜,视频聊,语音聊,粉丝,师徒,约聊,交友',
    '生活服务':'物业缴费,业主,燃气费,电费,水费,小区,押金,租赁,租住,合同,租金,司机,预约专享,呼叫出租车,联系师傅,乘客,行程已关闭,里程费,调节费,取消叫车,调度费,顺风车',
    '隐私生活':'拍摄|拍照|自拍,相册|相机,滤镜,重新拍',
    '虚拟货币+区块链游戏+零撸资金盘':'邀请人|邀请码|推荐人,活跃度,趣豆|云豆|福豆|花豆|咖啡豆|波豆|秘豆|链豆|钻|圣果|糖果|酒|卷轴|宝石|茶叶|羽毛|体力|福星|音点|数字货币|科呗|帮呗|借呗|呗壳|淘呗|算力|水晶,交易手续费,实名认证,区块,分红,佣金|返佣,分红羊|分红龙,永久分红',
    '电商购物+直播':'权益金,现金券,引荐,打赏,主播榜|魅力榜|土豪榜,送我礼物|送礼物,取消关注,粉丝,包邮,优惠券,购物车,家居|厨具|母婴|服饰|数码|运动鞋,订单编号,返利',
}
# 程序名称  字符串关键词 字典
app_type_keyword_dict={
    '虚拟货币+区块链游戏+零撸资金盘':'世界|鼠|牛|虎|兔|龙|蛇|羊|猴|鸡|狗|猪|鱼|猫|马|宠|汪|喵|养|熊|海豚|鹅|鸭|鲲|牧场|农场,区块,分红,佣金|返佣,分红羊|分红龙,永久分红'
}

# 资源字符串  分类-关键词列表  字典
type_keyword_dict_new={}
all_keyword_list=[]
for k,v in type_keyword_dict.items():
    keyword_list=[k.strip() for k in v.split(',')]
    type_keyword_dict_new[k]=keyword_list
    all_keyword_list.extend(keyword_list)
# 程序名称  分类-关键词列表  字典
app_type_keyword_dict_new={}
app_all_keyword_list=[]
for k,v in app_type_keyword_dict.items():
    app_keyword_list=[k.strip() for k in v.split(',')]
    app_type_keyword_dict_new[k]=app_keyword_list
    app_all_keyword_list.extend(app_keyword_list)

merge_keyword_list=all_keyword_list+app_all_keyword_list
keyword_set=set(merge_keyword_list)
print('****所有关键词标签****')
print(keyword_set)

import os
with open(os.path.join(os.getcwd(),'resourceStr.txt'),'r',encoding='utf-8') as f:
    resourceStr=f.read()
with open(os.path.join(os.getcwd(), 'resourceStr.txt'), 'r', encoding='utf-8') as f:
    resourceStr_lines=f.readlines()
app_name=''
for line in resourceStr_lines:
    if 'app_name' in line:
        app_name=line.split('=')[1].strip()
        break

print('****应用名称****\n',app_name)

print('****分类结果的关键词标签****')
# 资源字符串  分类结果-关键词标签  字典
type_keyword_dict_result={}
for k,v in type_keyword_dict_new.items():
    v_result=[]
    for t in v:
        t_list=t.split('|')
        for tmp in t_list:
            if tmp in resourceStr:
                v_result.append(t)
                break
    if v_result:
        type_keyword_dict_result[k]=v_result
        # print(k,':',len(v_result),':',v_result)
# 程序名称  分类结果-关键词标签  字典
app_type_keyword_dict_result={}
for k,v in app_type_keyword_dict_new.items():
    v_result=[]
    for t in v:
        t_list=t.split('|')
        for tmp in t_list:
            if tmp in app_name:
                v_result.append(t)
                break
    if v_result:
        app_type_keyword_dict_result[k]=v_result
# 合并 资源字符串+程序名称  分类结果-关键词标签  字典
merge_type_keyword_dict_result={}
for k in app_type_keyword_dict_result.keys():
    if k in type_keyword_dict_result.keys():
        type_keyword_dict_result[k]=type_keyword_dict_result[k]+app_type_keyword_dict_result[k]

# 分类结果-关键词标签  列表
type_keyword_result_list=sorted(type_keyword_dict_result.items(), key=lambda item:len(item[1]), reverse=True)
for tup in type_keyword_result_list:
    print(tup[0], ':', len(type_keyword_dict_new[tup[0]]),':',len(tup[1]), ':',tup[1])
print('\n')

