# Use the official Python image as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /tests

# Copy the current directory contents into the container at /tests
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run tests when the container launches
CMD ["python", "-m", "unittest", "discover"]
