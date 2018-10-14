FROM python:3.6

ADD main_bot_script.py /

RUN python -m pip install discord.py==0.16.12

CMD [ "python", "./main_bot_script.py" ]