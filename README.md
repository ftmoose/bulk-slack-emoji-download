#Download all slack emojis from your workspace


##Setup
There's a little bit of a setup for my scripts to work properly, if anything is ambiguous feel free
to let me know via email *mr.rammo@gmail.com* with a subject **slack emojis**

First step is of course cloning this repo into a directory of your choice.

####Creating a slack browser session
So first thing we need to do is manually log into our slack workspace, modify the following link to your
workspace.
`https://<Your Workspace>.slack.com/customize/emoji`

That should take you to a slack login screen.  At this point you want to open up your browser's dev tools and
navigate to the network tab.  Log in.

After reaching the **Customize Your Workspace** page you should see multiple rest calls, the one we're
interested in hase a name similar to **checkcookie?redir=..** (If you're using chrome you can filter by 'other',
this will make the specific call easier to find).  Click on the call and scroll to the **Request Header** section.

We're going to need the cookie so go ahead and copy that value.  You'll need to keep your browser open for the
rest of these steps, so if you close it you may need to start from the beggining.

####Editing the config file
I've already created a config.json file, all you need to do is fill in the blank values.  Start by pasting the
cookie value we copied in the last step into it's corresponding field.

Then go ahead and enter the name of your workspace in the **slack-workspace** field.  No need to worry about the
outFile.

####Downloading dependencies
For this to work you're going to need python3 installed on your system, along with a few dependecies.
An easy way to be sure you have all the dependecies is to just run:
`pip3 install requests bs4 simplejson`

####The easy part
All we need to do now is open up a bash shell if you haven't already, navigate to wherever you cloned this repo
and run:
`./exec.sh`





