# API Documentation

## Base URL
http://localhost:5000

## Headers
x-api-key: secure_api_key

---

## GET /health
Check service status

## POST /block
Block an IP

Body:
{
  "ip": "192.168.1.100"
}

## POST /unblock
Unblock IP

## GET /blacklist
Get all blocked IPs

## GET /report
Generate system report
