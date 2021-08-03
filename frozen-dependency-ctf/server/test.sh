#!/bin/bash

TEMP=`curl -c cookiejar -H "Content-Type: application/json" 'http://0.0.0.0:8000/login' | grep 'csrf_token' | awk '{print $2}'`
echo $TEMP
TEMP="${TEMP%\"}"
CSRF="${TEMP#\"}"
curl -H "X-XSRF-Token: $CSRF" -d "next=%2Fadmin%2F&email=admin%40me.com&password=password" -b cookiejar -c cookiejar http://0.0.0.0:8000/login
