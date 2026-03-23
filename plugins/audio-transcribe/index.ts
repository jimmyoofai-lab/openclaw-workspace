import { execSync } from "child_process";

export default function (api: any) {
  api.registerTool({
    name: "transcribe_audio",
    description:
      "Transcribe an audio file (OGG, MP3, WAV, etc.) to text using faster-whisper. Use this automatically whenever you receive a message with an audio attachment.",
    parameters: {
      type: "object",
      properties: {
        file_path: {
          type: "string",
          description: "Absolute path to the audio file to transcribe",
        },
        language: {
          type: "string",
          description: "Language code (default: ru). Examples: ru, en, uk",
        },
      },
      required: ["file_path"],
    },
    async execute(_id: string, params: { file_path: string; language?: string }) {
      const lang = params.language ?? "ru";
      const script = "/root/.openclaw/workspace/scripts/transcribe.py";
      const python = "/opt/whisper-env/bin/python3";

      try {
        const result = execSync(
          `no_proxy="*" ALL_PROXY="" HTTP_PROXY="" HTTPS_PROXY="" ${python} ${script} "${params.file_path}" ${lang}`,
          { encoding: "utf8", timeout: 60000 }
        );
        return {
          content: [{ type: "text", text: result.trim() }],
        };
      } catch (err: any) {
        return {
          content: [
            {
              type: "text",
              text: `Transcription error: ${err.message}`,
            },
          ],
        };
      }
    },
  });
}
