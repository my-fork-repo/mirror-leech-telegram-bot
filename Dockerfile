FROM anasty17/mltb:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt --break-system-packages
RUN pip3 install speedtest-cli
COPY . .

RUN bash start.sh
