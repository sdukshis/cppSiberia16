from conans import ConanFile, CMake
import os

class FooConan(ConanFile):
    name = "foo"
    version = "0.0.1"
    requires = "gizmo/0.0.1@demo/testing"
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
        self.cpp_info.libs = ["foo"]

