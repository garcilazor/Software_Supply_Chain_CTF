#!/bin/bash

echo "TEMP=\`curl -s -c cookiejar -H \"Content-Type: application/json\" 'http://marsexp/login' | grep 'csrf_token' | awk '{print $2}'\`" >> /root/.bashrc
echo 'TEMP="${TEMP%\"}"' >> /root/.bashrc
echo 'CSRF="${TEMP#\"}"' >> /root/.bashrc
echo "echo 'root@ubuntu:/app# curl -H \"X-XSRF-Token: $CSRF\" -d \"next=%2Fadmin%2F&email=ramon%40me.com&password=password\" -b cookiejar -c cookiejar http://marsexp/login'" >> /root/.bashrc
echo 'curl -H "X-XSRF-Token: $CSRF" -d "next=%2Fadmin%2F&email=ramon%40me.com&password=password" -b cookiejar -c cookiejar http://marsexp/login' >> /root/.bashrc
echo 'echo "\n"' >>/root/.bashrc
