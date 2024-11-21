from api_client import ApiClient

class UserRepository:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_users(self):
        response = self.api_client.get('/users')
        return response.json()

    def get_user_by_id(self, user_id):
        response = self.api_client.get(f'/users/{user_id}')
        return response.json()

class PostRepository:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_posts(self):
        response = self.api_client.get('/posts')
        return response.json()

    def get_post_by_id(self, post_id):
        response = self.api_client.get(f'/posts/{post_id}')
        return response.json()

class CommentRepository:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_comments(self):
        response = self.api_client.get('/comments')
        return response.json()

    def get_comments_by_post_id(self, post_id):
        response = self.api_client.get(f'/posts/{post_id}/comments')
        return response.json()