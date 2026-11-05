'use strict';

// Keep the canonical collector unchanged. Retry only a bounded, observed
// HTTP 504 or 529 response while reading the same public, commit-pinned GitHub URL.
// Access failures, redirects and other statuses retain the collector's behavior.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { argumentsFor, run } = require('./capture_hosted_math.cjs');

async function main() {
  const args = argumentsFor(process.argv.slice(2));
  if (args.help) {
    console.log('run_hosted_check.cjs --root REPO --repository owner/name --revision FULLSHA --output EMPTY_DIR [--page PATH ...] [--contract JSON] [--python python3]');
    return;
  }
  const output = path.resolve(args.output);
  if (fs.existsSync(output) && fs.readdirSync(output).length) {
    throw new Error('Use an empty output directory; preserve earlier failed evidence');
  }
  const prefix = `https://github.com/${args.repository}/blob/${args.revision}/`;
  const attempts = [];
  const delays = [5000, 15000, 30000];
  const launch = chromium.launch.bind(chromium);
  chromium.launch = async options => {
    const browser = await launch(options);
    const newContext = browser.newContext.bind(browser);
    browser.newContext = async options => {
      const context = await newContext(options);
      const newPage = context.newPage.bind(context);
      context.newPage = async () => {
        const page = await newPage();
        const goto = page.goto.bind(page);
        page.goto = async (url, options) => {
          for (let attempt = 0; ; attempt++) {
            const at = new Date().toISOString();
            let response;
            try {
              response = await goto(url, options);
            } catch (error) {
              attempts.push({ url, attempt: attempt + 1, at, error: String(error) });
              throw error;
            }
            const status = response?.status();
            attempts.push({ url, attempt: attempt + 1, at, status });
            if (![504, 529].includes(status) || !url.startsWith(prefix) || page.url() !== url ||
                response.url() !== url || response.request().redirectedFrom() ||
                attempt >= delays.length) {
              return response;
            }
            await page.waitForTimeout(delays[attempt]);
          }
        };
        return page;
      };
      return context;
    };
    return browser;
  };
  try {
    process.exitCode = await run(args);
  } finally {
    fs.mkdirSync(output, { recursive: true });
    fs.writeFileSync(path.join(output, 'navigation-attempts.json'), JSON.stringify({
      policy: 'At most four reads of the identical pinned URL; retry only HTTP 504 or 529 after 5, 15 and 30 seconds. No credential, host, source or collector changes.',
      attempts
    }, null, 2) + '\n', { flag: 'wx' });
  }
}

main().catch(error => { console.error(String(error)); process.exitCode = 2; });
