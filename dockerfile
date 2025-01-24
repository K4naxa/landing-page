# Use the official Node.js 18 image as the base image
FROM node:23.6.0 AS build

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Build the Vue 3 application for production
RUN npm run build

# Use an Nginx image to serve the built application
FROM nginx:alpine

# Copy the built application to the Nginx default public directory
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 to access the application
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
