cmake_minimum_required (VERSION 2.8.11)
project (hana_learn)

set(CMAKE_C_FLAGS "-O2 -std=c++11 -fPIC")
set(CMAKE_CXX_FLAGS "-O2 -std=c++11 -fPIC")

add_subdirectory (hana_learn/hanabi_lib)
add_subdirectory (hana_learn)
