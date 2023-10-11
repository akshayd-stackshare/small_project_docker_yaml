# Agile Card for Correlation IDs at entry points to backend, so we can trace an event properly.

---

### **Correlation IDs:** 
To make it easier to query data as well as inspect its path through the system, I want to add correlation IDs.

---

### **User Story:** 
- **Role:** Platform Operator
- **Desire:** More Easily Track Requests
- **Benefit:** Allows for easier debugging of the system

> _As a Platform Operator, I want to more easily track requests so that debugging of the system is facilitated._

---

### **Acceptance Criteria:**
1. All incoming requests to the backend have a correlation ID.
2. If a request does not have a correlation ID, one should be generated and added.
3. The correlation ID should be logged at every service or component that it passes through.
4. The correlation ID should be returned in the response headers.
5. Existing logs should be retrofitted to include the correlation ID where applicable.
6. Update application to use logging correctly.

---

### **Technical Details:** 
- **Endpoints:** 
  - [POST, /api/service1, Endpoint for service 1]
  - [GET, /api/service2, Endpoint for service 2]
  - [...]
- **Database Changes:** 
  - [Add a new 'correlation_id' column in the 'logs' table]
  - [...]
- **Third-party Services:** [No changes required]
- **Algorithms:** 
  - [Use UUID to generate unique correlation IDs]

---

### **Dependencies:** 
- Logging mechanism already in place.
- Middleware for processing request headers.

---

### **Mockups/Wireframes:** 
[Links or references to any visual aids. N/A for this task as it's more backend-oriented.]

---

### **Notes/Comments:** 
Correlation IDs will help improve monitoring, logging, and debugging, especially in a microservices architecture where tracing can become complex.

---

### **Priority:** 
High

---

### **Estimation:** 
Unestimated 
---

### **Assigned To:** 
Jermell B
---

### **Labels/Tags:** 
- Backend
- Debugging
- Enhancement

---

### **Status:** 
To Do

---

### **History/Activity Log:** 
