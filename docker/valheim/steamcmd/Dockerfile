FROM steamcmd/steamcmd:debian-12
WORKDIR /server
RUN steamcmd +force_install_dir /server +login anonymous +app_update 896660 validate +exit
COPY start_vh_server.sh /server
RUN chmod +x /server/start_vh_server.sh
