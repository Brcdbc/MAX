<template>
  <div class="hello">
    <router-link to="/my" class="my-articles-button">我的文章</router-link>
    <h1 class="title">{{ msg }}</h1>
    
    <!-- 写文章表单 -->
    <form @submit.prevent="submitArticle" class="article-form">
      <div class="form-group">
        <label for="title">请写如你要查询的文章</label>
        <input type="text" id="title" v-model="inputwen.title" required @input="searchArticles" style="width: 200px; height: 30px;">

      </div>  
    </form>
    
    <!-- 文章列表 -->
    <ul class="article-list">
      <li v-for="(wen, index) in filteredArticles" :key="wen.id" class="article-item">
        <router-link :to="'/showdetails/' + wen.id" class="article-link">
          <span class="article-index">{{ index+1 }}</span>
          <span class="article-title">{{ wen.title }}</span>
          <span class="article-author">{{ wen.author }}</span>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { getArticles, postwen } from '../api/api.js'

export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: '请欣赏我们的文章',
      wens: [],
      inputwen: {
        author: '',
        title: '',
        content: '',
      },
      filteredArticles: [], // 用于存储筛选后的文章
    }
  },
  methods: {
    loadArticles() {
      getArticles().then(response => {
        this.wens = response.data;
        this.filteredArticles = response.data; // 初始化 filteredArticles
      });
    },
    submitArticle() {
      // 提交文章表单
      postwen(this.inputwen.author, this.inputwen.title, this.inputwen.content).then(response => {
        console.log(response);
        this.loadArticles();
        this.inputwen = { author: '', title: '', content: '' }; // 清空表单
      });
    },
    searchArticles() {
      // 在 wens 中筛选包含搜索关键字的文章
      this.filteredArticles = this.wens.filter(wen => wen.title.includes(this.inputwen.title));
    }
  },
  created() {
    this.loadArticles();
  }
}
</script>




<style>
.hello {
  margin: 20px;
}
.custom-input {
  width: 200px;
  height: 30px;
  /* 添加其他样式属性，如颜色、边框等 */
}
.title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 20px;
}

.article-form {
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 10px;
}

label {
  display: block;
  font-size: 16px;
  font-weight: bold;
}

input, textarea {
  width: 100%;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  background-color: #007BFF;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.article-list {
  list-style: none;
  padding: 0;
}

.article-item {
  margin-bottom: 10px;
  padding: 10px;
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.article-link {
  text-decoration: none;
  color: #333;
  display: flex;
  align-items: center;
}

.article-index {
  flex: 0 0 10%;
  font-weight: bold;
}

.article-title {
  flex: 0 0 60%;
  font-size: 18px;
}

.article-author {
  flex: 0 0 30%;
  font-size: 16px;
  color: #777;
}

.my-articles-button {
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
</style>
