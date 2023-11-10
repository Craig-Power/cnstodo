# Base Image
FROM python:3.10
# set variables

ENV HOME=/app PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 VIRTUAL_ENV=/env

RUN mkdir p $HOME
WORKDIR $HOME
COPY . $HOME

# Install dependencies
RUN python -m venv $VIRTUAL_ENV && pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000
# Shouldn't be run as insecure, but necessary due to known issue with CSS files not loading from static directory
CMD ["python", "manage.py", "runserver", "--insecure", "0.0.0.0:8000"]
