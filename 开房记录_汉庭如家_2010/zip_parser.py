"""
此文件用来记录邮政编码和地区的对应关系，目前只考虑邮政编码前两位
"""

zip_region_mapping = {
    '10': '北京',
    '20': '上海',
    '30': '天津',
    '40': '重庆',
    '01': '内蒙中西部',
    '02': '内蒙东部',
    '03': '山西中北部',
    '04': '山西南部',
    '05': '河北中部',
    '06': '河北东部（大概，有点乱）',
    '07': '河北西部（大概，有点乱）',
    '11': '辽宁中东部',
    '12': '辽西',
    '13': '吉林全省',
    '15': '黑龙江中东部',
    '16': '黑龙江西部，内蒙呼伦贝尔一部',
    '21': '苏南',
    '22': '苏北',
    '23': '皖北',
    '24': '皖南',
    '25': '鲁西北',
    '26': '胶东',
    '27': '鲁中南',
    '31': '浙北',
    '32': '浙南',
    '33': '赣北',
    '34': '赣南',
    '35': '闽北',
    '36': '闽南',
    '41': '湖南北部（张家界除外）',
    '42': '湖南南部、张家界',
    '43': '湖北东部',
    '44': '湖北西部',
    '45': '河南北部',
    '46': '河南南部',
    '47': '河南东、西部',
    '51': '广东东部（潮州、揭阳除外）',
    '52': '广东西部、',
    '53': '广西西南部',
    '54': '广西东北部',
    '55': '贵州中部',
    '56': '贵州东北、西南部',
    '57': '海南全省',
    '61': '四川中南部',
    '62': '四川西、北部',
    '63': '四川东北部',
    '64': '四川东南部',
    '65': '云南东部',
    '66': '云南南部',
    '67': '云南西、北部',
    '71': '陕西中北部（铜川除外）',
    '72': '陕西南部、铜川等地',
    '73': '甘肃中北部、内蒙阿拉善盟一部',
    '74': '甘肃东、南部',
    '75': '宁夏全区、内蒙阿拉善盟一部',
    '81': '青海全省',
    '83': '北疆',
    '84': '南疆',
    '85': '西藏全区',
}


def main():
    input_path = r"d:\\analyzer_out.txt"
    output_path = r"d:\\zip_output.csv"

    dict_counter = {k: 0 for k in zip_region_mapping}  # 真正用来统计地域的计数器
    total_line_num = 0  # 文件一共多少行
    valid_line_num = 0  # 有效邮编一共多少行
    unprocessed_line_num = 0  # 在有效邮编中，还有多少行没处理

    with open(input_path, mode='r', encoding='utf8') as f:
        while True:
            # 读到文件结束为止
            line = f.readline()
            if line == "":
                break
            line = line.strip("\n ")
            total_line_num += 1

            # 不是6位的邮政编码就不计入了
            if not len(line) == 6:
                continue

            # 开始进行区域统计
            if line[:2] in dict_counter:
                dict_counter[line[:2]] += 1
                valid_line_num += 1
            else:
                unprocessed_line_num += 1

    # 最终呈现的时候使用地名而不是邮政编码前两位
    dict_counter = {zip_region_mapping[k]: v for k, v in dict_counter.items()}
    # 按出现频率排序
    list_counter = [(k, v) for k, v in dict_counter.items()]
    list_counter.sort(key=lambda _: _[1], reverse=True)

    # 输出统计结果
    with open(output_path, mode='w', encoding='gb2312') as f:
        for x in list_counter:
            f.write("{},{}\n".format(x[0], x[1] / (valid_line_num - unprocessed_line_num)))
    print("total: {}, valid: {}, unprocessed: {}".format(total_line_num, valid_line_num, unprocessed_line_num))


if __name__ == '__main__':
    main()
