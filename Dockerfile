FROM anasty17/mltb:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt --break-system-packages
RUN pip3 install --force-reinstall --break-system-packages speedtest-cli
RUN pip3 install --break-system-packages yt-dlp==2023.10.13
COPY . .

RUN bash start.sh
