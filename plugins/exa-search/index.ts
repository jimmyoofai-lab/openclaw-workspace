import { execSync } from "child_process";

const EXA_API_KEY = "a3f1c72f-38b6-48cd-9f79-ae504bd98315";

export default function (api: any) {
  api.registerTool({
    name: "exa_search",
    description:
      "Neural web search via Exa. Use for finding recent info, articles, news, research. Better than basic search for semantic queries.",
    parameters: {
      type: "object",
      properties: {
        query: {
          type: "string",
          description: "Search query",
        },
        num_results: {
          type: "number",
          description: "Number of results (default: 5, max: 10)",
        },
        include_contents: {
          type: "boolean",
          description: "Include page contents/text in results (default: false)",
        },
      },
      required: ["query"],
    },
    async execute(_id: string, params: { query: string; num_results?: number; include_contents?: boolean }) {
      const numResults = params.num_results ?? 5;
      const body: any = {
        query: params.query,
        numResults,
        type: "auto",
      };

      if (params.include_contents) {
        body.contents = { text: { maxCharacters: 1000 } };
      }

      const bodyStr = JSON.stringify(body).replace(/'/g, "'\\''");

      try {
        const result = execSync(
          `no_proxy="*" ALL_PROXY="" HTTP_PROXY="" HTTPS_PROXY="" curl -s -X POST "https://api.exa.ai/search" -H "x-api-key: ${EXA_API_KEY}" -H "Content-Type: application/json" -d '${bodyStr}'`,
          { encoding: "utf8", timeout: 15000 }
        );

        const data = JSON.parse(result);
        const results = (data.results || []).map((r: any, i: number) => {
          let text = `${i + 1}. **${r.title}**\n   ${r.url}`;
          if (r.publishedDate) text += `\n   📅 ${r.publishedDate.slice(0, 10)}`;
          if (r.text) text += `\n   ${r.text.slice(0, 500)}...`;
          return text;
        });

        return {
          content: [{ type: "text", text: results.join("\n\n") || "No results found." }],
        };
      } catch (err: any) {
        return {
          content: [{ type: "text", text: `Exa search error: ${err.message}` }],
        };
      }
    },
  });
}
