FROM gcc:latest

RUN apt-get update && apt-get install -y cmake

COPY . ./opt/techprog

WORKDIR /opt/techprog

RUN cmake . && cmake --build .
