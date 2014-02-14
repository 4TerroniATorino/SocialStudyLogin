# Copy this file into secrets.py and set keys, secrets and scopes.

# This is a session secret key used by webapp2 framework.
# Get 'a random and long string' from here: 
# http://clsc.net/tools/random-string-generator.php
# or execute this from a python shell: import os; os.urandom(64)
SESSION_KEY = "a very long and secret session key goes here"

# Google APIs
GOOGLE_APP_ID = '732826816917'
GOOGLE_APP_SECRET = 'FD7ZTfUDeGtXHj2_tViv3FF4'

# Facebook auth apis
FACEBOOK_APP_ID = '450980025001888'
FACEBOOK_APP_SECRET = 'd5ca5fda7506e0bb9ac7e8c86db5af55'

# config that summarizes the above
AUTH_CONFIG = {
  # OAuth 2.0 providers
  'google'      : (GOOGLE_APP_ID, GOOGLE_APP_SECRET,
                  'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email'),
  'facebook'    : (FACEBOOK_APP_ID, FACEBOOK_APP_SECRET,
                  'user_about_me,email'),

  # OpenID doesn't need any key/secret
}
