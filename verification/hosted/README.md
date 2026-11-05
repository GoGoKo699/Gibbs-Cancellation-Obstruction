# Checking the mathematics on GitHub

The scientific certificates verify mathematical inputs and inequalities. This separate check compares the mathematics that GitHub actually renders with the TeX in an exact source commit.

The collector opens anonymous Chromium pages at widths 1440 and 760. It compares every captured expression with independently compiled source MathML, including subscripts, fractions, symbols and table cells. It also checks display geometry and retains full-page screenshots. Its output establishes a rendering comparison for those pages and that revision; scientific correctness and visual readability still require review.

## Run locally

Use Node.js 18 or newer, Python 3.10 or newer, Git, Playwright 1.56.1 and MathJax 3.2.1. Install the browser dependencies outside the repository:

```sh
npm install --prefix /tmp/gibbs-math-deps playwright@1.56.1 mathjax-full@3.2.1
/tmp/gibbs-math-deps/node_modules/.bin/playwright install chromium
NODE_PATH=/tmp/gibbs-math-deps/node_modules node verification/hosted/run_hosted_check.cjs \
  --root /absolute/path/to/checkout \
  --repository GoGoKo699/Gibbs-Cancellation-Obstruction \
  --revision FULL_COMMIT_SHA \
  --output /absolute/path/to/new-empty-evidence-directory
```

Replace the path and commit placeholders with the checkout and exact commit being reviewed. The default scope includes all tracked Markdown pages. A new run uses an empty output directory so failed evidence is retained. GitHub access and working browser dependencies are required; unavailable pages do not count as passing.

The read-only Actions job supplies this browser environment when checking a pull request. Its artifact contains the source inventory, HTML, screenshots, MathML comparisons and a revision-bound report. Artifact expiry does not preserve a permanent review record; retain the required conclusions and source pin separately.

The observed GitHub captures returned HTTP 504 and 529 when pages were temporarily unavailable. The small runner retries only those responses, at the identical commit-pinned URL, after 5, 15 and 30 seconds (four reads at most). It records every navigation attempt separately. Workflow artifacts include the run-attempt number so a later retry retains earlier evidence. Other status codes, access failures and redirects keep the collector's normal failure behavior. It does not alter the page, captured mathematics, comparison rules or report.

The two collector scripts are an unchanged snapshot of the Merlin–Arthur research rendering helpers. Their checks remain separate from this project's exact and interval certificate suite. No sign-in, stored browser profile, repository write permission or secret is used by the capture job.
