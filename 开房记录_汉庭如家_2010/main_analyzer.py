import os
import sys
from 开房记录_汉庭如家_2010.address_parser import AddressFilterLevelOne


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


def address_parser_level_1(work_dir: str, output_path: str, enable_dict_collector=False):
    """
    :return:
    """
    line_counter = 0
    f = open(output_path, 'w', encoding='utf8')

    if enable_dict_collector is True:
        dict_collector = DictCollector()

    for line_num, line in enumerate(reader(work_dir)):
        # if not i % 17237 == 0:
        #     continue

        try:
            col_Name, col_CardNo, col_Descriot, col_CtfTp, col_CtfId, \
            col_Gender, col_Birthday, col_Address, col_Zip, col_Dirty, \
            col_District1, col_District2, col_District3, col_District4, col_District5, \
            col_District6, col_FirstNm, col_LastNm, col_Duty, col_Mobile, \
            col_Tel, col_Fax, col_EMail, col_Nation, col_Taste, \
            col_Education, col_Company, col_CTel, col_CAddress, col_CZip, \
            col_Family, col_Version, col_id = line.split(",")
        except ValueError as err:
            # print("row_{}, {}, {}".format(i, len(line.split(",")), line), file=sys.stderr)
            continue
        else:
            # print("row_{}, {}".format(i, line))
            pass

        if address_filter.filter(col_Address) is True:
            print(col_Address, file=f)

            # global_counter += 1

    print(line_counter)
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

    def get_collection_result(self):
        """
        返回收集器的当前计数结果
        :return:
        """
        return str(self._info_dict)


def main():
    address_parser_level_1(work_dir=r"D:\2000W", output_path=r"d:\\address_2.txt", enable_dict_collector=False)


if __name__ == '__main__':
    address_filter = AddressFilterLevelOne()
    main()
