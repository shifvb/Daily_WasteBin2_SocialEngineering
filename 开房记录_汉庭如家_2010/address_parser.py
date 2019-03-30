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
    if "北京" in line or "海淀区" in line or "朝阳区" in line or "东城区" in line or "大兴区" in line or "丰台区" in line:
        handled_dict["北京市"] += 1
    elif "天津" in line:
        handled_dict["天津市"] += 1
    elif "上海" in line or "奉贤区" in line or "浦东新区" in line or "崇明县" in line  or "虹口区" in line \
            or "宝山区" in line or "徐汇区" in line:
        handled_dict["上海市"] += 1
    elif "重庆" in line:
        handled_dict["重庆市"] += 1
    # 23个省
    elif "河北" in line or "唐山" in line or "石家庄" in line or "裕华区" in line or "桥东区" in line \
            or "桥西区" in line or "辛集区" in line or "开平区" in line or "张家口" in line:
        handled_dict["河北省"] += 1
    elif "山西" in line or "万柏林区" in line:
        handled_dict["山西省"] += 1
    elif "辽宁" in line or "大连" in line or "沈阳" in line or "甘井子区" in line or "立山区" in line or "瓦房店" in line \
            or "沙河口区" in line or "皇姑区" in line:
        handled_dict["辽宁省"] += 1
    elif "吉林" in line or "长春市" in line:
        handled_dict["吉林省"] += 1
    elif "黑龙江" in line or "哈尔滨" in line or "南岗区" in line or "道里区" in line:
        handled_dict["黑龙江省"] += 1
    elif "江苏" in line or "海门" in line or "南京" in line or "无锡" in line or "苏州" in line or "白下区" in line \
            or "泉山区" in line or "丹徒区" in line or "沧浪区" in line:
        handled_dict["江苏省"] += 1
    elif "浙江" in line or "杭州" in line or "宁波" in line or "绍兴区" in line or "江东区" in line or "瑞安市" in line \
            or "越城区" in line or "象山县" in line:
        handled_dict["浙江省"] += 1
    elif "安徽" in line or "黄山" in line or "合肥" in line or "鸠江区" in line or "颖泉区" in line:
        handled_dict["安徽省"] += 1
    elif "福建" in line or "厦门" in line or "莆田" in line or "晋江" in line or "台江区" in line or "长乐区" in line:
        handled_dict["福建省"] += 1
    elif "江西" in line or "南昌" in line:
        handled_dict["江西省"] += 1
    elif "山东" in line or "济南" in line or "青岛" in line or "章丘区" in line or "奎文区" in line or "东营市" in line \
            or "平阴区" in line or "龙口市" in line or "张店区" in line or "胶南区" in line:
        handled_dict["山东省"] += 1
    elif "河南" in line or "郑州" in line or "河市省" in line:
        handled_dict["河南省"] += 1
    elif "湖北" in line or "武汉" in line or "洪山区" in line:
        handled_dict["湖北省"] += 1
    elif "湖南" in line or "长沙市" in line or "湖市省" in line:
        handled_dict["湖南省"] += 1
    elif "广东" in line or "广州" in line or "深圳" in line or "顺德区" in line or "万江区" in line or "萝岗区" in line \
            or "凤岗镇" in line or "黄浦区" in line or "南山区" in line or "海珠区" in line:
        handled_dict["广东省"] += 1
    elif "海南" in line or "海口" in line:
        handled_dict["海南省"] += 1
    elif "四川" in line or "成都" in line or "都江堰市" in line:
        handled_dict["四川省"] += 1
    elif "贵州" in line or "南明区" in line:
        handled_dict["贵州省"] += 1
    elif "云南" in line:
        handled_dict["云南省"] += 1
    elif "陕西" in line or "西安" in line:
        handled_dict["陕西省"] += 1
    elif "甘肃" in line or "兰州" in line:
        handled_dict["甘肃省"] += 1
    elif "青海" in line:
        handled_dict["青海省"] += 1
    elif "台湾" in line or "台北" in line:
        handled_dict["台湾省"] += 1
    # 5自治区
    elif "蒙古" in line or "呼和浩特" in line or "包头市" in line:
        handled_dict["内蒙古自治区"] += 1
    elif "广西" in line or "南宁市" in line or "柳北区" in line or "柳南区" in line or "城中区" in line or "兴宁区" in line:
        handled_dict["广西壮族自治区"] += 1
    elif "西藏" in line:
        handled_dict["西藏自治区"] += 1
    elif "宁夏" in line or "银川" in line:
        handled_dict["宁夏回族自治区"] += 1
    elif "新疆" in line or "乌鲁木齐" in line:
        handled_dict["新疆维吾尔自治区"] += 1
    # 2特别行政区
    elif "香港" in line:
        handled_dict["香港特别行政区"] += 1
    elif "澳门特别行政区" in line:
        handled_dict["澳门特别行政区"] += 1
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
