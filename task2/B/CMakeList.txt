cmake_minimum_required(VERSION 3.0)

project(${lib_tp})
set(HEADERS lib.h)
set(SOURCES lib.cpp)

add_executable(${lib_tp} ${HEADERS} ${SOURCES})
