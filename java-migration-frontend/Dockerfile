FROM node:20-alpine AS build
WORKDIR /app

# Install deps based on package-lock / package.json
COPY package.json package-lock.json* tsconfig*.json ./
COPY public ./public
COPY src ./src
COPY vite.config.ts ./
COPY index.html ./

RUN npm ci --silent
RUN npm run build

FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
