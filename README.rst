Objectifier
===========

Objectifier is a tool that makes traversing dictionaries, lists, and other
Python objects a lot easier.

If you have an bug to report or a feature request, add it to our `issue tracker
<https://github.com/elmcitylabs/objectifier/issues>`_.

.. _installation:

Installation
------------

Objectifier is on `PyPi`_. You can install it through `pip`_ or easy_install,
whichever you prefer. ::

    $ pip install objectifier

.. _pip: http://www.pip-installer.org/en/latest/
.. _PyPi: http://pypi.python.org

.. _configuration:

Usage
-----

Objectifier takes any Python object--a string, dictionary, list, tuple,
etc--and turns it into an object with some pretty cool properties.

The best way to explain is through some examples. Let's say you are interacting
with the Twitter API and have `a JSON tweet`_ that you'd like to manipulate or
traverse.

.. _a JSON tweet: javascript:toggleTweet();

.. raw:: html

    <script type='text/javascript'>
      $(function() {
        $.getJSON("https://api.twitter.com/1/statuses/show.json?id=112652479837110273&include_entities=true&callback=?", function(json) {
          $("pre#tweet").html(JSON.stringify(json, null, 4));
        });
      });

      var tweetHidden = true;
      function toggleTweet() {
        if (tweetHidden) {
          tweetHidden = false;
          $("pre#tweet").fadeIn();
        }
        else {
          tweetHidden = true;
          $("pre#tweet").fadeOut();
        }
      }
    </script>
    <div class='highlight-js'><div class='highlight'><pre id='tweet' style='display:none'></pre></div></div>


After parsing the response into a Python dictionary using the ``json``
module, this is how we might display all the user mentions in a list. ::

    >>> tweet = json.loads(response.read())
    >>> ", ".join(user['screen_name'] for user in tweet['entities']['user_mentions'])

This isn't too different than what you'd do with Objectifier. The main
difference is that you can access attributes with dot notation. ::

    >>> tweet = Objectifier(response.read())
    >>> ", ".join(user.screen_name for user in tweet.entities.user_mentions)

The ``Objectifier`` class will wrap any Python string, unicode string,
dictionary, list, or tuple. If the input is a JSON string, Objectifier will
attempt to parse it before leaving it as text only. This allows you to do
things like the above, without having to use ``json.load`` for the response
data.

You can test that an attribute exists (as you could with a dictionary). ::

    >>> 'user' in tweet
    True

And get the number of items in an object that defines ``__len__``. ::

    >>> len(tweet.entities.user_mentions)
    3

The above things are nice, but not game changers. Objectifier's real strength
shines in the Python console. ::

    >>> tweet
    <Objectifier#dict user=dict favorited=bool entities=dict contributors=NoneType truncated=bool text=unicode created_at=unicode retweeted=bool in_reply_to_status_id_str=NoneType coordinates=NoneType in_reply_to_user_id_str=unicode source=unicode in_reply_to_status_id=NoneType in_reply_to_screen_name=unicode id_str=unicode place=NoneType retweet_count=int geo=NoneType id=int possibly_sensitive=bool in_reply_to_user_id=int>

Everything in the object is recursively wrapped with Objectifier, so attributes
of the original object get all the benefits of pretty display. For example ::

    >>> tweet.user
    <Objectifier#dict follow_request_sent=NoneType profile_use_background_image=bool default_profile_image=bool id=int verified=bool profile_image_url_https=unicode profile_sidebar_fill_color=unicode profile_text_color=unicode followers_count=int profile_sidebar_border_color=unicode id_str=unicode profile_background_color=unicode listed_count=int profile_background_image_url_https=unicode utc_offset=NoneType statuses_count=int description=unicode friends_count=int location=unicode profile_link_color=unicode profile_image_url=unicode following=NoneType show_all_inline_media=bool geo_enabled=bool profile_background_image_url=unicode screen_name=unicode lang=unicode profile_background_tile=bool favourites_count=int name=unicode notifications=NoneType url=unicode created_at=unicode contributors_enabled=bool time_zone=NoneType protected=bool default_profile=bool is_translator=bool>
    >>> tweet.user.profile_image_url
    u'http://a0.twimg.com/profile_images/1380912173/Screen_shot_2011-06-03_at_7.35.36_PM_normal.png'

If you're inspecting a list, Objectifier will tell you the number of elements. ::

    >>> tweet.entities.user_mentions
    <Objectifier#list elements:3>

And finally, if you use IPython, pressing tab will give you a nice rundown of
all the attributes in the object. ::

    >>> tweet.<tab>
    ...contributors               ...id                         ...in_reply_to_user_id_str    ...source
    ...coordinates                ...id_str                     ...objectify_if_needed        ...text
    ...created_at                 ...in_reply_to_screen_name    ...place                      ...truncated
    ...entities                   ...in_reply_to_status_id      ...possibly_sensitive         ...user
    ...favorited                  ...in_reply_to_status_id_str  ...retweet_count
    ...geo                        ...in_reply_to_user_id        ...retweeted

There are probably a lot of other things Objectifier could do too, so if you
have an idea, fork the code on `Github
<https://github.com/elmcitylabs/objectifier>`_ or `bitbucket
<https://bitbucket.org/elmcitylabs/objectifier>`_ and send us a pull request!

Contributing, feedback, and questions
-------------------------------------

* Github: https://github.com/elmcitylabs/objectifier
* Bitbucket: http://bitbucket.com/elmcitylabs/objectifier
* Email: opensource@elmcitylabs.com.
* Twitter: `@elmcitylabs <http://twitter.com/elmcitylabs>`_

