const { chromium } = require('D:/PROJECT/image-captioning-system-main/frontend/node_modules/playwright');
(async () => {
  const out = process.argv[2];
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  for (const [name, url] of [["fraud-radar", "https://fraud-radar-lilac.vercel.app/"], ["captioning", "https://image-captioning-system.vercel.app/"]]) {
    await page.goto(url, { waitUntil: "networkidle", timeout: 60000 });
    await page.waitForTimeout(2500);
    await page.screenshot({ path: `${out}/${name}-landing.png` });
    const buttons = await page.$$eval("button, a[href]", els => els.slice(0, 60).map(e => (e.innerText || e.getAttribute("aria-label") || "").trim().replace(/\s+/g, " ")).filter(Boolean));
    console.log(name, "TITLE:", await page.title());
    console.log(name, "BUTTONS/LINKS:", JSON.stringify(buttons));
    const h = await page.$$eval("h1,h2,h3", els => els.slice(0, 30).map(e => e.innerText.trim().replace(/\s+/g, " ")));
    console.log(name, "HEADINGS:", JSON.stringify(h));
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
