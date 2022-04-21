FROM gcc:latest
RUN apt-get update && \
    apt-get install -y cmake
WORKDIR /opt/techprog/build
COPY . ../
RUN cmake .. && \
    cmake --build .

FROM ubuntu:latest
RUN groupadd -r tp2022user && useradd -r -g tp2022user tp2022user
USER tp2022user
WORKDIR /opt/techprog
