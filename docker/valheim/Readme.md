#Valheim Server

-To get the latest server code build and deploy the steam cmd docker image by running build.sh and run.sh in steamcmd/

-After running steamcmd container only!!!

-Build valheim server using build.sh and run.sh

-Check its running in Yacht

-Note: both steamcmd and valheim containers use the same /server volume which allows steam cmd to pull latest server update patches

-Cleanup: Remove all images associated with valheim and steamcmd and delete valheim:/server volume
