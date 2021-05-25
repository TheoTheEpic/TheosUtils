const superagent = require('superagent');
const fs = require('fs');

console.log('\x1b[32m', '[+] Starting to log models')

function loadJSON(filename = '') {
    return JSON.parse(
        fs.existsSync(filename)
        ? fs.readFileSync(filename).toString()
        : 'null'
    )
}

function saveJSON(filename = '', json = '') {
    return fs.writeFileSync(filename, JSON.stringify(json, null, 2))
}

setInterval(async () => {
    await superagent.get('https://search.roblox.com/catalog/json?CatalogContext=2&Category=6&SortType=3&ResultsPerPage=20').then(res => {
        res = res.body

        res.forEach(element => {
            if (element.Name === 'SUBSCRIBE TO PEWDIEPIE') return
            if (element.Name === 'Join .gg/DNPtYxTFb7, also Ro was here you monkeys') return

            var created = element.CreatedDate
            created = created.replace(/[^0-9]/g, '')
            const unixTime = created
            const date = new Date(parseInt(unixTime))

            try {
                console.log('\x1b[37m', `Type: Model | Name: ${element.Name} | Asset ID: ${element.AssetId} | Creator: ${element.Creator}`)

            } catch (error) {
                console.error('\x1b[41m', '[ERROR] There was an error saving the log file.')
            }

        })
    })
}, 5000)

setInterval(async () => {
    await superagent.get('https://search.roblox.com/catalog/json?CatalogContext=2&Category=7&SortType=3&ResultsPerPage=20').then(res => {
        res = res.body

        res.forEach(element => {            var created = element.CreatedDate
            created = created.replace(/[^0-9]/g, '')
            const unixTime = created
            const date = new Date(parseInt(unixTime))

            try {
                console.log('\x1b[37m', `Type: Plugin | Name: ${element.Name} | Asset ID: ${element.AssetId} | Creator: ${element.Creator}`)
            } catch (error) {
                console.error('\x1b[41m', '[ERROR] There was an error saving the log file.')
            }

        })
    })
}, 5000)

