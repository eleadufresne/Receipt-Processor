# python image
FROM python

# install the requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy the code to the container
COPY . .

# expose the port 5000 to the world (outside the container)
EXPOSE 5000

# run app.py when the container launches
CMD ["python", "app.py"]