FROM node:16

WORKDIR /app

COPY ./frontend_app/package.json ./frontend_app/package-lock.json ./
COPY ./frontend_app/public ./public
COPY ./frontend_app/src ./src
RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
