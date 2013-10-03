pebblefish
==========

a social networking site where we value protecting user privacy and enhancing online communication


What it is
----------

Pebblefish allows users to form groups with others. A group can be as small as 2 or as large as 100. Users share content within groups, unlike other sites where users share on persanal walls. Unlike other sites, we value small-scale communication within tight groups of friends rather than large-scale broadcast updates that are often ignored by acquaintences. Rather than try and filter 'relevant' content, we believe users know who to share with, and we give users the ability to share inside stories within a circle of friends who would actually get the content.

How it works
------------
Pebblefish is a social peer-to-peer network application. Content is stored locally and shared when users are online together. All content is encypted using AES, and communications are encrypted. A list of usernames and public data (public posts, aka 'followable' posts) are stored on central servers. There are 3 levels of content: group, public, and followable. Group content is encrypted using a key that is the product of the keys of the group and is stored on each member's local system. Public content is encrypted using the user's key and is stored on the user's and friends' systems. Public content is stored temporarily if a user is not the onwer. If the user is a friend, public content is stored locally for a month. If the user is an acquaintance, public content is not stored. Users can only have 128 friends. Followable content is unencrypted and stored on central servers. Followable content can only be managed by Goldfish users and can be accessed by anyone.
