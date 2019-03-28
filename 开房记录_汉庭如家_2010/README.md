### 汉庭如家2000万条开房记录

### Download

see ./download/download.txt

### ParseResult

一共`20051428`行，不过似乎有`11660`行的数据不太规范，其实里面还是有信息的。
方便起见，这11660行数据不予考虑，即被清洗掉。

1. `Name`字段
    就是名字哒!

2. `CardNo`字段
    1. 看起来没啥意义的说。
    2. 数据分布稀疏且不太均匀，出现频率为`10115/20039768(0.050%)`。
        * 前1000W行里有546行存在此字段，均以`H`或`G`开头，随后辅以7位数字。
        * 后1000W行里有9569行存在此字段，大部分为10位纯数字。

3. `Descriot`字段
    1. 估计是`Description`的缩写。。。`Description -> Descript -> Descriot`(笑)。
    要知道，qwerty键盘上的"P"和"O"键位很近的说。
    2. 数据分布稀疏，出现频率为`20357/20039768(0.102%)`。
        * 主要出现字样为价格/客房类型/服务类型，对客人特殊情况的描述等

 , `CtfTp`, CtfId,
            Gender, Birthday, Address, Zip, Dirty, \
            District1, District2, District3, District4, District5, \
            District6, FirstNm, LastNm, Duty, Mobile, \
            Tel, Fax, EMail, Nation, Taste, \
            Education, Company, CTel, CAddress, CZip, \
            Family, Version, id

### References

1. [https://blog.csdn.net/qq_36561697/article/details/82356106](https://blog.csdn.net/qq_36561697/article/details/82356106)