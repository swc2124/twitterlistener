"""
-------------------
The Streamer Script
-------------------

This script calls the TweetspyStreamListener object from slistener.py.

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream

from slistener import TweetspyStreamListener as TSL
from tweetspy_lib import get_auth

# =========================================================================== #
# OPERATIONS

def main():

    try:

        # Get all 4 authorization values from helper library function.
        con_key, con_sec, acc_tok, acc_sec = get_auth()

        # Set the authorization handler.
        auth = OAuthHandler(con_key, con_sec)

        # Set access token and secret.
        auth.set_access_token(acc_tok, acc_sec)

        # Initialize the stream object.
        stream = Stream(auth, TSL())

        # Begin the filtered stream
        stream.filter(
            track=["a", "i", "#", "e", "."],
            async=True,
            stall_warnings=True)

    except Exception as err:
        print("<caught><exception> [{}]".format(err))
        main()

    except KeyboardInterrupt as err:
        import sys
        sys.exit(0)



if __name__ == '__main__':

    main()


# =========================================================================== #
