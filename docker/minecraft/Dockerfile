FROM openjdk:23-bookworm
WORKDIR /server
RUN apt update 
RUN apt install wget
RUN wget https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar
EXPOSE 25565/tcp 25565/udp
COPY eula.txt /server
COPY ops.json /server

CMD java -Xmx1024M -Xms1024M -jar server.jar

