# Instabug task

This task is required by instabug, their requirements were in rub in rails but this implmenetation is in djanog


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure (Optional)](#project-structure-optional)
- [Configuration](#configuration)
- [Contributing](#contributing)

## Introduction

The project should keep track of bugs reported by the sdk on the client side

## Features

- Using docker-compose and the whole stack can run with single command
- Applicatoin has 2 endpoints POST /bugs and GET /bugs/[number]
- The post endpoint not writing directly to the database and publishes a message through rabbit mq instead
- Each new bug has a unique number for each client

## Installation

1. **Prerequisites:** 
    - **Docker:** [Install Docker Engine](https://docs.docker.com/engine/install/)
    - **Docker Compose:** [Install Docker Compose](https://docs.docker.com/compose/install/) 
   
2. **Cloning the Repository:**
    ```bash
    git clone https://github.com/ahmedyasserays/instabug.git
    cd instabug
    ```


## Usage
in progress

## Project Structure
in progress


## Contributing

We welcome contributions from everyone! Here's how you can get involved:

1. **Fork the repository:** Click the "Fork" button at the top right of this page. This will create your own copy of the project.
2. **Make changes:** Clone your forked repository, make your desired changes, and commit them.
3. **Create a pull request:** Submit a pull request (PR) to the main repository.  Please provide a clear description of your changes and why they should be included.


### Additional Notes:

- **Issues:** If you find a bug or have a feature request, please open an issue in this repository.

