FROM python:3

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 3000

# run the command
CMD ["pip", "install", "--upgrade", "pip"]
CMD ["python", "-u", "./src/app.py"]