import os
import sys

from src.project.build import Build
from src.project.project import ProjectType
from src.config.config import *

"""
    in_path : 项目路径 
            1.接收传入的路径
            2.如果没有传入，采用当前路径
            3.如果以上路径不支，查找上线目录
    in_type : 接收传入的类型，不传的话会提示选择
"""

# 处理输入的参数
in_path = ""
in_dd = ""
in_type = ""
ipa_path = ""
for item in sys.argv:
    if os.path.isdir(item):
        in_path = item
    elif "type" in item:
        arr = item.split('=')
        if len(arr) > 1:
            in_type = arr[1].strip(" ")


# 1. 采用传入的目录
if in_path:
    # 切换目录
    os.chdir(in_path)
    build = Build()
else:
    # 2. 采用当前目录
    build = Build()
    if build.project.project_type == ProjectType.Unknown:
        # 3. 采用上级目录
        os.chdir("..")
        build = Build()

if build.project.project_type == ProjectType.Unknown:
    print("项目路径错误")
    exit(1)

# 项目路径正确
print("你的项目为：", build.project.project_type.value)


# 如果没有传入就提醒输入
if not in_type:
    s = input("""请输入要操作的类型：
  11. apk ➣ 蒲公英 ➣ 钉钉 （xm xh）
  12. 蒲公英失败再次上传 ➣ 钉钉 （xm  xh）
  13. apk ➣ 打开文件夹
  21. ipa ➣ 蒲公英 ➣ 钉钉
  22. ipa ➣ AppStore ➣ 钉钉
  23. ipa ➣ 本地文件夹
  24. ipa ➣ 本地路径 ➣ AppStore
➜ """)
    in_type = s.strip(" ")
if in_type == "11":
    print("11. apk ➣ 蒲公英 ➣ 钉钉")
    # 传入需要钉钉发送的人
    if not in_dd:
        dd = input("""请输入要钉钉发送的人（可空格拼接）:
      xm. dd ➣ 小明
      xh. dd ➣ 小红
    ➜ """)
    int_dd = dd.strip(" ")
    build.android_release_to_pgy(in_type, int_dd)
elif in_type == "12":
    print("12. 蒲公英再次上传 ➣ 钉钉")
     # 传入需要钉钉发送的人
    if not in_dd:
        dd = input("""请输入要钉钉发送的人（可空格拼接）:
      xm. dd ➣ 小明
      xh. dd ➣ 小红
    ➜ """)
    int_dd = dd.strip(" ")
    build.android_release_to_pgy(in_type, int_dd)
elif in_type == "13":
    print("13. apk ➣ 打开文件")
    build.android_release_to_file()
elif in_type == "21":
    print("21. ipa ➣ 蒲公英 ➣ 钉钉")
    build.ios_ad_hoc_to_pgy()
elif in_type == "22":
    print("22. ipa ➣ AppStore ➣ 钉钉")
    build.ios_release_to_app_store()
elif in_type == "23":
    print("23. ipa ➣ 文件夹 ➣ 签名")
    build.ios_ad_hoc_to_sign()
elif in_type == "24":
    print("24. ipa ➣ AppStore")
    if not ipa_path:
        path = input("""请输入ipa本地路径:
    ➜ """)
    ipa_path = path.strip(" ")
    build.ios_no_build_to_app_store(ipa_path)
else:
    print("你的参数输入有误:", in_type)




