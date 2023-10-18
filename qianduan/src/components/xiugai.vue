<template>
  <div class="article-detail">
    <router-link to="/my" class="home-button">回到我的文章</router-link>
    <button @click="deleteArticle" class="delete-button">删除</button>
    <!-- 文章标题，可以编辑 -->
    <h1 class="article-title">
      <span v-if="isEditing">
        <input v-model="article.title" class="edit-input" type="text">
      </span>
      <span v-else>
        {{ article.title }}
      </span>
    </h1>

    <!-- 作者信息 -->
    <p class="article-info">作者：{{ article.author }}</p>

    <!-- 文章内容，可以编辑 -->
    <p class="article-content">
      <span v-if="isEditing">
        <textarea v-model="article.content" class="edit-textarea"></textarea>
      </span>
      <span v-else>
        {{ article.content }}
      </span>
    </p>

    <!-- 编辑和保存按钮 -->
    <button @click="startEditing" v-if="!isEditing">编辑</button>
    <button @click="saveChanges" v-if="isEditing">保存</button>
  </div>
</template>

<script>
import { detailed, updateArticle,deleteArticle } from '../api/api.js';

export default {
  data() {
    return {
      article: {
        id: 0,
        title: '',
        author: '',
        content: '',
      },
      isEditing: false,
    };
  },
  created() {
    this.getArticleDetails();
  },
  methods: {
    getArticleDetails() {
      // 获取文章详细信息
      detailed(this.$route.params.id)
        .then(response => {
          this.article = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    startEditing() {
      // 开始编辑文章
      this.isEditing = true;
      console.log(this.$route.params);
    },
    deleteArticle(){
      deleteArticle(this.$route.params.id)
        .then(response => {
              alert("已删除")
              this.$router.push({ name: 'my' })
        })
        .catch(error => {
          console.error(error);
        });
    },
    saveChanges() {
      // 保存修改后的文章内容
      updateArticle(this.$route.params.id, this.article.title,this.article.content)
        .then(response => {
          this.isEditing = false;
          // 可选：更新文章内容为响应中的数据
        })
        .catch(error => {
          console.error(error);
          // 处理错误，如果需要的话
        });
    },
  },
}
</script>

<style>
.article-detail {
  margin: 20px;
  padding: 20px;
  background-color: #f7f7f7;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.article-title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.article-info {
  font-size: 16px;
  color: #777;
  margin-bottom: 5px;
}

.article-content {
  font-size: 18px;
  line-height: 1.5;
  color: #444;
}

button {
  margin-top: 10px;
  padding: 5px 10px;
  background-color: #007BFF;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.edit-input,
.edit-textarea {
  /* 添加编辑时输入框的样式 */
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.delete-button {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 5px 10px;
  background-color: #FF0000; /* 红色按钮 */
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.delete-button:hover {
  background-color: #CC0000; /* 鼠标悬停时的颜色 */
}
.home-button {
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
