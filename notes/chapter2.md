#第二章学习笔记

###一、进行HTML解析前的思考
并不是任何时候都需要进行HTML解析。在开始进行HTML解析前，需要考虑一下是不是真的有必要这么做。  
* 看看有没有“print this page”链接或者有没有手机版页面  
* 查看隐藏在JavaScript中的信息
* 有的时候需要的信息就参在与页面的URL中
* 需要的信息是否能够在其他来源中找到

###二、BeautifulSoup

####1. findAll( )方法
在第一章中使用过的`bsObj.tagName`可以找到`bsObj`中的名为`tagName`的**第一个**实例。而这里的`bsObj.findAll(tagName, tagAttributes)`方法以list形式返回BeautifulSoup对象`bsObj`中名为`tagName`的全部实例。
####2. get_text( )方法
在文档上调用`get_text()`方法，会将文章中全部tag去掉，返回一个只包含文本，没有tag的字符串。
####3. find( )方法和findAll( )方法

####4. BeautifulSoup中的对象（Object）
BeautifulSoup中共有四类对象：
* BeautifulSoup对象
* Tag对象
* NavigableString对象
* Comment对象


####5. 浏览文档树
`find()`和`findAll()`方法可以通过标签名称和标签属性来查找特定的标签。但是如果想要基于标签位置查找特定的标签，就需要一些浏览文档树的方法。

`bsObj.tag.subTag.anotherSubTag`：这个形式可以沿着文档树进行但方向的浏览

如果要基于“树结构”相关概念的浏览，就需要依赖与标签之间的亲属关系：父子、兄弟、祖先、后代等

* 处理子节点和后代节点：  
`children()`  
`descendents()`

* 处理兄弟节点：  
`next_siblings()`：返回位于当前标签之后的所有兄弟节点  
`previous_siblings()`：返回位于当前标签之前的所有兄弟节点  
`next_sibling()`：返回位于当前标签之后的第一个兄弟节点  
`previous_sibling()`：返回位于当前标签之前的第一个兄弟节点

* 处理父节点  
`parent()`

###三、正则表达式


###四、访问标签属性


###五、lambda表达式

