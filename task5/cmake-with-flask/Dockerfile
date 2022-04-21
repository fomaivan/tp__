FROM gcc:latest
RUN mkdir -p /opt/techprog/build
COPY . /opt/techprog
WORKDIR /opt/techprog/build
RUN apt-get update && apt-get install -y cmake
RUN cmake .. && cmake --build .
