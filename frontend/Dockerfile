# base image
FROM node:12.20.0-alpine

RUN npm i -g serve
# set working dir
WORKDIR /app
ENV PATH /app/node_modules/ .bin:$PATH

# install and cache app dependencies
COPY  /app/package.json ./
RUN npm install 
# RUN npm install @vue/cli@3.7.0 -g
COPY . .

RUN npm run build


#start app
CMD ["npm", "run", "serve" ]