cmake_minimum_required(VERSION 3.0)

include_directories(include)

set(CMAKE_C_COMPILER ${TOOLCHAIN}/aarch64-linux-gnu-gcc)
set(CMAKE_CXX_COMPILER ${TOOLCHAIN}/aarch64-linux-gnu-g++)


project(SimpleLibrary)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${SimpleLibrary_SOURCE_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${SimpleLibrary_SOURCE_DIR}/lib)

set(CMAKE_INSTALL_RPATH ${CMAKE_INSTALL_PREFIX}/lib)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

add_subdirectory(src)
add_executable(Main main.cpp)
add_executable(MainLib main_lib.cpp)

set_property(TARGET MainLib PROPERTY PUBLIC_HEADER "${SimpleLibrary_SOURCE_DIR}/include/buffer.h")

target_link_libraries(MainLib buffer)
install(TARGETS Main DESTINATION ${CMAKE_INSTALL_PREFIX}/bin)
install(TARGETS MainLib DESTINATION ${CMAKE_INSTALL_PREFIX}/bin PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_PREFIX}/include)
