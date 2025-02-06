# python image
FROM python

# set the working directory in the container
WORKDIR /app

# copy the code to the 'app' dir of the container
COPY . .

# install the requirements
RUN pip3 install -r requirements.txt

# expose the port 5000 to the world (outside the container)
EXPOSE 5000

# run app.py when the container launches
CMD ["python", "app.py"]