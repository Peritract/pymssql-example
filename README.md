# PyMSSQL example

A small example of using `pymssql` inside a Lambda function.

## Installation

Don't install anything; do it all through Docker.

## Setup

- Build the image with `bash build-image.sh`
- Run a container locally with `bash run-container.sh`
- In a second terminal, check the container behaves as expected through `bash test-container.sh`

## Benefits

- No need for `sqlalchemy`
- Familiar cursor syntax
- Bulk insertion
- No awkward transition to the cloud (just ECR the final image)
  