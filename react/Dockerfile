FROM node:8.1
MAINTAINER beradgaskill@gmail.com

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV
RUN mkdir -p /usr/src/app
COPY package.json /usr/src/app/package.json
WORKDIR /usr/src/app
RUN npm install
COPY . /usr/src/app

CMD ["npm","start"]