# Python implementation of analyzere problem

### Docker

- Build the Docker image: `docker build -t solution .`
- Run the Docker container with the command: `cat input | docker run -i --rm solution:latest compute 100 5000`

### Non Docker

- Run the program with the command: `cat input.txt | python ./compute.py 100 500`

Make sure in both scenarios, you have the input.txt file in the same directory as the python file or the Dockerfile.