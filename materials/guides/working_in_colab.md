# Working in Colab
## Setup, saving your work, and turning it in

Every notebook in this course runs in **Google Colab**, a free tool that runs Python in your browser. There's nothing to install. This page covers getting set up, saving your work, and submitting it.

## Before your first class

- **You need a personal Gmail account.** Colab runs through Google, and your work is saved to that account's Google Drive.
- Bring a laptop with an up-to-date browser. Chrome works best with Colab.

## Opening a notebook

- **1.** Click a notebook's link on the course site (the home page or the **Schedule** page) or in TCU Online. It opens in Colab. Each notebook's link goes live on its class day.
- **2.** Go to **File → Save a copy in Drive** right away. The notebook you opened is the class original, and nothing you type in it is saved.
- **3.** Your copy opens in a new tab, named "Copy of …". Work in that tab. It's saved in your Google Drive, in a folder called **Colab Notebooks**.

## Running code

- Click a code cell and press **Shift + Enter**, or click the **▶** button at its left.
- The first run takes a few seconds while Colab starts up. After that it's quick.
- Run cells **from top to bottom**. Later cells often use names an earlier cell created.
- If things get confusing, **Runtime → Restart and run all** starts over cleanly.
- **Errors are normal.** Read the last line of the message, since it usually names the problem. Errors are part of the work here, not something to hide.

## Coming back later

- Open **your copy** from Google Drive (Colab Notebooks folder), or from **File → Open notebook** in Colab.
- Don't use the class link again. It opens a fresh, blank original.
- Colab forgets running results between sessions, so run the cells again when you come back. Your typing is still there.
- Files you upload into Colab (like a CSV for HW3 or HW4) are deleted when the session ends. Keep the original on your computer or in Drive.

## Submitting homework

- **1.** Put your name at the top of the notebook, and run every cell so your output shows.
- **2.** Go to **File → Download → Download .ipynb**.
- **3.** Rename the file `LASTNAME_HW1.ipynb` (HW2, HW3…).
- **4.** Upload it to that homework's folder in **TCU Online → Assignments**.

## When something goes wrong

- **"I lost my work":** check Drive → Colab Notebooks for a "Copy of …" file.
- **"My changes disappeared":** you were probably in the class original. Save a copy next time, and open it from Drive.
- **"NameError: name … is not defined":** an earlier cell didn't run. Use Runtime → Run all, or run the cells above it.
- **Still stuck?** Ask the [Code Guide](../chatbot.html), come to office hours, or ask in class.
