# 检索诊断的本地执行入口

教学索引，非实时学术库。S1/S2 采用真实题名；S3–S5 是构造条目。只用来检验字段、同义词与查询语义，不把命中数当作文献检索结果。

Python 3 标准库，无需安装包。在本目录运行两条原查询：

```bash
python3 search.py --group paper --group reading --group card
python3 search.py --group 'paper|reading' --group 'card|review'
```

每个 --group 内用 | 连接 OR 词，各 group 之间为 AND；默认搜索 title 字段，大小写不敏感子串匹配。可选择 --field keywords。空词不允许。

保存实际输出，与任务中的“已保存结果”比较；随后自行修订并执行一条查询。概念组不等于独立查询分支；只有分别运行的查询才计算独有命中。将本地练习与真实来源审计分开记录。
