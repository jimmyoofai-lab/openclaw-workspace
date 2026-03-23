import { execSync } from "child_process";

const API_KEY = "ak_OuZ4n9gspfYdD060XUF3";
const BASE = "https://backend.composio.dev/api/v1";

function req(path: string, method = "GET", body?: any): any {
  const bodyArg = body ? `-d '${JSON.stringify(body).replace(/'/g, "'\\''")}'` : "";
  const result = execSync(
    `no_proxy="*" ALL_PROXY="" HTTP_PROXY="" HTTPS_PROXY="" curl -s --max-time 15 -X ${method} "${BASE}${path}" -H "x-api-key: ${API_KEY}" -H "Content-Type: application/json" ${bodyArg}`,
    { encoding: "utf8", timeout: 20000 }
  );
  return JSON.parse(result);
}

export default function (api: any) {
  // Список доступных приложений
  api.registerTool({
    name: "composio_list_apps",
    description: "List available apps/integrations in Composio (Gmail, GitHub, Slack, Notion, etc.)",
    parameters: {
      type: "object",
      properties: {
        search: { type: "string", description: "Filter apps by name" },
      },
      required: [],
    },
    async execute(_id: string, params: { search?: string }) {
      const data = req(`/apps?limit=50${params.search ? `&search=${params.search}` : ""}`);
      const apps = (data.items || []).map((a: any) => `• ${a.name} (${a.key})`);
      return { content: [{ type: "text", text: apps.join("\n") || "No apps found." }] };
    },
  });

  // Подключённые аккаунты
  api.registerTool({
    name: "composio_connected_accounts",
    description: "List connected accounts in Composio (which apps are already authenticated)",
    parameters: { type: "object", properties: {}, required: [] },
    async execute() {
      const data = req("/connectedAccounts?limit=50");
      if (!data.items?.length) {
        return { content: [{ type: "text", text: "No connected accounts yet. Use composio_connect_app to add one." }] };
      }
      const accounts = data.items.map((a: any) => `• ${a.appName} — ${a.status} (id: ${a.id})`);
      return { content: [{ type: "text", text: accounts.join("\n") }] };
    },
  });

  // Выполнить действие
  api.registerTool({
    name: "composio_execute",
    description: "Execute an action via Composio (e.g. GMAIL_SEND_EMAIL, GITHUB_CREATE_ISSUE, SLACK_SEND_MESSAGE). First connect the app account, then execute actions.",
    parameters: {
      type: "object",
      properties: {
        action: { type: "string", description: "Action name e.g. GMAIL_SEND_EMAIL, GITHUB_LIST_REPOS" },
        connected_account_id: { type: "string", description: "Connected account ID from composio_connected_accounts" },
        params: { type: "object", description: "Action parameters (depends on the action)" },
      },
      required: ["action", "connected_account_id"],
    },
    async execute(_id: string, p: { action: string; connected_account_id: string; params?: any }) {
      const data = req(`/actions/${p.action}/execute`, "POST", {
        connectedAccountId: p.connected_account_id,
        input: p.params || {},
      });
      return { content: [{ type: "text", text: JSON.stringify(data, null, 2).slice(0, 2000) }] };
    },
  });

  // Список действий для приложения
  api.registerTool({
    name: "composio_list_actions",
    description: "List available actions for a specific app in Composio",
    parameters: {
      type: "object",
      properties: {
        app: { type: "string", description: "App key e.g. gmail, github, slack, notion" },
      },
      required: ["app"],
    },
    async execute(_id: string, params: { app: string }) {
      const data = req(`/actions?appNames=${params.app}&limit=30`);
      const actions = (data.items || []).map((a: any) => `• ${a.name} — ${a.description || ""}`);
      return { content: [{ type: "text", text: actions.slice(0, 30).join("\n") || "No actions found." }] };
    },
  });
}
