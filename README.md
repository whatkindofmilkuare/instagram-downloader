# Instagram Downloader

This Python script uses the `instaloader` library to download posts and stories from specified Instagram profiles. It handles login sessions, downloads new posts, and retrieves stories for the profiles listed.

## Features

- **Login Handling:** The script attempts to load a saved session. If no session is found, it logs in with the provided credentials and saves the session for future use.
- **Post Downloading:** Downloads all posts from the specified profiles.
- **Story Downloading:** Downloads all stories from the specified profiles.

## Requirements

- Python 3.x
- `instaloader` library

You can install the `instaloader` library using pip:

```bash
pip install instaloader
```

## Configuration

1. **Set Username and Password:**
   Replace `<username>` and `<password>` with your Instagram credentials in the script.

2. **Specify Profiles:**
   Replace `<names_of_profiles>` with the Instagram usernames of the profiles you want to download posts and stories from. For example:
   
   ```python
   PROFILES = ['profile1', 'profile2']
   ```

## Usage

1. **Clone or Download the Script:**
   Save the script to a file, for example `instagram_downloader.py`.

2. **Run the Script:**
   Execute the script using Python:

   ```bash
   python instagram_downloader.py
   ```

3. **Monitor Output:**
   The script will print messages indicating the progress of downloading posts and stories.

## Error Handling

- **Login Failures:** If login fails, an error message will be printed and the script will exit.
- **Profile Not Found:** If a specified profile does not exist, an error message will be printed.
- **Download Failures:** Any issues encountered during downloading posts or stories will be reported.

## Example

Here’s an example of how the script might look with actual values:

```python
import instaloader

USERNAME = 'your_username'
PASSWORD = 'your_password'

PROFILES = ['profile1', 'profile2']

L = instaloader.Instaloader()

try:
    L.load_session_from_file(USERNAME)
except FileNotFoundError:
    try:
        L.login(USERNAME, PASSWORD)
        L.save_session_to_file()
    except instaloader.exceptions.InstaloaderException as e:
        print(f"Login failed: {e}")
        exit()

# Functions to download posts and stories
# ...

for profile_name in PROFILES:
    try:
        profile = instaloader.Profile.from_username(L.context, profile_name)
        download_new_posts(profile)
        download_stories(profile)
    except instaloader.exceptions.ProfileNotExistsException as e:
        print(f"Can't find profile {profile_name}: {e}")
    except Exception as e:
        print(f"Profile processing failed {profile_name}: {e}")
```

## License

This script is provided as-is without warranty. Use it responsibly and in accordance with Instagram's terms of service.

Feel free to modify and extend the script to better suit your needs. Contributions and improvements are welcome!