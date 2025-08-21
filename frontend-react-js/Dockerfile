FROM node:20-slim
WORKDIR /frontend-react-js
COPY package.json package-lock.json* ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]