FROM ubuntu:23.10

# Set environment variables
ENV USER root
ENV HOME /root

WORKDIR $HOME
EXPOSE 2456/tcp 2456/udp
EXPOSE 2457/tcp 2457/udp
EXPOSE 2458/tcp 2458/udp
RUN apt update

# Insert Steam prompt answers
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN echo steam steam/question select "I AGREE" | debconf-set-selections \
 && echo steam steam/license note '' | debconf-set-selections

RUN apt install software-properties-common -y
RUN add-apt-repository multiverse
ARG DEBIAN_FRONTEND=noninteractive
RUN dpkg --add-architecture i386 
RUN apt install libpulse-dev -y
RUN apt install libatomic1 -y
RUN apt install libc6 -y
RUN apt update
RUN apt install -y --no-install-recommends ca-certificates locales steamcmd
RUN ln -s /usr/games/steamcmd /usr/bin/steamcmd

# Update SteamCMD and verify latest version
RUN steamcmd +quit

# Fix missing directories and libraries
RUN ln -s $HOME/.steam/steamcmd/linux32 $HOME/.steam/sdk32 \
 && ln -s $HOME/.steam/steamcmd/linux64 $HOME/.steam/sdk64 \
 && ln -s $HOME/.steam/sdk32/steamclient.so $HOME/.steam/sdk32/steamservice.so \
 && ln -s $HOME/.steam/sdk64/steamclient.so $HOME/.steam/sdk64/steamservice.so



#RUN apt install steamcmd -y 1
#RUN steamcmd +force_install_dir /server +login anonymous +app_update 896660 validate +exit
#COPY start_vh_server.sh /server
#RUN chmod +x /server/start_vh_server.sh 
#ADD Valheim /Valheim
WORKDIR /server
CMD ./start_vh_server.sh

