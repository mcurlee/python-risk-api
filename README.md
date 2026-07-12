## Objective
	What problem are we solving?

## Architecture
	Draw a diagram

## Commands Used
Install FastAPI - python3 -m venv .venv
Activate Fast API: source .venv/bin/activate
Once FastAPI is activated, terminal will show (.venv) in fron tof directory
Now install packages:
	pip install fastapi uvicorn
Save dependencies:
	pip freeze > requirements.txt
Run API:
	uvicorn app:app --reload
You should see "...running on http://ip address"
Navigate to that ip address:port

To close down gracefully:
CRTL + C to quit uvicorn
Verify project
	pwd
	ls -la
Check git status
	git init
	git status
## Lessons Learned
Helm packages Kubernetes resources
Docker packages applications
Kubernetes schedules containers

What is FastAPI: it's a Python web framework used to build REST APIs quickly and with minimal code. Instead of writing a web server from scratch, FastAPI handles:
	HTTP requests
	URL routing
	JSON serialization
	Request validation
	API documentation
	Error handling

## What is Uvicorn?

Uvicorn is the web server that actually runs the FastAPI application.

When I type:

```
uvicorn app:app --reload
```

Uvicorn:

- Starts listening on port 8000
- Waits for incoming HTTP requests
- Passes requests to FastAPI
- Sends responses back to the client

Without Uvicorn, my FastAPI code just sits on disk.

### Simple analogy

FastAPI = the restaurant kitchen

Uvicorn = the waiter

The waiter takes customer orders to the kitchen and delivers the finished meal back.

---

## What is a REST API?

REST stands for **Representational State Transfer**.

A REST API is simply a standardized way for software systems to communicate over HTTP.

Instead of people talking to people...

Applications talk to applications.

Example:

Browser

↓

GET /health

↓

FastAPI

↓

```
{
    "status":"healthy"
}
```

The browser doesn't care that the application is written in Python.

It only understands HTTP and JSON.

That makes REST APIs language-independent.

---

## What are Endpoints?

Endpoints are individual URLs that perform specific actions.

My application has three endpoints:

```
GET /
```

Returns:

```
{
    "message":"Risk Calculator API"
}
```

---

```
GET /health
```

Returns whether the application is healthy.

---

```
POST /risk
```

Calculates a cybersecurity risk score.

Each endpoint performs one specific function.

You can think of endpoints as "doors" into an application.

---

## Why did `/health` return 404?

Because I accidentally wrote:

```
@app.get("health")
```

instead of

```
@app.get("/health")
```

Without the leading slash, FastAPI never created the `/health` route.

The application was running correctly...

The endpoint simply didn't exist.

404 means:

> "The resource you requested does not exist."

---

## How did I troubleshoot it?

Instead of guessing, I followed a structured process.

### Step 1

Observe the problem.

```
GET /health

↓

404 Not Found
```

---

### Step 2

Look at the logs.

Uvicorn showed:

```
GET /health 404
```

That proved:

- Uvicorn was running.
- The browser reached the application.
- Networking wasn't the issue.

---

### Step 3

Inspect the code.

I found:

```
@app.get("health")
```

instead of

```
@app.get("/health")
```

---

### Step 4

Fix it.

Add the slash.

Save.

Uvicorn automatically reloaded.

---

### Step 5

Test again.

```
GET /health

↓

200 OK
```

Problem solved.

---

## How does FastAPI compare to nginx?

This was one of the biggest "aha" moments from the lab.

### FastAPI

FastAPI **creates** an application.

It contains business logic.

Example:

```
Calculate Risk

Validate Input

Store Data

Authenticate Users

Return JSON
```

FastAPI decides **what** happens.

---

### nginx

nginx doesn't create applications.

It delivers them.

Its job is things like:

- reverse proxy
- load balancing
- TLS termination
- serving static files
- routing traffic

nginx decides **where** traffic goes.

---

### Together

A production environment often looks like this:

```
Internet

↓

nginx

↓

FastAPI

↓

Python Code

↓

Database
```

nginx receives the request.

FastAPI processes the request.

Python executes the business logic.

---

# Biggest Lesson Learned

Before this lab, I thought Kubernetes was mostly about deploying containers.

Now I understand Kubernetes doesn't care _what_ the application does.

Its job is simply to keep the application running.

It could be:

- FastAPI
- Java Spring Boot
- Node.js
- Go
- .NET
- nginx

Kubernetes only sees **containers**.

The application itself is built with frameworks like FastAPI, and tomorrow I'll package that application into a Docker image, deploy it with Kubernetes, and manage it with Helm. That completes the full path from **code → container → platform**, which is the core workflow of modern platform engineering.
## Troubleshooting

Problem: When I navigate to http://localhost:8000/health, I got a 404 error
Cause: missed a forward slash in that code block
Solution: once I added the slash and saved, I re-navigated to the page and the expected result popped up.