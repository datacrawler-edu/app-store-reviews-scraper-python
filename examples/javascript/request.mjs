import { readFile } from "node:fs/promises";

const base = (process.env.APIFY_API_BASE_URL ?? "https://api.apify.com/v2").replace(/\/$/, "");
const token = process.env.APIFY_API_TOKEN;
if (!token) throw new Error("Set APIFY_API_TOKEN first.");
const input = JSON.parse(await readFile(new URL("../../data/sample-input.json", import.meta.url), "utf8"));

async function request(path, body) {
  const response = await fetch(base + path, {
    method: body === undefined ? "GET" : "POST",
    headers: { Authorization: "Bearer " + token, "Content-Type": "application/json" },
    body: body === undefined ? undefined : JSON.stringify(body),
    redirect: "error",
    signal: AbortSignal.timeout(25_000),
  });
  if (!response.ok) throw new Error("Apify API returned HTTP " + response.status);
  return response.json();
}

let run;
try {
  ({ data: run } = await request("/acts/datascraperes~app-store-reviews-deep-scraper/runs?maxTotalChargeUsd=0.03&timeout=180", input));
  if (!run?.id) throw new Error("Missing run ID");
} catch {
  throw new Error("Could not confirm the start. Check Apify Runs before trying again.");
}
console.error("Apify run ID: " + run.id);
for (let remaining = 13; run.status !== "SUCCEEDED"; remaining--) {
  if (["FAILED", "ABORTED", "TIMED-OUT"].includes(run.status)) throw new Error("Run ended as " + run.status);
  if (!remaining) throw new Error("Wait limit reached. Check the saved run ID.");
  ({ data: run } = await request("/actor-runs/" + run.id + "?waitForFinish=15"));
}

const summary = await request("/key-value-stores/" + run.defaultKeyValueStoreId + "/records/SUMMARY");
if (summary.complete !== true) console.error("Incomplete collection. Check SUMMARY for coverage and stop reasons.");
const rows = [];
for (let offset = 0; ;) {
  const page = await request("/datasets/" + run.defaultDatasetId + "/items?format=json&limit=250&offset=" + offset);
  if (!Array.isArray(page)) throw new Error("Expected a list of Dataset items");
  if (!page.length) break;
  rows.push(...page);
  offset += page.length;
}
console.log(JSON.stringify(rows, null, 2));
