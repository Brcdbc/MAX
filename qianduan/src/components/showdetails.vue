<template>
  <div class="article-detail">
    <router-link to="/main" class="back-button">
      <i class="el-icon-arrow-left"></i> 返回
    </router-link>
    <h1 class="article-title">{{ article.title }}</h1>
    <p class="article-info">作者：{{ article.author }}</p>
    <p class="article-content">{{ article.content }}</p>
  </div>
</template>

<script>
import { detailed } from '../api/api.js';

export default {
  data() {
    return {
      article: {
        title: '',
        author: '',
        content: '',
      },
    };
  },
  created() {
    this.getDetail();
  },
  methods: {
    getDetail() {
      detailed(this.$route.params.id)
        .then((response) => {
          this.article = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style>
.article-detail {
  margin: 20px;
  padding: 20px;
  background-color: #f5f5f5; /* 浅灰色背景 */
  border: 1px solid #ccc;
  border-radius: 8px; /* 更圆润的边框 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 更明显的阴影 */
}

.article-title {
  font-size: 28px; /* 增大标题字体 */
  font-weight: bold;
  color: #333;
  margin-bottom: 20px; /* 增加标题下方间距 */
}

.article-info {
  font-size: 18px; /* 增大作者信息字体 */
  color: #555; /* 更柔和的文本颜色 */
  margin-bottom: 10px;
}

.article-content {
  font-size: 20px; /* 增大内容字体 */
  line-height: 1.6;
  color: #333; /* 更醒目的文本颜色 */
  margin-top: 20px;
}

.back-button {
  color: #007BFF;
  text-decoration: none;
  display: flex;
  align-items: center;
  font-size: 18px; /* 增大返回按钮字体 */
  margin-bottom: 20px; /* 增加按钮下方间距 */
}

.back-button i {
  margin-right: 8px; /* 缩小图标与文本间距 */
  font-size: 24px; /* 增大图标大小 */
}
</style>
