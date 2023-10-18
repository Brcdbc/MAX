// appfront/src/api/api.js
import axiosInstance from './index'

const axios = axiosInstance

export const postuser = (username,password) => {return axios.post(`http://localhost:8000/api/userapi/register/`, {'username': username, 'password':password})}

export const login_postuser = (username,password) => {return axios.post(`http://localhost:8000/api/userapi/login/`, {'username': username, 'password':password})}

export const Apost = (title,content) => {return axios.post(`http://localhost:8000/api/userapi/writeArticle/`, {'title': title, 'content':content})}

export const getArticles = () => {return axios.get(`http://localhost:8000/api/ArticlesViewSet/`)}

export const postwen = (author,title,content) => {return axios.post(`http://localhost:8000/api/userapi/writeArticle/`, {'author': author,'title': title, 'content':content})}


export const detailed = (id) => {return axios.post(`http://localhost:8000/api/userapi/getin/`, {'de_id': id})}

export const deleteArticle = (id) => {return axios.post(`http://localhost:8000/api/userapi/delete/`, {'de_id': id})}

export const get_queryset =()  => {return axios.post(`http://localhost:8000/api/my/get_queryset/`)}

export const updateArticle = (id,title, content) => {return axios.post('http://localhost:8000/api/userapi/xiugai/', {'i_id':id, title: title, content: content });};
  