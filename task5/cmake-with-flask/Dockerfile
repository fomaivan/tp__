FROM gcc:latest
WORKDIR /opt/techprog/build
COPY . ../
RUN apt-get update && \
    apt-get install -y cmake
RUN cmake .. && \
    cmake --build . && \
    make

#FROM ubuntu:latest
#RUN groupadd -r tp2022user && useradd -r -g tp2022user tp2022user
#USER tp2022user
#WORKDIR /opt/techprog
