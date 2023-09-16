cmake_minimum_required (VERSION 2.8.11)
project (hana_learn)

set(CMAKE_C_FLAGS "-O3 -std=c++11 -fPIC")
set(CMAKE_CXX_FLAGS "-O3 -std=c++11 -Wall -Wextra -fPIC -Wno-sign-compare")

add_subdirectory (hanabi_lib)

add_subdirectory (hana_learn/hanabi_lib)
add_subdirectory (hana_learn)
