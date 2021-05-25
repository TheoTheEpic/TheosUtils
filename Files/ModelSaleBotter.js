const rbx = require('noblox.js')
const fs = require('fs')
const cookies = require('./Config/Cookies.json');
const id = require('./Config/AssetID.json');

cookies.map(async (cookie) => {
    await rbx.setCookie(cookie).catch(() => console.log('\x1b[41m', '[ERROR] Could not login'))
    console.log('\x1b[32m', '[+] Logged in to account(s)')
});

setInterval(async () => {
    await rbx.buy(id).catch(() => { return console.log('\x1b[33m', '[!] Ratelimmited') })
    await rbx.deleteFromInventory(id).catch(() => { return console.log('\x1b[33m', '[!] Ratelimmited') })
    console.log('\x1b[32m', `[+] Sold ${id}`)
}, 400)