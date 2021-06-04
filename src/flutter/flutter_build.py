import os

from .project import FlutterProject


class FlutterBuild:
    android_release_dir = "build/app/outputs/apk/release"

    def __init__(self, path="./"):
        self.path = path
        self.project = FlutterProject(path)

    def build_apk(self):
        os.system("fvm flutter clean".format(self.path))
        os.system("fvm flutter pub get".format(self.path))
        if os.system("fvm flutter build apk --release".format(self.path)):
            return True
        return False

    def build_ios(self):
        os.system("fvm flutter clean".format(self.path))
        os.system("fvm flutter pub get".format(self.path))
        if os.system("fvm flutter build ios --release".format(self.path)):
            return True
        return False
