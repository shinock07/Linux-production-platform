# NGINX Reverse Proxy

## Architecture

```text
Client
   |
   | HTTP :80
   v
NGINX
   |
   | proxy_pass
   v
Python Application :8000
   |
   v
systemd
