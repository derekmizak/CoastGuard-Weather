# Use the official Nginx image as a parent image
FROM nginx:alpine

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy the configuration file from the current directory to the container
COPY ./docker/nginx/django.conf /etc/nginx/conf.d/

# Create a new user 'nginxuser' and group 'nginxgroup'
# and set the ownership of relevant directories
#RUN addgroup -S nginxgroup && adduser -S nginxuser -G nginxgroup \
#    && chown -R nginxuser:nginxgroup /var/cache/nginx \
#    && chown -R nginxuser:nginxgroup /var/log/nginx \
#    && chown -R nginxuser:nginxgroup /etc/nginx/conf.d

# Expose port 80 and 443
EXPOSE 80 443

# Run Nginx as non-root user
#USER nginxuser

# Start Nginx when the container has provisioned
CMD ["nginx", "-g", "daemon off;"]
