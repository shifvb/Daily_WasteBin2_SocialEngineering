import os
import pprint


def address_filter(line, handled_dict):
    """
    Parse semi-identified address string to universal address string (category by region/province).
    Use if-elif-else statements for speed (rather than dynamic dict).
    :param line: address line contains address, str type
    :param handled_dict: a dict contains region, dict type
    :return: True if in handled_dict, False if not in handled_dict, bool type
    """
    # 4个直辖市
    if "北京" in line or "海淀" in line or "朝阳" in line or "东城区" in line or "大兴" in line or "崇文" in line \
            or "丰台" in line or "通州" in line or "海滨" in line or "石景山" in line or "BEIJING" in line \
            or "beijingshi" in line:
        handled_dict["北京市"] += 1
    elif "天津" in line or "东丽" in line or "tianjin" in line or "夭津" in line or "塘沽" in line or "蓟县" in line \
            or "西青" in line or "南开" in line or "TIANJIN " in line:
        handled_dict["天津市"] += 1
    elif "上海" in line or "奉贤" in line or "浦东" in line or "崇明" in line or "虹口" in line or "松江" in line \
            or "宝山" in line or "徐汇" in line or "漕溪" in line or "陆家浜" in line or "杨浦" in line \
            or "宋园" in line or "闵行" in line or "嘉定" in line or "长宁" in line or "普陀" in line \
            or "shanghai" in line or "SHANGHAI" in line or "Shanghai" in line:
        handled_dict["上海市"] += 1
    elif "重庆" in line or "长寿" in line or "九龙坡" in line or "永川" in line or "沙坪坝" in line \
            or "巫溪" in line or "巴南" in line or "渝北" in line or "龙兴" in line:
        handled_dict["重庆市"] += 1
    # 23个省
    elif "河北" in line or "唐山" in line or "石家庄" in line or "裕华" in line or "桥东" in line or "新华" in line \
            or "桥西" in line or "辛集" in line or "开平" in line or "张家口" in line or "华龙" in line \
            or "正定" in line or "涞源" in line or "秦皇岛" in line or "衡水" in line:
        handled_dict["河北省"] += 1
    elif "山西" in line or "万柏林" in line or "太原" in line or "小店" in line or "平鲁" in line or "高平" in line \
            or "清徐" in line:
        handled_dict["山西省"] += 1
    elif "辽宁" in line or "大连" in line or "沈阳" in line or "甘井子" in line or "立山" in line or "瓦房店" in line \
            or "沙河口" in line or "皇姑" in line or "大东" in line or "鞍山" in line or "铁西" in line or "连山" in line \
            or "中山区" in line or "盘锦" in line or "和平区" in line or "liaoning" in line or "铁岭" in line \
            or "丹东" in line:
        handled_dict["辽宁省"] += 1
    elif "吉林" in line or "长春" in line or "南关" in line or "四平" in line or "通化" in line or "jilin" in line:
        handled_dict["吉林省"] += 1
    elif "黑龙江" in line or "哈尔滨" in line or "南岗" in line or "道里" in line or "鸡西" in line or "大庆" in line \
            or "双鸭山" in line or "道外" in line or "佳木斯" in line or "爱辉" in line or "五常" in line or "伊春" in line \
            or "牡丹江" in line or "齐齐哈尔" in line:
        handled_dict["黑龙江省"] += 1
    elif "江苏" in line or "海门" in line or "南京" in line or "无锡" in line or "苏州" in line or "白下" in line \
            or "泉山" in line or "丹徒" in line or "沧浪" in line or "江阴" in line or "市京" in line \
            or "京口" in line or "丹阳" in line or "扬中" in line or "淮阴" in line or "清河" in line \
            or "扬中" in line or "楚州" in line or "清浦" in line or "京口" in line or "盐城" in line \
            or "嵊州" in line or "灌南" in line or "常州" in line or "海安" in line or "沭阳" in line or "周铁" in line \
            or "徐州" in line or "南通" in line or "临安" in line or "常州" in line or "台州" in line or "宜兴" in line \
            or "海陵" in line or "靖江" in line or "张家" in line or "镇江" in line or "如皋" in line or "东台" in line \
            or "大丰" in line or "如皋" in line or "连云港" in line or "如皋" in line or "淮安" in line or "姜堰" in line \
            or "昆山" in line or "扬州" in line or "蘇州" in line or "范市" in line or "邳州" in line:
        handled_dict["江苏省"] += 1
    elif "浙江" in line or "杭州" in line or "宁波" in line or "绍兴" in line or "江东" in line or "瑞安" in line \
            or "越城" in line or "象山" in line or "温州" in line or "上城" in line or "吴兴" in line or "萧山" in line \
            or "草塔" in line or "天台" in line or "宁海" in line or "慈溪" in line or "上虞" in line or "平阳" in line \
            or "武义" in line or "嘉兴" in line or "诸暨" in line or "金华" in line or "zhejiang" in line or "湖州" in line \
            or "余姚" in line or "龙泉" in line or "东阳" in line:
        handled_dict["浙江省"] += 1
    elif "安徽" in line or "黄山" in line or "合肥" in line or "鸠江" in line or "颖泉" in line or "迎江" in line or \
            "淮南" in line or "太湖县" in line or "安微" in line or "宿州" in line or "芜湖" in line or "繁昌" in line \
            or "马鞍山" in line or "淮北" in line or "蜀山" in line or "当涂" in line or "蚌埠" in line or "庐阳" in line \
            or "安庆" in line or "铜陵" in line:
        handled_dict["安徽省"] += 1
    elif "福建" in line or "厦门" in line or "莆田" in line or "晋江" in line or "台江" in line or "长乐" in line \
            or "泉州" in line or "福州" in line or "晋安" in line or "南靖" in line or "仓山" in line or "福清" in line:
        handled_dict["福建省"] += 1
    elif "江西" in line or "南昌" in line or "萍乡" in line or "临川" in line or "乐平" in line or "上饶" in line \
            or "吉安" in line:
        handled_dict["江西省"] += 1
    elif "山东" in line or "济南" in line or "青岛" in line or "章丘" in line or "奎文" in line or "东营" in line \
            or "平阴" in line or "龙口" in line or "张店" in line or "胶南" in line or "德州" in line or "安丘" in line \
            or "莱山" in line or "海阳" in line or "坊子" in line or "章丘" in line or "汶上" in line or "桓台" in line \
            or "寿光" in line or "海阳" in line or "临朐" in line or "城阳" in line or "潍坊" in line or "长清" in line \
            or "長清" in line or "高密" in line or "莒县" in line or "天桥" in line or "历下" in line or "临沂" in line \
            or "烟台" in line or "萊陽" in line or "qingdao" in line or "shandong" in line or "淄博" in line \
            or "枣庄" in line:
        handled_dict["山东省"] += 1
    elif "河南" in line or "郑州" in line or "河市省" in line or "鹤壁" in line or "洛阳" in line or "伊川" in line \
            or "项城" in line or "开封" in line or "商城县" in line or "何南" in line or "偃师" in line or "唐河" in line \
            or "罗山" in line or "澶河" in line or "安阳" in line:
        handled_dict["河南省"] += 1
    elif "湖北" in line or "武汉" in line or "洪山" in line or "夷陵" in line or "西陵" in line or "江岸" in line \
            or "猇亭" in line or "鄂州" in line or "武昌" in line or "青山" in line or "伍家" in line or "江汉" in line \
            or "黄陂" in line or "孝南" in line or "郢中" in line or "黄破" in line or "荆门" in line:
        handled_dict["湖北省"] += 1
    elif "湖南" in line or "长沙" in line or "湖市省" in line or "湘潭" in line or "怀化" in line or "醴陵" in line \
            or "株洲" in line or "雨花" in line or "天心" in line:
        handled_dict["湖南省"] += 1
    elif "广东" in line or "广州" in line or "深圳" in line or "顺德" in line or "万江" in line or "萝岗" in line \
            or "凤岗" in line or "黄浦" in line or "南山" in line or "海珠" in line or "虎门" in line \
            or "高埗" in line or "厚街" in line or "大朗" in line or "东莞" in line or "沙田" in line \
            or "黄埔" in line or "龙岗" in line or "荔湾" in line or "汕头" in line or "广 东" in line \
            or "茂名" in line or "廣東" in line or "廣州" in line or "guangdong" in line or "惠州" in line \
            or "中山市" in line or "湛江" in line or "江门" in line or "東莞" in line:
        handled_dict["广东省"] += 1
    elif "海南" in line or "海口" in line or "海市" in line or "五指山" in line or "三亚" in line:
        handled_dict["海南省"] += 1
    elif "四川" in line or "成都" in line or "都江堰" in line or "四州省" in line or "南部县" in line or "青羊" in line \
            or "三台" in line or "金牛" in line:
        handled_dict["四川省"] += 1
    elif "贵州" in line or "南明" in line or "贵阳" in line or "贵呀" in line:
        handled_dict["贵州省"] += 1
    elif "云南" in line or "云市省" in line or "昆明" in line or "西山" in line:
        handled_dict["云南省"] += 1
    elif "陕西" in line or "西安" in line or "莲湖" in line or "秦都" in line or "碑林" in line or "耀州" in line \
            or "宝鸡" in line or "金台" in line or "凤翔" in line or "xi'an" in line:
        handled_dict["陕西省"] += 1
    elif "甘肃" in line or "兰州" in line or "玉门" in line:
        handled_dict["甘肃省"] += 1
    elif "青海" in line or "果洛藏族" in line or "西宁" in line:
        handled_dict["青海省"] += 1
    elif "台湾" in line or "台北" in line or "高雄" in line or "台灣" in line or "新北" in line or "中和" in line \
            or "台中市" in line or "永和" in line or "台南" in line or "嘉義市" in line or "三重市" in line:
        handled_dict["台湾省"] += 1
    # 5自治区
    elif "蒙古" in line or "呼和浩特" in line or "包头" in line or "内蒙" in line or "呼伦贝尔" in line:
        handled_dict["内蒙古自治区"] += 1
    elif "广西" in line or "南宁" in line or "柳北" in line or "柳南" in line or "城中" in line or "兴宁" in line \
            or "市宁" in line or "青秀" in line or "柳州" in line:
        handled_dict["广西壮族自治区"] += 1
    elif "西藏" in line or "拉萨" in line:
        handled_dict["西藏自治区"] += 1
    elif "宁夏" in line or "银川" in line:
        handled_dict["宁夏回族自治区"] += 1
    elif "新疆" in line or "乌鲁木齐" in line or "吐鲁番" in line:
        handled_dict["新疆维吾尔自治区"] += 1
    # 2特别行政区
    elif "香港" in line or "HK" in line or "Hong Kong" in line or "HONGKONG" in line:
        handled_dict["香港特别行政区"] += 1
    elif "澳门特别行政区" in line:
        handled_dict["澳门特别行政区"] += 1
    # extra
    elif "中国" in line or "CHN" in line or "个人" in line or "公司" in line or "城区" in line or "大厦" in line \
            or "中区" in line or "开发区" in line or "市区" in line or "人民路" in line or "高新" in line:
        handled_dict["中国其它地区"] += 1

    # 国外
    elif "美国" in line or "USA" in line:
        handled_dict["美国"] += 1
    elif "日本" in line or "JPN" in line or "JAPAN" in line or "大阪" in line:
        handled_dict["日本"] += 1
    elif "澳大利亚" in line or "AUS" in line:
        handled_dict["澳大利亚"] += 1
    elif "新加坡" in line or "SGP" in line or "Singapore" in line:
        handled_dict["新加坡"] += 1
    elif "韩国" in line or "KOR" in line:
        handled_dict["韩国"] += 1
    elif "马来西亚" in line or "MYS" in line:
        handled_dict["马来西亚"] += 1
    elif "cze" in line or "CZE" in line:
        handled_dict["捷克共和国"] += 1
    elif "巴基斯坦" in line:
        handled_dict["巴基斯坦"] += 1
    elif "NZL" in line or "新西兰" in line:
        handled_dict["新西兰"] += 1
    elif "CAN" in line:
        handled_dict["加拿大"] += 1
    elif "GBR" in line:
        handled_dict["英国"] += 1
    elif "NOR" in line:
        handled_dict["挪威"] += 1
    elif "印度" in line or "IND" in line:
        handled_dict["印度"] += 1
    elif "RUS" in line:
        handled_dict['俄罗斯'] += 1
    elif "BLR" in line:
        handled_dict["白俄罗斯"] += 1
    elif "ITA" in line or "意大利" in line:
        handled_dict["意大利"] += 1
    elif "TUR" in line:
        handled_dict["土耳其"] += 1
    elif "MNG" in line:
        handled_dict["蒙古"] += 1
    elif "SAU" in line:
        handled_dict["沙特阿拉伯"] += 1
    elif "IDN" in line:
        handled_dict["印度尼西亚"] += 1
    elif "缅甸" in line:
        handled_dict["缅甸"] += 1
    elif "德国" in line:
        handled_dict["德国"] += 1
    else:
        return False
    return True


