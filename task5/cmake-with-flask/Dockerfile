FROM gcc:latest

WORKDIR /opt/techprog

COPY . .

RUN apt-get update && apt-get install -y build-essential cmake

RUN cmake . && make

RUN useradd -d /opt/techprog tp2022user

USER tp2022user