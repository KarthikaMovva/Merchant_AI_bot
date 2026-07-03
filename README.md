# Merchant AI Assistant

An AI-powered Merchant Assistant built using **FastAPI** and **Google Gemini 2.5 Flash**.

The application generates personalized marketing messages for merchants based on:

- Merchant profile
- Trigger information
- Customer information (optional)
- Business context

The project was developed as a prototype for the Magicpin Merchant AI Challenge.

---

# Features

- FastAPI REST API
- Gemini 2.5 Flash integration
- Dynamic prompt generation
- JSON response validation
- Error handling
- Mock fallback when API key is unavailable
- Health check endpoint
- Metadata endpoint

---

# Tech Stack

Backend
- Python 3.11
- FastAPI
- Uvicorn

LLM
- Google Gemini 2.5 Flash

Libraries

- google-generativeai
- python-dotenv
- pydantic



# Installation

```bash
pip install -r requirements.txt
```

---
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```
GEMINI_API_KEY=your_api_key_here
```

---

# Run the Project

```bash
uvicorn app.main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## GET /

Returns server status.

---

## GET /healthz

Health Check

Example

```json
{
    "status":"healthy"
}
```

---

## GET /metadata

Returns application metadata.

---

## POST /tick

Generates an AI-powered marketing message.


# Response Format

Every successful response contains

```
message
cta
send_as
rationale
```

---

# Fallback Mode

If no Gemini API key is configured, the application automatically returns a demo response.

---