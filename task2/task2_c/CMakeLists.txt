cmake_minimum_required(VERSION 3.22)
project(Thread_lab_3 C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)

find_package(OpenMP REQUIRED)
add_compile_options(-Wno-unused-result)

add_library(
        Thread_lab_3
        SHARED
        task2.c
        task2.h
)

target_link_libraries(Thread_lab_3 PUBLIC m)
target_link_libraries(Thread_lab_3 PUBLIC OpenMP::OpenMP_C)

set(LIBRARY_OUTPUT_PATH "../libs")

if(WIN32)
    add_custom_command(TARGET Thread_lab_3 POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E remove "${LIBRARY_OUTPUT_PATH}/lib${PROJECT_NAME}.dll.a"
    )
endif()