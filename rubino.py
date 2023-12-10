'''rubino is a simple libray for rubino-bot-selfs'''

from requests import session
from random import randint


class BaseMethod:
    client: dict = {
        'app_name': 'Main',
        'app_version': '3.0.1',
        'lang_code': 'en',
        'package': 'app.rubino.main',
        'platform': 'Android'
    }

    def url(self) -> str:
        return f'https://rubino{randint(1, 20)}.iranlms.ir/'

    video: str = 'Video'
    picture: str = 'Picture'


class Client(BaseMethod):

    def __init__(self, auth: str) -> None:
        self.session = session()
        self.auth = auth


    def post(self, **kwargs) -> dict:
        while True:
            with self.session.post(self.url(), **kwargs) as res:
                if res.status_code != 200: continue
                return res.json()


    def makeJson(self, method: str, data: dict) -> dict:
        json = {
            'api_version': '0',
            'auth': self.auth,
            'client': self.client,
            'data': data,
            'method': method
        }
        return json


    async def get_post_by_share_link(self, share_link: str, profile_id: str = None) -> dict:
        json = self.makeJson(
            'getPostByShareLink',
            {
              'share_string': share_link.split('/')[-1],
              'profile_id': profile_id
            })
        return self.post(json=json)



    async def is_exist_username(self, username: str) -> dict:
        json = self.makeJson(
            'isExistUsername',
            {
                'username': username.split('@')[-1]
            })
        return self.post(json=json)



    async def get_profile_list(
            self,
            limit: int = 10,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getProfileList',
            {
                'limit': limit,
                'sort': sort,
                'equal': equal
            }
        )
        return self.post(json=json)


    async def get_profile_info(self, target_profile_id: str):
        json = self.makeJson(
            'getMyProfileInfo',
            {
                'profile_id': target_profile_id
            })
        return self.post(json=json)


    async def follow(self, followee_id: str, profile_id: str = None) -> dict:
        json = self.makeJson(
            'requestFollow',
            {
              'f_type':'Follow',
              'followee_id': followee_id,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def unfollow(self, followee_id: str, profile_id: str = None) -> dict:
        json = self.makeJson(
            'requestFollow',
            {
                'f_type': 'Unfollow',
                'followee_id': followee_id,
                'profile_id': profile_id
            })
        return self.post(json=json)


    async def create_page(self, **kwargs) -> dict:
        '''createPage(
            bio='',
            name='',
            username='',
            email='',phone='',
            website=''
            )'''
        json = self.makeJson('createPage', {**kwargs})
        return self.post(json=json)


    async def remove_page(self, profile_id: str, record_id: str) -> dict:
        json = self.makeJson(
            'removeRecord',
            {
             'model': 'Profile',
             'record_id': record_id,
             'profile_id': profile_id
            })
        return self.post(json=json)


    async def update_profile(self, **kwargs) -> dict:
        '''updateProfile(
            bio='',
            name='',
            username='',
            email='',
            phone='',
            website='',
            is_message_allowed=True or False,
            is_mute=True or False,
            profile_status='Public' or 'Private'
            )'''
        json = self.makeJson('updateProfile', {**kwargs})
        return self.post(json=json)


    async def add_comment(
            self,
            text: str,
            post_id: str,
            post_profile_id: str,
            profile_id: str = None
    ) -> dict:
        json = self.makeJson(
            'addComment',
            {
              'content': text,
              'post_id': post_id,
              'post_profile_id': post_profile_id,
              'rnd': randint(100000000, 999999999),
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def like(self, post_id: str, post_profile_id: str, profile_id: str = None) -> dict:
        json = self.makeJson(
            'likePostAction',
            {
              'action_type': 'Like',
              'post_id': post_id,
              'post_profile_id': post_profile_id,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def unlike(self, post_id: str, post_profile_id: str, profile_id: str = None) -> dict:
        json = self.makeJson(
            'likePostAction',
            {
              'action_type': 'Unlike',
              'post_id': post_id,
              'post_profile_id': post_profile_id,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def view(self, post_id: str, post_profile_id: str) -> dict:
        json = self.makeJson(
            'addPostViewCount',
            {
              'post_id': post_id,
              'post_profile_id': post_profile_id
            })
        return self.post(json=json)


    async def get_comments(
            self,
            post_id: str,
            post_profile_id: str,
            profile_id: str = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getComments',
            {
              'equal': equal,
              'limit': limit,
              'sort': sort,
              'post_id': post_id,
              'profile_id': profile_id,
              'post_profile_id': post_profile_id
            })
        return self.post(json=json)


    async def get_profile_posts(
            self,
            target_profile_id: str,
            profile_id: str = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getRecentFollowingPosts',
            {
              'equal': equal,
              'limit': limit,
              'sort': sort,
              'profile_id': profile_id,
              'target_profile_id': target_profile_id
            })
        return self.post(json=json)


    async def get_profiles_stories(self, profile_id: str, limit: int = 100) -> dict:
        json = self.makeJson(
            'getProfilesStories',
            {
              'limit': limit,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def get_recent_following_posts(
            self,
            profile_id: str,
            limit: int = 30,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getRecentFollowingPosts',
            {
              'equal': equal,
              'limit': limit,
              'sort': sort,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def request_up_load_file(
            self,
            profile_id: str,
            file_name: str,
            file_size: int,
            file_type: str
    ) -> dict:
        json = self.makeJson(
            'requestUploadFile',
            {
              'file_name': file_name.split('/')[-1],
              'file_size': file_size,
              'file_type': file_type,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def get_profile_high_lights(
            self,
            profile_id: str,
            target_profile_id: str,
            limit: int = 10,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getProfileHighlights',
            {
              'equal': equal,
              'limit': limit,
              'sort': sort,
              'target_profile_id': target_profile_id,
              'profile_id': profile_id
              })
        return self.post(json=json)


    async def get_bookmarked_posts(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getBookmarkedPosts',
            {
              'equal': equal,
              'limit': limit,
              'sort': sort,
              'profile_id': profile_id
              })
        return self.post(json=json)


    async def get_explore_posts(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False,
            max_id: str = None
    ) -> dict:
        json = self.makeJson(
            'getExplorePosts',
            {
              'equal': equal,
              'limit': limit,
              'sort': sort,
              'max_id': max_id,
              'profile_id': profile_id
              })
        return self.post(json=json)


    async def get_blocked_profiles(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getBlockedProfiles',
            {
             'equal': equal,
              'limit': limit,
              'sort': sort,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def get_profile_followers(
            self,
            profile_id: str,
            target_profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getProfileFollowers',
             {
               'equal': equal,
               'f_type': 'Follower',
               'limit': limit,
               'sort': sort,
               'target_profile_id': target_profile_id,
               'profile_id': profile_id
             })
        return self.post(json=json)


    async def get_profile_followings(
            self,
            profile_id: str,
            target_profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getProfileFollowers',
             {
               'equal': equal,
               'f_type': 'Following',
               'limit': limit,
               'sort': sort,
               'target_profile_id': target_profile_id,
               'profile_id': profile_id
             })
        return self.post(json=json)


    async def get_profile_info(self, profile_id: str, target_profile_id: str) -> dict:
        json = self.makeJson(
            'getProfileInfo',
            {
              'profile_id': profile_id,
              'target_profile_id': target_profile_id
            })
        return self.post(json=json)


    async def block_profile(self, profile_id: str, blocked_id: str) -> dict:
        json = self.makeJson(
            'setBlockProfile',
             {
               'action':'Block',
               'blocked_id': blocked_id,
               'profile_id': profile_id
               })
        return self.post(json=json)


    async def un_block_profile(self, profile_id: str, blocked_id: str) -> dict:
        json = self.makeJson(
            'setBlockProfile',
             {
               'action': 'Unblock',
               'blocked_id': blocked_id,
               'profile_id': profile_id
               })
        return self.post(json=json)


    async def get_my_archive_atories(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        json = self.makeJson(
            'getMyArchiveStories',
            {
             'equal': equal,
              'limit': limit,
              'sort': sort,
              'profile_id': profile_id
            })
        return self.post(json=json)


    async def add_post(
            self,
            profile_id: str,
            file: str,
            caption: str = None,
            file_type: str = BaseMethod.picture
    ) -> dict:
        result = self.uploadFile(file, profile_id, file_type)
        json = self.makeJson('addPost', {
            'rnd': int(random() * 1e6 + 1),
            'width': 720,
            'height': 720,
            'caption': caption,
            'file_id': result[1]['file_id'],
            'post_type': file_type,
            'profile_id': profile_id,
            'hash_file_receive': result[0]['hash_file_receive'],
            'thumbnail_file_id': result[1]['file_id'],
            'thumbnail_hash_file_receive': result[0]['hash_file_receive'],
            'is_multi_file': False
            })
        return self.post(json=json)
