# Same thing than the 'server' Dockerfile.
FROM python:latest

# Same thing than the 'server' Dockerfile.
# We import 'client.py' in '/client/' folder.
COPY datanode1.py /datanode1/

# I would like to introduce something new, the 'WORKDIR' command.
# This command changes the base directory of your image.
# Here we define '/client/' as base directory (where all commands will be executed).
WORKDIR /datanode1/