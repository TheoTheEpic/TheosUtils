const RPC = require("discord-rpc");
const client = new RPC.Client({
  transport: "ipc",
});

client.on("ready", () => {
    client.request("SET_ACTIVITY", {
      pid: process.pid,
      activity: {
        details: "Running version 2 BETA",
        state: "Join @ www.floppa.dev/discord",
        assets: {
          large_image: "floppa",
        },
        buttons: [
          {
            label: "Discord server",
            url: "https://discord.gg/JAdqp56Tuv",
          },
        ],
      },
    });

    console.log('\x1b[32m', `[+] Discord Status Ready (Do not close this console)`)
});

client.login({
  clientId: "837034845665755197",
});