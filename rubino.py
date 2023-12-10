'''rubino is a simple libray for rubino-bot-selfs'''

from requests import session
from random import randint

from methods import Methods


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
        return await Methods.GetPostByShareLink(self, share_link, profile_id)


    async def is_exist_username(self, username: str) -> dict:
        return await Methods.IsExistUsername(self, username)


    async def get_profile_list(self, limit: int = 10, sort: str = 'FromMax', equal: bool = False) -> dict:
        return await Methods.GetProfileList(self, limit, sort, equal)


    async def get_profile_info(self, profile_id: str):
        return await Methods.GetProfileInfo(self, profile_id)


    async def follow(self, followee_id: str, profile_id: str = None) -> dict:
        return await Methods.Follow(self, followee_id, profile_id)


    async def unfollow(self, followee_id: str, profile_id: str = None) -> dict:
        return await Methods.UnFollow(self, followee_id, profile_id)


    async def create_page(self, **kwargs) -> dict:
        '''createPage(
            bio='',
            name='',
            username='',
            email='',phone='',
            website=''
            )'''
        return await Methods.CreatePage(self, **kwargs)


    async def remove_page(self, profile_id: str, record_id: str) -> dict:
        return await Methods.RemovePage(self, profile_id, record_id)


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
        return await Methods.UpdateProfile(self, **kwargs)


    async def add_comment(
            self,
            text: str,
            post_id: str,
            post_profile_id: str,
            profile_id: str = None
    ) -> dict:
        return await Methods.AddComment(self, text, post_id, post_profile_id, profile_id)


    async def like(self, post_id: str, post_profile_id: str, profile_id: str = None) -> dict:
        return await Methods.Like(self, post_id, post_profile_id, profile_id)


    async def unlike(self, post_id: str, post_profile_id: str, profile_id: str = None) -> dict:
        return await Methods.UnLike(self, post_id, post_profile_id, profile_id)


    async def view(self, post_id: str, post_profile_id: str) -> dict:
        return await Methods.View(self, post_id, post_profile_id)


    async def get_comments(
            self,
            post_id: str,
            post_profile_id: str,
            profile_id: str = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods.GetComments(self, post_id, post_profile_id, profile_id, sort, limit, equal)


    async def get_profile_posts(
            self,
            target_profile_id: str,
            profile_id: str = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods.GetProfilePosts(self, target_profile_id, profile_id, limit, sort, equal)


    async def get_profiles_stories(self, profile_id: str, limit: int = 100) -> dict:
        return await Methods.GetProfilesStories(self, profile_id, limit)


    async def get_recent_following_posts(
            self,
            profile_id: str,
            limit: int = 30,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods.GetRecentFollowingPosts(self, profile_id, limit, sort, equal)



    async def request_up_load_file(
            self,
            profile_id: str,
            file_name: str,
            file_size: int,
            file_type: str
    ) -> dict:
        return Methods.RequestUpLoadFile(self, profile_id, file_name, file_size, file_type)


    async def get_bookmarked_posts(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods.GetBookmarkedPosts(self, profile_id, limit, sort, equal)



    async def get_explore_posts(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False,
            max_id: str = None
    ) -> dict:
        return await Methods.GetExplorePosts(self, profile_id, limit, sort, equal, max_id)



    async def get_blocked_profiles(
            self,
            profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods.GetBlockedProfiles(self, profile_id, limit, sort, equal)



    async def get_profile_followers(
            self,
            profile_id: str,
            target_profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods.GetProfileFollowers(self, profile_id, target_profile_id, limit, sort, equal)


    async def get_profile_followings(
            self,
            profile_id: str,
            target_profile_id: str,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        return await Methods.GetProfileFollowings(self, profile_id, target_profile_id, limit, sort, equal)


    async def block_profile(self, profile_id: str, blocked_id: str) -> dict:
        return await Methods.BlockProfile(self, profile_id, blocked_id)


    async def un_block_profile(self, profile_id: str, blocked_id: str) -> dict:
        return await Methods.UnBlockProfile(self, profile_id, blocked_id)


    async def add_post(
            self,
            profile_id: str,
            file: str,
            caption: str = None,
            file_type: str = BaseMethod.picture
    ) -> dict:
        return await Methods.AddPost(self, profile_id, file, caption, file_type)
