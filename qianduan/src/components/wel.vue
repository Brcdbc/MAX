<template>
  <div class="welcome">
    <el-container>
      <el-main>
        <div class="welcome-content">
          <h1 class="welcome-title">欢迎来到我制作的CMS系统</h1>
          <p class="welcome-description">我们实现了注册，登录以及文章的增删改查的的功能</p>
          <router-link to="/login">
            <el-button class="welcome-button" type="primary" size="large">进入系统</el-button>
          </router-link>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'Welcome1',
}
</script>
<style scoped>
body, html {
  margin: 0;
  padding: 0;
}

.welcome {
  background-image: url('/static/background.jpg');
  background-size: cover;
  background-position: center;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0; /* 增加这行以消除外部 margin */
}

.welcome-content {
  text-align: center;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  margin: 0; /* 增加这行以消除内部 margin */
}

.welcome-title {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 20px;
  color: rgba(51, 51, 51, 0.7);
}

.welcome-description {
  font-size: 18px;
  color: rgba(102, 102, 102, 0.7);
  margin-bottom: 20px;
}

.welcome-button {
  width: 200px;
  height: 60px;
  font-size: 20px;
  margin: 0; /* 增加这行以消除按钮内部的 margin */
}
</style>
