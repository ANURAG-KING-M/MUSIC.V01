from Anuragmusicpro.core.bot import Loy
from AnuragMusicpro.core.dir import dirr
from AnuragMusicpro.core.git import git
from AnuragMusicpro.core.userbot import Userbot
from AnuragMusicpro.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Loy()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
