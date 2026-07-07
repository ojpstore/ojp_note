---
notion-id: 1e4b8e19-0da6-4b2e-8f49-7e7e03443d1a
base: "[[Docker.base]]"
최종 편집 일시: 2024-03-21T16:01:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
```docker
name: Build docker container (Docker Hub)
on:
  push:
    branches:
      - main

jobs:
  build:
    name: Build image
    runs-on: ubuntu-latest
    container:
      image: catthehacker/ubuntu:act-latest # The Docker image to use as the container
    # strategy: # Strategy for the job execution
    #   matrix: # Allows running jobs with different variations
    #     arch: [amd64, arm64] # Variations of architecture to run the job with
    steps:
      - name: Login to Docker Hub # Step to log in to Docker Hub
        uses: docker/login-action@v2.2.0 # Uses an action to perform the login
        with: # Inputs to the login-action
          # registry: { { registry_url } } # Specifies the registry to log in to. You can set a variable or just hardcode this value.
          username: ${{ secrets.DOCKERHUB_USERNAME }} # Docker Hub username from secrets
          password: ${{ secrets.DOCKERHUB_TOKEN }} # Docker Hub token/password from secrets

      - name: Checkout repository # Step to check out the repository code
        uses: actions/checkout@v3.6.0 # Uses the checkout action

      - name: Set up Docker Buildx # Step to set up Docker Buildx
        uses: docker/setup-buildx-action@v2.10.0 # Uses an action to set up Buildx

      - name: Build and push
        run: |
          docker build -t ojpfight/nextapp .
          docker push ojpfight/nextapp

```