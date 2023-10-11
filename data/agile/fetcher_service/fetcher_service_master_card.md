# URL Fetcher Service

---

### **Title/Summary:** 
The purpose of this card is to create a service that will do 4 things:
- [x] Request a webpage
- [x] Store a screenshot of that webpage
- [x] Store the raw HTML response
- [x] Store the archive from the browser of all responses and calls
- [X] Deploy api onto docker via a docker-compose
- [X] Ensure all traffic transits a VPN container
---

### **User Story:** 
- **Role:** CLI or UI user
- **Desire:** Initiate and Store the results of a crawl
- **Benefit:** 
  - check if a webpage exists
  - ensure no scraping errors
  - Monitor a point in time for changes.

> _As a [role], I want to [do something] so that [benefit/result]._ 

---

### **Acceptance Criteria:** 
1. Can request a webpage via a function
2. Stores what the user sees if they were to visit manually
3. Raw textual oriented data is stored in MinIO
4. Visual data is stored in MinIO
5. The service runs until stopped by operator
6. Rate limiting
---

### **Technical Details:**
**Overview**

- **Endpoints:** 
  - [GET, /fetch_site, grabs data from a website]

- **Inputs**

  - **Payload 1:**
    - correlation_id
    - requester
    - url string
    - time in utc

- **Outputs**

  - **Payload 1:**
    - correlation_id
    - requester
    - url string
    - time in utc
    - raw text data
    
  - **Payload 2:**
    - correlation_id
    - requester
    - url string
    - time in utc
    - raw image data


- **Database Changes:** 
    - None Currently
  
- **MinIO Object Creation:**
  
  - **Bucket Name:** Screenshots
  - **Object Name:** screenshots/url
  - **Access Policy:** Public
  - **Size/Capacity:** Undetermined
  - **Metadata:** UTC
  - **Retention Policy:** Forever
  
  - **Bucket Name:** Raw Text
  - **Object Name:** raw_text/url
  - **Access Policy:** Public
  - **Size/Capacity:** Undetermined
  - **Metadata:** UTC
  - **Retention Policy:** Forever
  
- **RabbitMQ:**
  - **Queues:**
  - 
    ---
    - **Queue Name:** Fetch Input Queue
    - **Durable:** Yes
    - **Exclusive:** Yes
    - **Auto-delete:** Yes
    ---
  - 
    - **Queue Name:** Fetch Screenshot Queue
    - **Durable:** Yes
    - **Exclusive:** Yes
    - **Auto-delete:** Yes
    ---
  - 
    - **Queue Name:** Fetch Raw Text Queue
    - **Durable:** Yes
    - **Exclusive:** Yes
    - **Auto-delete:** Yes
    
  - **Routing Strategies:**
    - **Exchange Type:** Direct
    - **Binding Key:** *
    - **Routing Key (for message publishing):** *
    - **Dead Letter Exchange/Queue:** Todo

- **Third-party Services:** None


---
## Algorithms
### Rate Limiting Approaches

1. **Fixed Delay**
    - **Description**: This method involves inserting a fixed delay or pause between successive requests.
    - **Usage**: After every request, the crawler pauses for a specified duration before initiating the next request.
    - **Example**: If the delay is set to 1 second, the crawler will make a maximum of 60 requests per minute.

2. **Token Bucket**
    - **Description**: The token bucket algorithm is a method that allows bursts of requests up to a defined limit.
    - **Usage**: 
        - A "bucket" is filled with tokens at a consistent rate.
        - Every request made removes a token from the bucket.
        - If the bucket is empty, further requests need to wait until tokens are added.
    - **Example**: If the bucket can hold 10 tokens and is refilled at a rate of 1 token per second, then a burst of 10 requests can be made immediately, followed by one request per second thereafter.

3. **Leaky Bucket**
    - **Description**: This algorithm maintains a constant output rate, regardless of the burstiness of the input. 
    - **Usage**:
        - Requests enter the bucket and are processed at a fixed rate.
        - If requests arrive faster than they can be processed and the bucket fills up, surplus requests are discarded or queued.
    - **Example**: If the bucket processes 1 request per second and 10 requests arrive at once, the first request is processed immediately, while the remaining 9 have to wait, with the bucket "leaking" one request per second.

---


### **Dependencies:** 
- RabbitMQ
- MinIO
- \>= Python 3.10

---

### **Mockups/Wireframes:** 
![fetcher_service_high_level.drawio.png](..%2F..%2Fdiagrams%2Ffetcher_service_high_level.drawio.png)


---

### **Notes/Comments:** 
[Any additional context or information]

---

### **Priority:** 
High

---

### **Estimation:** 
Undetermined

---

### **Assigned To:** 
Jermell

---

### **Labels/Tags:** 
- Backend/API

---

### **Status:** 
In Progress

---

