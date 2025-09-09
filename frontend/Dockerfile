FROM node:20-alpine
RUN apk add --no-cache g++ make py3-pip

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

COPY package*.json .

RUN npm install
RUN npm install vite --save-dev

COPY . .

CMD ["npm", "run", "dev"]
