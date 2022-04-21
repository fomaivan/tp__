FROM gcc:latest
WORKDIR /opt/techprog/build
COPY . ../
RUN apt-get update && \
    apt-get install -y cmake
RUN cmake .. && \
    cmake --build .