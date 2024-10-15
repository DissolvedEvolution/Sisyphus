# Step 1: Base image
FROM python:3.9-slim

# Step 2: Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Step 3: Set working directory in the container
WORKDIR /app

# Step 4: Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the project files into the container
COPY . .

# Step 6: Expose the Jupyter port
EXPOSE 8888

# Step 7: Command to run Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
