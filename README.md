# DataMigration
一款基于python+PySimpleGUI的小工具，<br>
可以减少你将数据由 ***MongoDB*** 迁移到 ***Mysql*** 的工作量。


## 作用/使用指南
- 修改conf.ini文件中的数据库配置，打开软件
- 修改要使用的表名，左边为MongoDB，右边为Mysql
- 修改置信度，(0,100]
- 点击“生成转换语句”，软件会自动以获取mysql表中的字段名，并作为基准，通过置信度一一匹配MongoDB表中的字段，生成Mongo的match语句。

```
 $match:{'content.flowType':'grantExamine'}
```

## 运行方式
1.  源码运行:<br>
修改conf.ini文件中的数据库账号密码等配置<br>
运行 ***DataMigrationGUI.py*** 文件


2. Windows X86:<br>
下载发布页的压缩包，同样修改conf.ini文件<br>
运行 ***DataMigration_MLN.exe***



## 截图
![](https://cdn.jsdelivr.net/gh/mmmlllnnn/blog-img/migration-2.png)

![](https://cdn.jsdelivr.net/gh/mmmlllnnn/blog-img/migration-1.png)


