cmake_minimum_required(VERSION 3.1)

if(ARM_BUILD)
	set(CMAKE_SYSTEM_NAME Linux)
	set(CMAKE_SYSTEM_PROCESSOR arm)
         set(CMAKE_C_COMPILER ${TOOLCHAIN}/arm-linux-gnueabihf-gcc)
	set(CMAKE_CXX_COMPILE ${TOOLCHAIN}/arm-linux-gnueabihf-g++)
endif(ARM_BUILD)

project(SimpleLibrary)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${SimpleLibrary_SOURCE_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${SimpleLibrary_SOURCE_DIR}/bin)
set(CMAKE_INSTALL_RPATH ${CMAKE_INSTALL_PREFIX}/lib)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
add_executable(Main main_first.cpp)
add_executable(MainLib main_second.cpp)

install(TARGETS Main DESTINATION ${CMAKE_INSTALL_PREFIX}/bin)
install(TARGETS MainLib DESTINATION ${CMAKE_INSTALL_PREFIX}/bin PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_PREFIX}/include)

