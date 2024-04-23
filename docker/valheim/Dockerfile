FROM steamcmd/steamcmd:debian-12
WORKDIR /Valheim
EXPOSE 2456/tcp 2456/udp
RUN apt update
RUN steamcmd +force_install_dir /Valheim +login anonymous +app_update 896660 validate +exit
COPY start_vh_server.sh /Valheim
RUN chmod +x /Valheim/start_vh_server.sh

CMD ./Valheim/start_vh_server.sh

