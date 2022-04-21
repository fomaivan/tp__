FROM gcc:latest
#RUN useradd --user-group --create-home --no-log-init --shell /bin/bash tp2022user
RUN apt-get update && \
    apt-get install -y cmake && \
    cmake --build .
COPY . /opt/techprog
WORKDIR /opt/techprog/build
RUN cmake ../src && \
    cmake --build . && \
    CTEST_OUTPUT_ON_FAILURE=TRUE cmake --build . 
#RUN cmake .. && \
#    cmake --build .
#RUN make
#USER tp2022user