- [!] Checklist for **insecure direct object reference**
---
### **IDOR Vulnerability Checklist**

1. **Identify Parameters**:
    - [i] Look for object IDs in URLs, query strings, POST bodies, and headers.
    - [I] Examples: `/user/123`, `?id=456`, `{"order_id": "789"}`.
2. **Manipulate Object IDs**:    
    - [i] Change ID values to another user's or an invalid ID.
    - [I] Increment, decrement, or replace with predictable patterns (e.g., `1, 2, 3`).
3. **Test HTTP Methods**:
    - [I] Check all methods (GET, POST, PUT, DELETE) for access control issues.
4. **Check Nested Objects**:
    - [I] Test multi-level paths (e.g., `/account/123/order/456`) by altering each ID.
5. **Role and Permission Testing**:
    - [i] Test if users with lower privileges can access admin or other users' resources.
6. **Error Message Analysis**:
    - [i] Look for revealing error messages after ID manipulation.
7. **Session Dependency**:
    - [i] Ensure ID access is tied to the session or authorization token.
8. **Fuzzing**
    - [i] Use tools like Burp Suite, Postman, or ffuf to brute force ID ranges.
9. **Log and Replay**: 
    - [i] Capture API requests and replay them with modified IDs.
10. **Avoid Client-Side Validation**:
    - [i] Ensure all checks are server-side.

---