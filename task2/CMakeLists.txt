cmake_minimum_required(VERSION 3.0)

project(task2)

find_package(GTest REQUIRED)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -Wall")
set(CMAKE_CXX_STANDARD 17)

add_subdirectory(B ${PROJECT_SOURCE_DIRECTORY}/lib)

include_directories(${GTEST_INCLUDE_DIRECTORIES})
include_directories(A)
include_directories(C)
include_directories(${PROJECT_SOURCE_DIRECTORY})

add_executable(main "C/main.cpp" ${PROJECT_SOURCE_DIRECTORY}/A/index.h)
add_executable(CTest "C/main_test.cpp" ${PROJECT_SOURCE_DIRECTORY}/A/index.h)
add_custom_command(OUTPUT ${PROJECT_SOURCE_DIRECTORY}/A/index.h COMMAND python3 ${PROJECT_SOURCE_DIRECTORY}/A/preparing.py ${PROJECT_SOURCE_DIRECTORY}/A)


set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIRECTORY}/bin)

target_link_libraries(main lib)
target_link_libraries(CTest ${GTEST_LIBRARIES} pthread lib)

target_include_directories(main PUBLIC "${CMAKE_CURRENT_LIST_DIRECTORY}")


