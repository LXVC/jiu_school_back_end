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
//发送手机验证码
//注:手机验证码只生成不发送,随着接口带回
//备注:username即phone
//以下所有需要用到phone的地方全部用username代替
var getVcode = 
{
  url:'',
  method:'',
  args:
  {
    phone:''
  },
  response:
  {
    ok:true,
    error_code:'',
    error_desc:'',
    vcode:''
  }
}
//用户登录
//注:为了防止暴力爆破,此接口应该有所限制
var login = 
{
    url:'',
    method:'post',
    args:
    {
      username:'',
      password:'' //MD5加密后password
    },
    response:
    {
      ok:true,
      error_code:'',
      error_desc:'',
      user:{}//user对象
    }
}
//用户注册
var register = 
{
    url:'',
    method:'post',
    args:
    {
      username:'',
      password:'', //MD5加密后password
      vcode:'' //手机验证码
    },
    response:
    {
      ok:true,
      error_code:'',
      error_desc:'',
      user:{}//user对象
    }
}
//用户忘记密码
var forgetpassword = 
{
    url:'',
    method:'post',
    args:
    {
      username:'',
      vcode:'' //手机验证码
    },
    response:
    {
      ok:true,
      error_code:'',
      error_desc:'',
      token: '' //本次重设密码的token
    }
}
//用户重设密码
var resetpassword = 
{
    url:'',
    method:'post',
    args:
    {
      username:'',
      old_password:'',//MD5加密后password
      new_password:'', //MD5加密后password
      token:'' //用户忘记密码所带token,有时限
    },
    response:
    {
      ok:true,
      error_code:'',
      error_desc:'',
    }
}
