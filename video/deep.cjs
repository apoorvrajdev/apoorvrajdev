const { chromium } = require('D:/PROJECT/image-captioning-system-main/frontend/node_modules/playwright');
(async () => {
  const out = process.argv[2];
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1920, height: 1080 } });
  const page = await ctx.newPage();
  // ---- Fraud Radar ----
  await page.goto("https://fraud-radar-lilac.vercel.app/", { waitUntil: "networkidle", timeout: 60000 });
  await page.waitForTimeout(1500);
  const dismiss = await page.$("button[aria-label*='Dismiss'], button:has-text('Dismiss')");
  if (dismiss) { await dismiss.click(); await page.waitForTimeout(400); }
  await page.screenshot({ path: `${out}/fr-overview.png` });
  for (const nav of ["Transactions", "Alerts"]) {
    await page.click(`text=${nav}`); await page.waitForTimeout(1500);
    await page.screenshot({ path: `${out}/fr-${nav.toLowerCase()}.png` });
    const h = await page.$$eval("h1,h2,h3,th,button", els => els.slice(0, 40).map(e => e.innerText.trim().replace(/\s+/g, " ")).filter(Boolean));
    console.log(nav, JSON.stringify(h));
  }
  // try opening first transaction row on Transactions page
  await page.click("text=Transactions"); await page.waitForTimeout(1200);
  const row = await page.$("tbody tr");
  if (row) { await row.click(); await page.waitForTimeout(1500); await page.screenshot({ path: `${out}/fr-transaction-detail.png` });
    const t = await page.$$eval("h1,h2,h3,h4,dt,strong", els => els.slice(0, 40).map(e => e.innerText.trim().replace(/\s+/g, " ")).filter(Boolean)); console.log("DETAIL", JSON.stringify(t)); }
  // ---- Caption Studio ----
  const responses = [];
  page.on("response", res => { if (res.url().includes("/v1/captions")) { res.text().then(t => responses.push({ status: res.status(), body: t })).catch(() => {}); } });
  await page.goto("https://image-captioning-system.vercel.app/", { waitUntil: "networkidle", timeout: 60000 });
  await page.waitForTimeout(1500);
  await page.click("text=Kitten on a computer keyboard"); await page.waitForTimeout(1200);
  await page.screenshot({ path: `${out}/cs-kitten-selected.png` });
  await page.click("button:has-text('Compare both')");
  await page.waitForTimeout(12000);
  await page.screenshot({ path: `${out}/cs-kitten-compare.png` });
  console.log("RESPONSES", JSON.stringify(responses));
  const txt = await page.$$eval("main, body", els => els[0].innerText.slice(0, 1500));
  console.log("PAGE TEXT", txt.replace(/\n+/g, " | "));
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
