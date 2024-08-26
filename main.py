import instaloader

USERNAME = '<username>'
PASSWORD = '<password>'

PROFILES = ['<names_of_profiles>']

L = instaloader.Instaloader()

try:
    L.load_session_from_file(USERNAME)
except FileNotFoundError:
    try:
        L.login(USERNAME, PASSWORD)
        L.save_session_to_file()
    except instaloader.exceptions.InstaloaderException as e:
        print(f"LOgin failed: {e}")
        exit()



def download_new_posts(profile):
    print(f"Downloading posts from profile: {profile.username}...")
    try:
        for post in profile.get_posts():
            try:
                L.download_post(post, profile.username)
            except Exception as e:
                print(f"Downloading post failed {profile.username}: {e}")
    except Exception as e:
        print(f"Downloading posts failed {profile.username}: {e}")



def download_stories(profile):
    print(f"Downloading stories from: {profile.username}...")
    try:
        stories = L.get_stories(userids=[profile.userid])
        for story in stories:
            for item in story.get_items():
                try:
                    L.download_storyitem(item, profile.username)
                except Exception as e:
                    print(f"Downloading story failed {profile.username}: {e}")
    except Exception as e:
        print(f"Downloading stories failed {profile.username}: {e}")



for profile_name in PROFILES:
    try:
        profile = instaloader.Profile.from_username(L.context, profile_name)
        download_new_posts(profile)
    except instaloader.exceptions.ProfileNotExistsException as e:
        print(f"Can't find profile {profile_name}: {e}")
    except Exception as e:
        print(f"Profile processing failed {profile_name}: {e}")



for profile_name in PROFILES:
    try:
        profile = instaloader.Profile.from_username(L.context, profile_name)
        download_stories(profile)
    except instaloader.exceptions.ProfileNotExistsException as e:
        print(f"Can't find profile {profile_name}: {e}")
    except Exception as e:
        print(f"Profile processing failed {profile_name}: {e}")
