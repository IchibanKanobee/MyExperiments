# frontend/Dockerfile
FROM node:14

WORKDIR /reactknow

COPY package.json package-lock.json ./

RUN npm install

# Install Packages
RUN npm install react-bootstrap bootstrap
RUN npm install react-router-dom

COPY . .

EXPOSE 3000

CMD ["npm", "start"]

