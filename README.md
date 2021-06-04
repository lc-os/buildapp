### 说明
* 一个支持 Flutter、ReactNative、原生 Android、iOS 的打包工具
* iOS/Android上传到蒲公英
* Android上传阿里云
* iOS上传到TestFlight
* 发送消息到钉钉
* 自动读取版本号来重命名上传包的文件名
* [这里查看运行效果图](https://github.com/lc-os/buildapp/raw/master/doc/images/img1.png)

### 安装
使用Python3编写，所以得自行安装相关环境<br/>
目前项目只在Mac上面跑过 <br/>
安装依赖 `pip3 install requests`  `pip3 install oss2`<br/>
或者通过 `pipenv shell` <br/>
我不是Python大神，如果有安装问题大家自行根据错误来解决吧。
### 配置*
打开src/config/config.py进行配置 <br/>
最低配置是把蒲公英配置上，其它不配置的也行。 <br/>
*Android需要配置keystore <br/>
*iOS需要配置导出plist文件(放到项目中即可，然后在 config.py中配置下文件名即可) <br/>
*以上两项为必须配置，网上都相关教程，自行配置
### 使用
克隆本项目到你的工程中(也可以是其它地方) 然后运行： <br/>
 `python3 ./buildapp/main.py` // 自动从当前目录然or上级查找项目 <br/>
 `python3 main.py 你的项目路径` // 或者指定目录路径 <br/>
根据提示选择下面的打包方式<br/>
 11. apk ➣ 蒲公英 ➣ 钉钉<br/>
 12. apk ➣ 阿里云 ➣ 钉钉<br/>
 21. ipa ➣ 蒲公英 ➣ 钉钉<br/>
 22. ipa ➣ TestFlight ➣ 钉钉
基于大佬版本改：<br/>
11. apk ➣ 蒲公英 ➣ 钉钉 （xm xh）<br/>
12. 蒲公英失败再次上传 ➣ 钉钉 （xm  xh）<br/>
13. apk ➣ 打开文件夹<br/>
21. ipa ➣ 蒲公英 ➣ 钉钉<br/>
22. ipa ➣ AppStore ➣ 钉钉<br/>
23. ipa ➣ 本地文件夹<br/>
24. ipa ➣ 本地路径 ➣ AppStore
### 相关文章
 1. 懒人plist在doc中（请自行修改teamId）
 2. 除了src/config/config.py需要配置的地方 其他需要更改的地方看图
 ![我是图1](https://github.com/lc-os/buildapp/raw/master/doc/images/img2.png)
 ![我是图二](https://github.com/lc-os/buildapp/raw/master/doc/images/img3.png)
 

