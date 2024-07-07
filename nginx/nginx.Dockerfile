# Use the official Nginx image as a base
FROM nginx:latest

# Copy the Nginx configuration file to the container
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf