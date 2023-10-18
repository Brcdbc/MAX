<template>
    <div class="hello">
      <router-link to="/main" class="home-button">回到主页</router-link>
      <h1 class="title">{{ msg }}</h1>
      <router-link to="/addA" class="write-button">写文章</router-link>
      <ul class="article-list">
        <li v-for="(wen, index) in wens" :key="wen.id" class="article-item">
          <router-link :to="'/xiugai/' + wen.id" class="article-link">
            <span class="article-index">{{ index }}</span>
            <span class="article-title">{{ wen.title }}</span>
            <span class="article-author">{{ wen.author }}</span>
          </router-link>
        </li>
      </ul>
    </div>
  </template>
  
  
  <script>
  import {  get_queryset, postwen } from '../api/api.js'
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: '我的文章',
        wens: [ ],
        inputwen: {
          author: '',
          title: '',
          content: '',
        }
      }
    },
    methods: {
      loadArticles() {
        get_queryset().then(response => {
          this.wens = response.data;
        });
      },
      wenSubmit() {
        postwen(this.inputwen.author, this.inputwen.title, this.inputwen.content).then(response => {
          console.log(response);
          this.loadArticles();
        });
      }
    },
    created: function () {
        this.loadArticles()
    }
  }
  </script>
  <style>
  .hello {
    margin: 20px;
  }
  
  .title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
    margin-bottom: 20px;
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

.write-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background-color: #007BFF;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  text-decoration: none;
}
  </style>
  