cmake_minimum_required(VERSION 3.0)

project(${lib})
set(HEADERS lib.h)
set(SOURCES lib.cpp)

add_library(lib SHARED ${HEADERS} ${SOURCES})
