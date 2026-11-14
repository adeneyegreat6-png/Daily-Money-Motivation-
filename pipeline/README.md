# Daily video pipeline
Each video is one HTML file drawing a 20s animation on a canvas via render(t). It loads common.js (stick figures, text, coins, pops).
- Portrait 1080x1920 by default; `?wide=1` switches to native 1920x1080 (see lowinc.html for the single-file WIDE pattern with a layout object L).
- Render: `ANIM=x.html node render.js full frames` (portrait) and `ANIM=x.html QS='?wide=1' VW=1920 VH=1080 node render.js full framesw`. Preview: mode `preview` with TIMES=comma list.
- Audio: copy an a_*.py, change SFX timings, output WAV.
- Encode: `ffmpeg -framerate 30 -i frames/%04d.png -i a.wav -c:v libx264 -crf 18 -preset veryfast -pix_fmt yuv420p -c:a aac -b:a 192k -shortest out.mp4`
Spec: original characters; 20s; hook header at top, story with real checked numbers, one-line end message at top, subscribe CTA at the BOTTOM: 9:16 shows "Subscribe & follow Daily Money Motivation" with a red Subscribe→Subscribed (bell) button and a yellow Follow→Following button; 16:9 shows "Subscribe for a new money habit every day" with the Subscribe→Subscribed button (see payday.html cta/btn + bell()); small disclaimer "Illustration only ... Not financial advice."
