import { makeAutoObservable } from "mobx";
import axios from "axios";

const BASE_URL = "http://localhost:8000";

class CommentStore {
    comments = [];

    constructor() {
        makeAutoObservable(this);
    }

    generateRandomName() {
        const randomName = "User" + Math.floor(Math.random() * 1000);
        return randomName;
    }

    async fetchComments() {
        try {
            const response = await axios.get(`${BASE_URL}/api/v1/all-comments/`);
            this.comments = [...response.data];
        } catch (error) {
            console.error("Ошибка при загрузке комментариев:", error);
            this.comments = [];
        }
    }

    async addComment(text, parentId = null) {
        const authorName = this.generateRandomName();
        try {
            const response = await axios.post(`${BASE_URL}/api/v1/all-comments/`, { text, parent: parentId, author_name: authorName });
            this.comments.push(response.data);
            await this.fetchComments();
        } catch (error) {
            console.error("Ошибка при добавлении комментария:", error);
        }
    }

    async deleteComment(id) {
        try {
            await axios.delete(`${BASE_URL}/api/v1/all-comments/${id}/`);
            this.comments = this.comments.filter(comment => comment.id !== id);
            await this.fetchComments();
        } catch (error) {
            console.error("Ошибка при удалении комментария:", error);
        }
    }
}

export const commentStore = new CommentStore();
