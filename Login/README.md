先获取cookie 然后可通过 urllib2来传递cookie来实现对网址的访问
weibo cookie获取参考博客：http://www.jianshu.com/p/816594c83c74
```
session = requests.Session()
res = session.post(login_Url, data=postData)
return_str = res.content.decode('gbk')
info = json.loads(return_str)
info['retcode'] == "0"  success
```
postData
```
cdult	3
domain	sina.com.cn
encoding	UTF-8
entry	sso
from	null
gateway	1
nonce	QAF8TC
pagerefer	http://login.sina.com.cn/sso/login.php?url=https%3A%2F%2Flogin.sina.com.cn%2Fsignup%2Fsignin.php%3Fentry
%3Dsso&_rand=1489914354.2146&gateway=1&service=sso&entry=sso&useticket=0&returntype=META&sudaref=&_client_version
=0.6.20
prelt	107
pwencode	rsa2
returntype	TEXT
rsakv	1330428213
savestate	30
servertime	1489914391
service	sso
sp xxxxxx	
sr	1440*900
su	xxxxxxxxz
useticket 0
vsnf	1
```
得到cookie后访问
```
requests.get(signal_page, cookies=tmp_cookie)
```
参考github 廖大神 https://github.com/tingyunsay/weiboSpider_tingyun
