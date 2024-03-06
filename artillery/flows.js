const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto('https://www.artillery.io/');
  await page.locator('#manifesto').getByRole('link', { name: 'Get Started with Artillery' }).click();
  await page.getByTitle('Run Your First Test').click();
  await page.getByTitle('Learn Core Concepts').click();

  // ---------------------
  await context.close();
  await browser.close();
})();