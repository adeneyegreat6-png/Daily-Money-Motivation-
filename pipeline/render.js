const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const mode = process.argv[2] || 'preview';
  const out = process.argv[3] || 'frames';
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: +(process.env.VW||1080), height: +(process.env.VH||1920) } });
  await page.goto('file://' + path.resolve(__dirname, process.env.ANIM||'anim.html') + (process.env.QS||''));
  await page.evaluate(() => document.fonts.ready);
  const fps = 30;
  const times = mode === 'preview'
    ? (process.env.TIMES||'0.4,2.5,4.0,7.0,9.5,11.8,14.5,16.2,17.5,19.5').split(',').map(Number)
    : Array.from({ length: Math.round(20 * fps) }, (_, i) => i / fps);
  for (let i = 0; i < times.length; i++) {
    const url = await page.evaluate(t => { render(t); return document.getElementById('c').toDataURL('image/png'); }, times[i]);
    fs.writeFileSync(path.join(out, String(i).padStart(4, '0') + '.png'), Buffer.from(url.split(',')[1], 'base64'));
  }
  await browser.close();
})();
