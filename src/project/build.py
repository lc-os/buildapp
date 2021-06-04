from src.android.android_build import AndroidBuild
from src.flutter.flutter_build import FlutterBuild
from src.ios.ios_build import IOSBuild
from .project import Project, ProjectType


class Build:
    def __init__(self):
        self.flutter_build = FlutterBuild()
        self.project = Project()

    # 上传 debug 包到蒲公英
    def android_debug_to_pgy(self):
        pass

    # 上传 release 包到蒲公英
    def android_release_to_pgy(self, in_type, int_dd):
        build = AndroidBuild(self.flutter_or_rn_path("android"), self.get_outputs_apk_dir())
        if self.project.project_type == ProjectType.Flutter:
            build.project.version_name = self.flutter_build.project.version_name
            build.project.version_code = self.flutter_build.project.version_code
        try:
            build.build_to_pgy(in_type,int_dd)
        except Exception as e:
            print(e)
            exit(1)
    
     # 上传 release 包到蒲公英
    def android_release_to_file(self):
        build = AndroidBuild(self.flutter_or_rn_path("android"), self.get_outputs_apk_dir())
        if self.project.project_type == ProjectType.Flutter:
            build.project.version_name = self.flutter_build.project.version_name
            build.project.version_code = self.flutter_build.project.version_code
        try:
            build.build_to_file()
        except Exception as e:
            print(e)
            exit(1)


    # 上传 release 包到阿里 oss
    def android_release_to_oss2(self):
        build = AndroidBuild(self.flutter_or_rn_path("android"), self.get_outputs_apk_dir())
        if self.project.project_type == ProjectType.Flutter:
            build.project.version_name = self.flutter_build.project.version_name
            build.project.version_code = self.flutter_build.project.version_code
        try:
            build.build_to_ali_oss()
        except Exception as e:
            print(e)
            exit(1)

    # 上传 debug 包到蒲公英
    def ios_debug_to_gpy(self):
        pass

    # 上传 adhoc 包到蒲公英
    def ios_ad_hoc_to_pgy(self):
        build = IOSBuild(self.flutter_or_rn_path("ios"))
        if self.project.project_type == ProjectType.Flutter:
            build.project.version_name = self.flutter_build.project.version_name
            build.project.version_code = self.flutter_build.project.version_code
            self.flutter_build.build_ios()
        try:
            build.build_to_pgy()
        except Exception as e:
            print(e)
            exit(1)

     # 上传hoc包到苹果
    def ios_ad_hoc_to_sign(self):
        build = IOSBuild(self.flutter_or_rn_path("ios"))
        if self.project.project_type == ProjectType.Flutter:
            build.project.version_name = self.flutter_build.project.version_name
            build.project.version_code = self.flutter_build.project.version_code
            self.flutter_build.build_ios()
        try:
            build.ios_ad_hoc_to_sign()
        except Exception as e:
            print(e)
            exit(1)

    # 上传正式包到苹果
    def ios_release_to_app_store(self):
        build = IOSBuild(self.flutter_or_rn_path("ios"))
        if self.project.project_type == ProjectType.Flutter:
            build.project.version_name = self.flutter_build.project.version_name
            build.project.version_code = self.flutter_build.project.version_code
            self.flutter_build.build_ios()
        try:
            build.build_to_app_store()
        except Exception as e:
            print(e)
            exit(1)
     # 上传正式包到苹果
    def ios_no_build_to_app_store(self, ipa_path):
        build = IOSBuild(self.flutter_or_rn_path("ios"))
        try:
            build.no_build_to_app_store(ipa_path)
        except Exception as e:
            print(e)
            exit(1)

    # 处理 flutter or rn 原生工程路径
    def flutter_or_rn_path(self,  path):
        if self.project.project_type == ProjectType.ReactNative or self.project.project_type == ProjectType.Flutter:
            return path
        return "."

    # 获取 android apk输出目录
    def get_outputs_apk_dir(self):
        if self.project.project_type == ProjectType.Flutter:
            return "build/app/outputs/apk/release"
        elif self.project.project_type == ProjectType.ReactNative:
            return "android/app/build/outputs/apk/release"
        else:
            return "app/build/outputs/apk/release"


