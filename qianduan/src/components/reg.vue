<template>
  <el-container class="reg-container">
    <el-header>
      <h1 class="page-title">注册页面</h1>
    </el-header>
    <el-main>
      <el-form :model="formData" ref="form" label-width="100px">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="formData.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="formData.password" placeholder="请输入密码"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submit">注册</el-button>
          <el-button @click="gotoLogin" class="login-link">已有账号？点击这里登录</el-button>
        </el-form-item>
        
      </el-form>
    </el-main>
  </el-container>
</template>

<script>
import { postuser } from '../api/api.js';

export default {
  data() {
    return {
      formData: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    submit() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          postuser(this.formData.username, this.formData.password).then((response) => {
            this.$message({
              message: response.data.msg,
              type: response.data.msg === '注册成功' ? 'success' : 'error',
            });
            if (response.data.msg === '注册成功') {
              this.$router.push({ name: 'login' });
            }
          });
        }
      });
    },
    gotoLogin() {
      this.$router.push({ name: 'login' });
    },
  },
};
</script>

<style scoped>
.reg-container {
  width: 100%;
  height: 100%;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}

.page-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.login-link {
  margin-top: 10px;
  color: #007BFF;
  text-decoration: underline;
  cursor: pointer;
}
</style>
