<template>
  <div class="article-form">
    <router-link to="/my" class="my-button">
      <i class="el-icon-arrow-left"></i> 返回我的文章
    </router-link>
    <h1 class="form-title">{{ formTitle }}</h1>
    <!-- Form to add an article -->
    <el-form @submit.native.prevent="articleSubmit" label-width="120px">
      <el-form-item label="文章标题">
        <el-input v-model="inputArticle.title" placeholder="文章标题"></el-input>
      </el-form-item>
      <el-form-item label="文章内容">
        <el-input type="textarea" v-model="inputArticle.content" placeholder="文章内容"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" native-type="submit">提交</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { Apost } from '../api/api.js';

export default {
  name: 'ArticleForm',
  data() {
    return {
      formTitle: '创建新文章',
      inputArticle: {
        title: '',
        content: '',
      },
    };
  },
  methods: {
    articleSubmit() {
      Apost(this.inputArticle.title, this.inputArticle.content).then((response) => {
        this.$message.success(response.data.msg);
        // 你可以在提交后执行其他操作，如重置表单
        this.inputArticle.title = '';
        this.inputArticle.content = '';
      });
    },
  },
};
</script>

<style scoped>
.my-button {
  position: absolute;
  top: 10px;
  left: 10px;
  background-color: #007BFF;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  text-decoration: none;
}

.form-title {
  font-size: 28px;
  font-weight: bold;
  color: #333;
  margin-bottom: 20px;
  text-align: center;
}

.el-input {
  width: 100%;
}

.el-button {
  width: 100%;
}
</style>
