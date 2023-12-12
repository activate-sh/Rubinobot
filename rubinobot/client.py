'''rubino is a simple libray for rubino-bot-selfs'''

from requests import session
from .methods import Methods, randint


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


class Client(BaseMethod):

    def __init__(self, auth: str) -> None:
        self.session = session()
        self.auth = auth

    def __enter__(self) -> None:
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.session.close()

    def makeJson(self, method: str, data: dict) -> dict:
        json: dict = {
            'api_version': '0',
            'auth': self.auth,
            'client': self.client,
            'data': data,
            'method': method
        }
        return json


    def post(self, **kwargs) -> dict:
        while True:
            with self.session.post(self.url(), **kwargs) as res:
                if res.status_code != 200: continue
                return res.json()


    async def is_exist_username(self, username: str) -> dict:
        return await Methods._is_exist_username(self, username)


    async def get_profile_info(self, profile_id: str):
        return await Methods._get_profile_info(self, profile_id)


    async def get_profile_id_by_username(self, username):
        return await Methods._get_profile_id_by_username(self, username)


    async def get_post_by_share_link(self, share_link: str, profile_id: str = None) -> dict:
        return await Methods._get_post_by_share_link(self, share_link, profile_id)


    async def get_me(self, profile_id: str = None) -> dict:
        return await Methods._get_me(self, profile_id)


    async def get_my_archive_atories(
            self,
            profile_id: str = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods._get_my_archive_atories(self, profile_id, limit, sort, equal)


    async def follow(self, followee_id: str, profile_id: str = None) -> dict:
        return await Methods._follow(self, followee_id, profile_id)


    async def un_follow(self, followee_id: str, profile_id: str = None) -> dict:
        return await Methods._un_follow(self, followee_id, profile_id)


    async def create_page(self, **kwargs) -> dict:
        '''create_page(
            bio='',
            name='',
            username='',
            email='',phone='',
            website=''
            )'''
        return await Methods._create_page(self, **kwargs)


    async def remove_page(self, profile_id: str, record_id: str) -> dict:
        return await Methods._remove_page(self, profile_id, record_id)


    async def update_profile(self, **kwargs) -> dict:
        '''update_profile(
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
        return await Methods._update_profile(self, **kwargs)


    async def add_comment(
            self,
            text: str,
            post_id: str,
            post_profile_id: str,
            profile_id: str = None
    ) -> dict:
        return await Methods._add_comment(self, text, post_id, post_profile_id, profile_id)


    async def like(self, post_id: str, post_profile_id: str, profile_id: str = None) -> dict:
        return await Methods._like(self, post_id, post_profile_id, profile_id)


    async def un_like(self, post_id: str, post_profile_id: str, profile_id: str = None) -> dict:
        return await Methods._un_like(self, post_id, post_profile_id, profile_id)


    async def view(self, post_id: str, post_profile_id: str) -> dict:
        return await Methods._view(self, post_id, post_profile_id)


    async def get_comments(
            self,
            post_id: str,
            post_profile_id: str,
            profile_id: str = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods._get_comments(
            self, post_id, post_profile_id, profile_id, sort, limit, equal)


    async def get_profile_posts(
            self,
            target_profile_id: str,
            profile_id: str = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods._get_profile_posts(self, target_profile_id, profile_id, limit, sort, equal)


    async def get_profiles_stories(self, profile_id: str, limit: int = 100) -> dict:
        return await Methods._get_profiles_stories(self, profile_id, limit)


    async def get_recent_following_posts(
            self,
            profile_id: str,
            limit: int = 30,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods._get_recent_following_posts(self, profile_id, limit, sort, equal)


    async def get_bookmarked_posts(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods._get_bookmarked_posts(self, profile_id, limit, sort, equal)


    async def get_explore_posts(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False,
            max_id: str = None
    ) -> dict:
        return await Methods._get_explore_posts(self, profile_id, limit, sort, equal, max_id)


    async def get_blocked_profiles(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods._get_blocked_profiles(self, profile_id, limit, sort, equal)


    async def get_profile_followers(
            self,
            profile_id: str,
            target_profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods._get_profile_followers(
            self, profile_id, target_profile_id, limit, sort, equal)


    async def get_profile_followings(
            self,
            profile_id: str,
            target_profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods._get_profile_followings(
            self, profile_id, target_profile_id, limit, sort, equal)


    async def block_profile(self, profile_id: str, blocked_id: str) -> dict:
        return await Methods._block_profile(self, profile_id, blocked_id)


    async def un_block_profile(self, profile_id: str, blocked_id: str) -> dict:
        return await Methods._un_block_profile(self, profile_id, blocked_id)


    async def request_upload_file(
            self,
            profile_id: str,
            file_name: str,
            file_size: int,
            file_type: str
    ) -> dict:
        return await Methods._request_upload_file(self, profile_id, file_name, file_size, file_type)


    async def upload_file(self, file: str, file_type: str, profile_id: str = None) -> dict:
        return await Methods._upload_file(self, file, profile_id, file_type)


    async def add_post(
            self,
            profile_id: str,
            file: str,
            caption: str = None,
            file_type: str = 'Picture'
    ) -> dict:
        return await Methods._add_post(self, profile_id, file, caption, file_type)
