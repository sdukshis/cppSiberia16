cmake_minimum_required(VERSION 2.8.12)

project(bar CXX)

include(${CMAKE_SOURCE_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(bar bar.cpp bar.h)

target_link_libraries(bar ${CONAN_LIBS})
