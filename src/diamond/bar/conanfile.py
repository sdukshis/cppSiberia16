from conans import ConanFile, CMake
import os

class FooConan(ConanFile):
    name = "bar"
    version = "0.0.2"
    requires = "gizmo/0.1.1@demo/testing"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "*"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="")
        self.copy("*.a", dst="", src="")

    def package_info(self):
        self.cpp_info.libs = ["bar"]

