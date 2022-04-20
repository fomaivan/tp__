FROM gcc:latest
RUN useradd --user-group --create-home --no-log-init --shell /bin/bash tp2022user
WORKDIR /opt/techprog/build
COPY . ../  
RUN apt-get update && \
    apt-get install -y cmake
RUN cmake .. && \
    cmake --build . && \
    make
USER tp2022user