cmake_minimum_required(VERSION 2.8.12)

project(foobar CXX)

include(${CMAKE_SOURCE_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(foobar foobar.cpp)

target_link_libraries(foobar ${CONAN_LIBS})
