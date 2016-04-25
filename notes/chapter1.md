####关于URLError和HTTPError
下面书书中的代码：

    from urllib.request import urlopen
    from urllib.error import HTTPError
    from bs4 import BeautifulSoup

    def getTitle(url):
        try:
            html = urlopen(url)
        except HTTPError:
            return None
        try:
            bsObj = BeautifulSoup(html.read(), "lxml")
            title = bsObj.body.h1
        except AttributeError:
            return None
        return title

    title = getTitle("http://www.pythonscraping.com/pages/page1.html")
    if title == None:
        print("Title could not be found!")
    else:
        print(title)

  但是，这里面有个错误。作者解释说，`urlopen(url)`函数当`url`页面找不到时候会抛出`HTTPError`异常，而当服务器找不到时会返回`None`。  
事实上，当服务器找出现问题的时候，并不会返回`None`，而是抛出`URLError`异常。`HTTPError`是`URLError`的子类。  
因而，代码中应当使用`URLError`，这样能捕获`HTTPError`和`URLError`。
