import React, { useEffect, useState } from 'react';
import { observer } from 'mobx-react';
import { commentStore } from '../stores/CommentStore';

const Comment = observer (({ comment }) => {
    const [isReplying, setIsReplying] = useState(false);
    const [replyText, setReplyText] = useState("");

    const handleReply = () => {
        commentStore.addComment(replyText, comment.id);
        setReplyText("");
        setIsReplying(false);
    };

    const handleDelete = () => {
        if (window.confirm('Вы уверены, что хотите удалить комментарий?')) {
            commentStore.deleteComment(comment.id);
        }
    };

    return (
        <div style={{ marginLeft: comment.parent ? '20px' : '0' }}>
            <div>{comment.author_name}: {comment.text}: {comment.created_dt}</div>
            <button onClick={handleDelete}>Удалить</button>
            <button onClick={() => setIsReplying(!isReplying)}>Ответить</button>
            {isReplying && (
                <div>
                    <textarea value={replyText} onChange={e => setReplyText(e.target.value)} />
                    <button onClick={handleReply}>Отправить</button>
                </div>
            )}
            {comment.children && comment.children.map(child => <Comment key={child.id} comment={child} />)}
        </div>
    );
});

const CommentTree = observer(() => {
    const [newCommentText, setNewCommentText] = useState("");

    useEffect(() => {
        commentStore.fetchComments();
    }, []);

    const handleAddComment = async () => {
        if (newCommentText.trim()) {
            await commentStore.addComment(newCommentText);
            setNewCommentText("");
        }
    };

    return (
        <div>
            <div>
                <textarea
                    value={newCommentText}
                    onChange={(e) => setNewCommentText(e.target.value)}
                    placeholder="Напишите комментарий..."
                />
                <button onClick={handleAddComment}>Добавить комментарий</button>
            </div>
            {Array.isArray(commentStore.comments) ? (
                commentStore.comments.map(comment => (
                    comment.parent === null && <Comment key={comment.id} comment={comment} />
            ))
            ) : (
                <div>Комментарии не загружены или произошла ошибка.</div>
            )}
        </div>
    );
});

export default CommentTree;
