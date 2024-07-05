# 使用特定版本的Node.js官方镜像
FROM node:22-alpine3.19

# 设置工作目录
WORKDIR /app

# 复制package.json和package-lock.json
COPY package*.json ./

# 安装依赖
RUN npm install
#RUN npm install @astrojs/node

# 复制项目文件
COPY . .

# 构建项目
#RUN npm run build

# 暴露端口
EXPOSE 3000

ARG API_URL
ENV API_URL=${API_URL}

# 启动项目
CMD ["npm", "run", "dev", "--", "--host"]