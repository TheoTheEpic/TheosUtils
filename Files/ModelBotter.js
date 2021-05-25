const rbx = require('noblox.js')
const fs = require('fs')
const cookies = require('./Config/Cookies.json')
const shell = require('child_process').execSync

cookies.map(async (cookie) => {
    await rbx.setCookie(cookie).catch(() => console.log('\x1b[41m', '[ERROR] Could not login'))
    console.log('\x1b[32m', '[+] Logged in to account(s)')
});

setInterval(async () => {
    const cu = 0
    await rbx.uploadModel(fs.readFileSync('./Config/Model.rbxm'), {
        name: '.ggJAdqp56Tuv',
        description: 'rekt',
        copyLocked: false,
        allowComments: false
    }).catch(() => {
        return console.log('\x1b[33m', '[!] Ratelimmited')
    })
    await console.log('\x1b[32m', '[+] Uploaded')
    await shell(`title Model Botter`)
}, 500)