# Getting a YouTube API Key
## One-time setup for the YouTube Comment Collector

For HW3 and HW4 you can collect comments from a YouTube video of your choice with the **YouTube Comment Collector** notebook. To do that, the notebook needs a **YouTube API key**. Getting one is free, takes about 10 minutes, and you only do it once. Do steps 1–3 anytime; do step 4 on Day 10 (Mon 11/9), when the notebook opens. Finish all four before Friday 11/13.

## What's an API key?

An **API** (application programming interface) is a door a company builds so programs can request data in an orderly way, instead of scraping web pages. YouTube's door requires a **key**: a long, password-like string that identifies you.

## 1. Create a Google Cloud project

Go to [console.cloud.google.com](https://console.cloud.google.com) and sign in with **the same Gmail account you use for Colab**. Accept the terms if asked. Click the project menu at the top → **New Project**, name it something like `writ20833`, and click **Create**. Make sure the new project is selected in that top menu.

## 2. Turn on the YouTube Data API v3

In the search bar at the top, type **YouTube Data API v3**, open it, and click **Enable**.

## 3. Create the key

Go to **APIs & Services → Credentials → + Create credentials → API key**, then copy the key.

*Optional but wise:* click **Edit API key**. Under *API restrictions*, choose **Restrict key → YouTube Data API v3** so the key can't be used for anything else. Leave *Application restrictions* at **None**, because Colab can't work with a website or IP-address restriction.

You don't need a credit card or billing.

## 4. Save the key in Colab Secrets

Open **your copy** of the YouTube Comment Collector notebook. Click the **🔑 key icon** in the left sidebar → **Add new secret**. Set **Name** to exactly `YOUTUBE_API_KEY`, paste your key as the **Value**, and switch **Notebook access** on.

## Keep your key private

Treat it like a password. Don't paste it into a code cell, a discussion post, a screenshot, or a chat. Secrets belong to *your* Google account, not to the notebook, so sharing a notebook doesn't share your key. If a key ever leaks, delete it on the Credentials page and create a new one.

## How much can you collect?

Each project gets 10,000 free "units" a day, and each request costs 1 unit. One request brings back up to 100 comments, so 500 comments costs about 6 units. You won't run out unless you collect replies from a very large video many times over.

## If something goes wrong

- **"No secret named YOUTUBE_API_KEY":** check the name's spelling and capitals in the 🔑 panel.
- **"Notebook isn't allowed to read it":** switch on **Notebook access** next to the secret.
- **Still stuck?** Bring it to class on Day 12, or ask the [Code Guide](../chatbot.html).
