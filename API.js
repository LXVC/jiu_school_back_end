const example = {
  url: "http://127.0.0.1:5000", // 请求地址
  method: "GET", // 请求方式['GET', 'POST']
  args: {
    // GET请求时带的参数， POST 时即为 body
    id: 1
  },
  response: {
    // 后端返回值
    ok: true,
    error_code: 1024,   // 1000至2000之间
    error_desc: "密码不正确", // 错误说明
    id: 1,
    name: "语文"
  }
}