def main():
    input_path = r"d:\\address_2.txt"
    output_path = r"d:\\address_out.txt"
    total_lines_counter = 0
    not_handled_counter = 0
    handled_dict = {
        # 4个直辖市
        "北京市": 0,
        "天津市": 0,
        "上海市": 0,
        "重庆市": 0,
        # 23个省
        "河北省": 0,
        "山西省": 0,
        "辽宁省": 0,
        "吉林省": 0,
        "黑龙江省": 0,
        "江苏省": 0,
        "浙江省": 0,
        "安徽省": 0,
        "福建省": 0,
        "江西省": 0,
        "山东省": 0,
        "河南省": 0,
        "湖北省": 0,
        "湖南省": 0,
        "广东省": 0,
        "海南省": 0,
        "四川省": 0,
        "贵州省": 0,
        "云南省": 0,
        "陕西省": 0,
        "甘肃省": 0,
        "青海省": 0,
        "台湾省": 0,
        # 5自治区
        "内蒙古自治区": 0,
        "广西壮族自治区": 0,
        "西藏自治区": 0,
        "宁夏回族自治区": 0,
        "新疆维吾尔自治区": 0,
        # 2特别行政区
        "香港特别行政区": 0,
        "澳门特别行政区": 0,
        # extra
        "中国其它地区": 0,

        # 国外
        "美国": 0,
        "日本": 0,
        "澳大利亚": 0,
        "新加坡": 0,
        "韩国": 0,
        "马来西亚": 0,
        "巴基斯坦": 0,
        "新西兰": 0,
        "加拿大": 0,
        "英国": 0,
        "挪威": 0,
        "印度": 0,
        "俄罗斯": 0,
        "白俄罗斯": 0,
        "意大利": 0,
        "土耳其": 0,
        "蒙古": 0,
        "沙特阿拉伯": 0,
        "印度尼西亚": 0,
        "缅甸": 0,
        "德国": 0,
        "捷克共和国": 0,
    }
    f_out = open(output_path, mode="w", encoding="utf8")
    with open(input_path, mode='r', encoding='utf8') as f:
        while True:
            line = f.readline()
            if line == "":
                break
            total_lines_counter += 1
            if address_filter(line, handled_dict) is False:
                not_handled_counter += 1
                f_out.write(line)
    f_out.close()
    print("total: {}, not_handled: {}".format(total_lines_counter, not_handled_counter))
    pprint.pprint(handled_dict)


if __name__ == '__main__':
    main()
