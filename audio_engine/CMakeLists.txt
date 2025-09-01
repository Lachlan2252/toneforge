cmake_minimum_required(VERSION 3.10)
project(audio_engine)

add_library(audio_engine src/audio_engine.cpp)
target_include_directories(audio_engine PUBLIC include)
