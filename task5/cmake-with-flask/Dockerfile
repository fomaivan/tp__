FROM gcc:latest
COPY . /opt/techprog  
WORKDIR /opt/techprog/build
RUN apt-get update && \
    apt-get install -y cmake

RUN cmake .. && \
    cmake --build . && \
    make
