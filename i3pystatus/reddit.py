#!/usr/bin/env python

import re
import praw

from i3pystatus import IntervalModule
from i3pystatus.core.util import internet, require, user_open


class Reddit(IntervalModule):
    """
    This module fetches and displays posts and/or user mail/messages from
    reddit.com. Left-clicking on the display text opens the permalink/comments
    page using webbrowser.open() while right-clicking opens the URL of the
    submission directly. Depends on the Python Reddit API Wrapper (PRAW)
    <https://github.com/praw-dev/praw>.

    PRAW must be configured for this module to work.
    https://praw.readthedocs.io/en/latest/

    .. rubric:: Available formatters

    * {submission_title}
    * {submission_author}
    * {submission_points}
    * {submission_comments}
    * {submission_permalink}
    * {submission_url}
    * {submission_domain}
    * {submission_subreddit}
    * {message_unread}
    * {message_author}
    * {message_subject}
    * {message_body}
    * {link_karma}
    * {comment_karma}

    """

    settings = (
        ("format", "Format string used for output."),
        ("username", "Reddit username."),
        ('keyring_backend', 'alternative keyring backend for retrieving \
                            credentials'),
        ("subreddit", "Subreddit to monitor. Uses frontpage if unspecified."),
        ("sort_by", "'hot', 'new', 'rising', 'controversial', or 'top'."),
        ("time_filter", "'all', 'day','hour', 'month', 'week', 'year'"),
        ("color", "Standard color."),
        ("colorize", "Enable color change on new message."),
        ("color_orangered", "Color for new messages."),
        ("mail_brackets", "Display unread message count in square-brackets."),
        ("title_maxlen", "Maximum number of characters to display in title."),
        ("interval", "Update interval."),
        ("status", "New message indicator."),
    )
    format = "[{submission_subreddit}] {submission_title} ({submission_domain})"
    username = ""
    keyring_backend = None
    subreddit = ""
    sort_by = "hot"
    time_filter = "all"
    color = "#FFFFFF"
    colorize = True
    color_orangered = "#FF4500"
    mail_brackets = False
    title_maxlen = 80
    interval = 300
    status = {
        "new_mail": "âœ‰",
        "no_mail": "",
    }

    on_leftclick = "open_permalink"

    _permalink = ""
    _url = ""

    subreddit_pattern = re.compile(r"{submission_\w+}")
    message_pattern = re.compile(r"{message_\w+\}")
    user_pattern = re.compile(r"{comment_karma}|{link_karma}")

    reddit_session = None

    @require(internet)
    def run(self):
        pass

    def connect(self):
        pass

    def get_redditor(self, reddit):
        pass

    def get_messages(self, reddit):
        pass

    def get_subreddit(self, reddit):
        pass

    def open_mail(self):
        pass

    def open_permalink(self):
        pass

    def open_link(self):
        pass
