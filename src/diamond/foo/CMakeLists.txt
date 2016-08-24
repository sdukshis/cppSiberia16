cmake_minimum_required(VERSION 2.8.12)

project(foo CXX)

include(${CMAKE_SOURCE_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(foo foo.cpp foo.h)

target_link_libraries(foo ${CONAN_LIBS})
