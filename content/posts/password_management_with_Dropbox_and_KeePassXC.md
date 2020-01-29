Title: Password management with Dropbox and KeePassXC
Date: 2020-01-28 20:20
Category: Blog
Tags: DIY
Author: Raymundo Cassani
Slug: password-management-with-Dropbox-and-KeePassXC
Summary: Nowadays we have to handle an enormous quantity of passwords. As it is not desirable to reuse passwords, nor to write down, it is necessary to have a way manage them. After research and thinking in advantages and drawbacks among the different methods, I came to the solution of using KeePassXC alongside with Dropbox.

<center>
[<img src="/images/keys.jpg" style="width: 600px;">](/images/keys.jpg)  
<a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px" href="https://unsplash.com/@contradirony?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from Samantha Lam"><span style="display:inline-block;padding:2px 3px"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-2px;fill:white" viewBox="0 0 32 32"><title>unsplash-logo</title><path d="M10 9V0h12v9H10zm12 5h10v18H0V14h10v9h12v-9z"></path></svg></span><span style="display:inline-block;padding:2px 3px">Samantha Lam</span></a>
</center>


Nowadays we have to handle an enormous quantity of passwords. As it is not desirable to reuse passwords, nor to write down, it is necessary to have a way manage them. My must- and nice-to-have list was:

1. Encrypted passwords
2. Passwords need to be always available, not depend on cloud storage
3. Being able to access them from different OS
4. Open-source software for encryption
5. Synchronization among unlimited devices

After research and thinking in advantages and drawbacks among the different methods, I came to the solution of using an offline password manager ([KeePassXC](https://keepassxc.org/)) and service to synchronize files ([Dropbox](https://www.dropbox.com/)).

[KeePassXC](https://keepassxc.org/) is an open-source cross-platform password manager that has has support for Windows, Linux, macOS. Although the there is not official, KeePassXC uses a database format that can be read and written with other [Android and iOS apps](https://keepassxc.org/docs/#faq-platform-mobile).  

To set up this password management strategy just:

1. Created a database with KeePassXC, and select a strong password for it. This password must be memorable as it should not be stored in any place but in your head.

2. Place the KeePassXC database file in a Dropbox folder. This will keep it synchronized in all your Dropbox devices.

This approach has worked very nice in my case, although it presents disadvantages such as:

* If the master password for the database is lost, all the passwords are locked.

* In March 2019, [Dropbox put a limit of 3 devices](https://help.dropbox.com/accounts-billing/settings-sign-in/computer-limit) for Basic (free) users, and two different OS in the same computer count as two devices.
