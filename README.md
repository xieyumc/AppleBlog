复刻[Apple Newsroom](https://www.apple.com/newsroom/)的一个博客网站，前后端分离

![项目结构简图](astro/public/preview/img_2.png)

![浅色模式](astro/public/preview/img.png)

![深色模式](astro/public/preview/img_1.png)
# 部署
为了方便部署，已经把项目容器化，并且编译好镜像上传了docker hub，运行非常简单，只需要2步：

1.	安装好docker，下载仓库根目录里的`docker-compose-ServerTemplate.yml`并更名为`docker-compose.yml`

2.	运行命令`docker compose up`，就会从docker hub拉取镜像，自动运行



# 注意

仓库根目录`docker-compose.yml`是为了构建docker hub镜像用的，要直接运行一定要下载仓库根目录里的`docker-compose-ServerTemplate.yml`并更名为`docker-compose.yml`

如果只是测试运行，不需要改动`docker-compose-ServerTemplate.yml`的任何内容，已经在容器里定义好数据库和示例数据了，访问localhost即可打开网站

如果想部署到服务器，需要把`docker-compose-ServerTemplate.yml`中的nginx的`SERVER_NAME`和Django的`SERVER_NAME`改成服务器域名，并且在docker volume里导入一个数据库，防止更新容器导致的数据库内容覆盖
