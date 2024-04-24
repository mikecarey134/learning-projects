FROM ubuntu:23.10
WORKDIR /server
EXPOSE 2456/tcp 2456/udp
EXPOSE 2457/tcp 2457/udp
EXPOSE 2458/tcp 2458/udp
RUN apt update
RUN apt install software-properties-common -y
RUN add-apt-repository multiverse
RUN dpkg --add-architecture i386 
RUN apt update
#RUN apt install steamcmd -y 1
#RUN steamcmd +force_install_dir /server +login anonymous +app_update 896660 validate +exit
#COPY start_vh_server.sh /server
#RUN chmod +x /server/start_vh_server.sh 
#ADD Valheim /Valheim
CMD ./start_vh_server.sh

