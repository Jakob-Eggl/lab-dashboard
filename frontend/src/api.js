// All requests go to /api/... which nginx proxies to the backend container.
// This avoids CORS entirely and means the app works no matter which
// hostname/IP you reach it under on your home network.

async function request(path, options = {}) {
  const res = await fetch(`/api${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!res.ok) {
    let detail = res.statusText;
    try {
      const body = await res.json();
      detail = body.detail || detail;
    } catch (e) {
      /* ignore */
    }
    throw new Error(detail);
  }
  if (res.status === 204) return null;
  return res.json();
}

export const api = {
  getParameters: () => request("/parameters"),
  getDashboard: () => request("/dashboard"),
  getHistory: (code) => request(`/history/${code}`),
  getEntries: () => request("/entries"),
  createEntry: (entry) => request("/entries", { method: "POST", body: JSON.stringify(entry) }),
  updateEntry: (id, entry) => request(`/entries/${id}`, { method: "PUT", body: JSON.stringify(entry) }),
  deleteEntry: (id) => request(`/entries/${id}`, { method: "DELETE" }),
  getSettings: () => request("/settings"),
  updateSettings: (settings) => request("/settings", { method: "PUT", body: JSON.stringify(settings) }),
};
