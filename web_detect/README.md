# web质量探测

## 安装环境
```
sudo pip install pycurl
```
## 模块常用方法说明
```
close()方法，对应libcurl包中的curl_easy_cleanup方法，无参数，实现关闭、回收curl对象
perform()方法，对应libcurl包中的curl_easy_perform方法，无参数，实现curl对象请求提交
setopt(option, value)方法，对应libcurl包中的curl_easy_setopt方法，参数option是通过libcurl的常量来指定的，参数value的值会依赖option，可以是一个字符串、整数、长整数、文件对象列表或者函数。
```

