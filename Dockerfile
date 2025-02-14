FROM yonggan/docker-ffmpeg

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DISCORD_TOKEN REPLACE_THIS_TOKEN

CMD [ "python", "./bot.py"]
