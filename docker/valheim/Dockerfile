FROM debian:bookworm-slim
WORKDIR /server
EXPOSE 2456/tcp 2456/udp
#RUN steamcmd +force_install_dir /server +login anonymous +app_update 896660 validate +exit
#COPY start_vh_server.sh /server
#RUN chmod +x /server/start_vh_server.sh 
#ADD Valheim /Valheim
CMD ./start_vh_server.sh

