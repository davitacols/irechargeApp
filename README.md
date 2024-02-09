# iRecharge Backend API Documentation

## Overview

The iRecharge Backend API is built with FastAPI and provides endpoints for managing articles, providers, and prices.

## Table of Contents

1. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installing Dependencies](#installing-dependencies)
    - [Running the Application](#running-the-application)
2. [Endpoints](#endpoints)
3. [Documentation](#documentation)
4. [Examples](#examples)
5. [Acknowledgments](#acknowledgments)
6. [License](#license)

## Getting Started

### Prerequisites

- Python 3.6 or later
- [FastAPI](https://fastapi.tiangolo.com/) and [Uvicorn](https://www.uvicorn.org/)

### Installing Dependencies

```bash
pip install fastapi uvicorn


### Installing Dependencies

```bash
uvicorn main:app --reload

## Endpoints

- **Create Article**: `POST /articles/`
- **Read Article**: `GET /articles/{article_no}`
- **Create Provider**: `POST /providers/`
- **Create Price**: `POST /prices/`
- **Read Prices**: `GET /prices/`

## Documentation

- Interactive API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Examples

### Create Article

```bash
curl -X POST "http://127.0.0.1:8000/articles/" -H "Content-Type: application/json" -d '{"article_no": 101, "currency": "US Dollar", "description": "Example Article"}'


**Read Article**

```bash
curl "http://127.0.0.1:8000/articles/101"


**Crate Provider**

```bash
curl -X POST "http://127.0.0.1:8000/providers/" -H "Content-Type: application/json" -d '{"provider_no": 1, "name": "Example Provider"}'
