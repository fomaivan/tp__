cmake_minimum_required(VERSION 3.0)

project(library)

set(HEADER lib.h)
set(SOURCE lib.cpp)
add_library(lib SHARED ${SOURCE} ${HEADER})
