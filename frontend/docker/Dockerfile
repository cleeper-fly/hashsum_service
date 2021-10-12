FROM node:lts-alpine as builder

RUN apk --update --no-cache --virtual build-dependencies add \
    git \
    py-pip \
    make \
    g++

RUN npm config set python /usr/bin/python3
WORKDIR /app
COPY ./package*.json ./
RUN npm install
COPY ./ .
RUN npm run build

FROM nginx:latest

COPY docker/etc/nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app /app
