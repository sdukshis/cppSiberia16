from conans import ConanFile, CMake
import os

class GizmoConan(ConanFile):
    name = "gizmo"
    version = "0.1.1"
    settings = "os", "compiler", "build_type", "arch"
    exports = "*"

    def build(self):
        cmake = CMake(self.settings)

    def package(self):
        self.copy("*.h", dst="include", src="include")
