# AI生成接口文档

> 通过阅读代码，自动生成文档，支持java, c++

## 使用方法

1. 使用 vim 生成一个`.env`，填写 OpenAI 的 API KEY 
    ```
    vim .env
    ```
    填写
    ```
    OPENAI_API_KEY=xxx
    ```
2. 将源代码下载到 `code` 文件夹中
3. 运行 `main.py` 等待文档编写完成
