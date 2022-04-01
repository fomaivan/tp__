cmake_minimum_required(VERSION 3.0)

project(Task2)

find_package(GTest REQUIRED)

add_subdirectory(B ${PROJECT_SOURCE_DIR}/lib)
target_include_directories(${GTEST_INCLUDE_DIRS})
target_include_directories(A)
target_include_directories(C)
target_include_directories(${PROJECT_SOURCE_DIR})


add_executable(main "C/main.cpp" ${PROJECT_SOURCE_DIR}/A/index.h)
add_executable(CTest "C/main_test.cpp" ${PROJECT_SOURCE_DIR}/A/index.h)

add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/A/index.h COMMAND python3 ${PROJECT_SOURCE_DIR}/A/preparing.py ${PROJECT_SOURCE_DIR}/A)
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

target_link_libraries(main lib)
target_link_libraries(CTest ${GTEST_LIBRARIES} pthread lib)


