## 说明

---

dist 文件夹内存放的是从nx-admin 中build 之后版本 



要在生产环境中运行打包后的代码，你需要将静态资源部署到一个 Web 服务器或 CDN 上。以下是一些部署打包后的 Web 应用程序的方法：

1. 使用 Web 服务器

将打包后的静态资源部署到一个 Web 服务器上，例如 Apache 或 Nginx，然后使用 Web 服务器配置文件将请求转发到静态资源的路径。如果你使用的是 Apache，可以将静态资源放到 Web 服务器的 `htdocs/` 或 `var/www/html/` 目录下，然后在 Apache 配置文件中添加以下内容：

```apl
apacheconfCopy code<VirtualHost *:80>
    ServerName example.com
    DocumentRoot /var/www/html
    <Directory /var/www/html>
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

2. 使用 Node.js HTTP 服务器

你可以使用 Node.js 提供的 HTTP 服务器模块将静态资源部署到 Node.js 服务器上。以下是一个简单的 Node.js HTTP 服务器示例：

```javascript
javascriptCopy codeconst http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
  let filePath = path.join(__dirname, 'build', req.url);
  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end('File not found');
    } else {
      let contentType;
      if (filePath.endsWith('.html')) {
        contentType = 'text/html';
      } else if (filePath.endsWith('.js')) {
        contentType = 'text/javascript';
      } else if (filePath.endsWith('.css')) {
        contentType = 'text/css';
      } else {
        contentType = 'text/plain';
      }
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(data);
    }
  });
});

const PORT = process.env.PORT || 8000;
server.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
```

该服务器将请求的静态资源文件读取到内存中，并通过 HTTP 响应返回。你可以使用 `node server.js` 命令启动该服务器。

3. 使用 Firebase Hosting

如果你的应用程序使用 Firebase，可以使用 Firebase Hosting 将静态资源部署到 Firebase 服务器上。使用 Firebase Hosting 可以轻松地将应用程序部署到全球范围内的 CDN 上，并获得 HTTPS 加密和自定义域名等功能。在使用 Firebase Hosting 之前，你需要在 Firebase 控制台中创建一个项目并安装 Firebase CLI。

安装完成 Firebase CLI 后，在应用程序的根目录下运行以下命令：

```shell
shellCopy code
firebase init hosting
```

4. 使用其他云服务

除了 Firebase Hosting，其他云服务提供商（如 AWS、Azure、Google Cloud 等）也提供类似的静态资源托管服务。你可以选择将打包后的静态资源部署到这些云服务上，以实现全球范围内的 CDN 加速和高可用性等功能。





* 实现

  这里采用了python自带的http服务器

  ```shell
  python3 -m http.server
  ```

  由于默认起的服务存在跨域问题,这里继承了服务,重写了该服务

  运行:

  ```shell
  python3 run.py
  ```

  