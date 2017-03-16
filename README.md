# Scrapy_Demo
# XPATH语法
```
nodename	选取此节点的所有子节点。
/	从根节点选取。
//	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
.	选取当前节点。
..	选取当前节点的父节点。
@	选取属性
```
bookstore	选取 bookstore 元素的所有子节点。
/bookstore	选取根元素 bookstore。
注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！
bookstore/book	选取属于 bookstore 的子元素的所有 book 元素。
//book	选取所有 book 子元素，而不管它们在文档中的位置。
bookstore//book	选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
//@lang	选取名为 lang 的所有属性。
## 选取未知节点
```
*	匹配任何元素节点。
@*	匹配任何属性节点。
node()	匹配任何类型的节点。
```
/bookstore/*	选取 bookstore 元素的所有子元素。
//*	选取文档中的所有元素。
//title[@*]	选取所有带有属性的 title 元素
# Scrapy
相关文档 
http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/overview.html

博客 
http://blog.csdn.net/fennvde007/article/details/19403977
http://blog.csdn.net/elecjack/article/details/51532482
