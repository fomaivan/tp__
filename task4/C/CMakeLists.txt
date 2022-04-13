project(C)

link_libraries(CTestExe gtest_main ClassLib)
add_executable(CTestExe tests.cpp main_test.cpp)
include_directories(CTestExe PRIVATE ${Task4_SOURCE_DIR})
add_executable(C main.cpp)

link_libraries(C ClassLib)
include_directories(C PRIVATE ${Task4_SOURCE_DIR})
