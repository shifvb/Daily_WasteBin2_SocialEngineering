import os
import sys
import datetime


def reader(work_dir):
    """
    read csv files from folder
    :param work_dir:
    :return:
    """
    # get csv file paths
    paths = [os.path.join(work_dir, _) for _ in os.listdir(work_dir)]
    paths.sort(key=lambda _: int(os.path.split(_)[-1].split(".")[0].split("-")[0].strip("最后|w|W")))

    # read csv file
    for path in paths:
        print("reading {}...".format(path), file=sys.stderr)
        f = open(path, encoding='utf8')
        f.readline()  # remove the first line
        while True:
            line = f.readline()
            if not line:  # reach the end of one file
                break
            yield line.strip("\n")
        f.close()


def main_analyzer(work_dir: str, output_path: str, enable_dict_collector=False):
    """
    :return:
    """
    line_counter = 0
    f = open(output_path, 'w', encoding='utf8')

    if enable_dict_collector is True:
        dict_collector = DictCollector()

    for line_num, line in enumerate(reader(work_dir)):

        # 用来稀疏输入的
        # if not line_num % 17237 == 0:
        #     continue

        try:
            col_Name, col_CardNo, col_Descriot, col_CtfTp, col_CtfId, \
            col_Gender, col_Birthday, col_Address, col_Zip, col_Dirty, \
            col_District1, col_District2, col_District3, col_District4, col_District5, \
            col_District6, col_FirstNm, col_LastNm, col_Duty, col_Mobile, \
            col_Tel, col_Fax, col_EMail, col_Nation, col_Taste, \
            col_Education, col_Company, col_CTel, col_CAddress, col_CZip, \
            col_Family, col_Version, col_id = line.split(",")
        except ValueError:
            # print("row_{}, {}, {}".format(i, len(line.split(",")), line), file=sys.stderr)
            continue
        else:
            # print("row_{}, {}".format(i, line))
            pass

        # 如果符合一定的条件，就把这个字段输出看看
        col_to_analyze = col_CtfTp
        if col_to_analyze:
            # print(col_to_analyze, file=f)
            line_counter += 1
            dict_collector.collect(col_to_analyze.split(" ")[0])

    print(line_counter)
    # 按降序输出统计结果
    if enable_dict_collector is True:
        for k, v in dict_collector.get_collection_result()[:200]:
            print("{},{}".format(k, v))

    # 关闭打开的文件
    f.close()


class InformationCollector(object):
    def __init__(self):
        pass

    def collect(self, info: object):
        pass

    def destruct(self):
        pass

    def get_collection_result(self):
        pass


class DictCollector(InformationCollector):
    def __init__(self):
        """
        用字典对比较容易重复出现的数据进行计数，比如性别之类的
        """
        super().__init__()
        self._info_dict = dict()

    def collect(self, info: object):
        """
        传入信息，本收集器会收集传入的信息
        拿性别举例子，如果传入的是字符串"男"，那么本收集器的相应计数器就会加1。由于采用了字典（dict, hashmap）进行记录，
        传入的info必须可以被哈希。
        :param info: 传入的要被计数的信息
        """
        if info not in self._info_dict:
            self._info_dict[info] = 0
        self._info_dict[info] += 1

    def destruct(self):
        """
        销毁操作
        :return:
        """
        del self._info_dict

    def get_collection_result(self) -> list:
        """
        返回收集器的当前计数结果
        :return:
        """
        _list_counter = [(k, v) for k, v in self._info_dict.items()]
        _list_counter.sort(key=lambda _: _[1], reverse=True)
        return _list_counter


def main():
    main_analyzer(work_dir=r"D:\2000W", output_path=r"d:\\analyzer_out.txt", enable_dict_collector=True)


if __name__ == '__main__':
    main()
