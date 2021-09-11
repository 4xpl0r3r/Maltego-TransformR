# Maltego Transform的开源替代版

**由于Maltego的Entity复制限制，终止此项目**

R表示Replacer

使用CSV作为交换格式，entity和links文件分开作为标准

由于Maltego的BUG，目前仅支持单类型Entity进行导入

## csv交换格式规范

maltego machine readable format

## 内部数据交换

Entity、Links使用Dict Array作为内部对象，方便使用，csvIO直接使用DictReader

Entity官网文档：https://docs.maltego.com/support/solutions/articles/15000035722-introduction-to-maltego-standard-entities
EntityID目前来看是会选择一个基地址，然后进行增加，那我自己也可以随机生成一个基地址，随机并且不落在
视作base36编码，并且随机在base36的2000000000000到2i00000000000之间生成一个基地址，并且确保不在原有ID的上下100000(数值)之间

TransformR脚本应维护两个表，Entity表和Link表并最终传递同样的名称参数导出

## entityDB 规范

第一列为类型名称，剩下的列为键

## 代码规范

类所有首字母大写，变量驼峰命名法，文件名驼峰命名法，函数驼峰命名法