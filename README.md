# AI 软件说明文档生成

> 通过阅读代码，自动生成文档

- 作者：欧阳鹏
- 开发日期：2023 年 4 月 20 日
https://github.com/oyps/code2doc

## 使用方法

1. 将 `.env.example` 复制到 `.env`，填写 OpenAI 的 API KEY
2. 将源代码下载到 `code` 文件夹中
3. 将事先准备的文档大纲，放入 `tasks` 文件中，一行一个任务
4. 运行 `main.py` 等待文档编写完成