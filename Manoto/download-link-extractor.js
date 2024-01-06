const puppeteer = require('puppeteer');
const fs = require('fs');

const extractDownloadLinks = async (seriesLink) => {
    const browser = await puppeteer.launch({ headless: 'new' });
    const page = await browser.newPage();

    try {
        await page.goto(seriesLink);
        await page.setViewport({ width: 600, height: 600 });
        const pageTitle = await page.title();
        console.log('Extracting episodes for ', pageTitle);

        const episodes =  await page.$$('a.Inner');

        const episodeLinks = [];
        for (let episode of episodes) {
            const href = await episode.getProperty('href');
            const epLink = await href.jsonValue();
            episodeLinks.push(epLink);
        }

        const downloadLinks = [];
        if (episodeLinks.length > 0) {
            for (let epLink of episodeLinks) {
                const fullLink = new URL(epLink, page.url()).href;
                await page.goto(fullLink);

                const downloadBtn = await page.waitForSelector('a.button');
                const link = await downloadBtn?.evaluate(el => el.href);
                downloadLinks.push(link);

                await page.goBack();
            }
        }

        if (downloadLinks.length > 0) {
            const fileName = `download-links/${pageTitle.replaceAll('"', '')}.txt`;

            fs.writeFile(fileName, downloadLinks.join('\n'), err => {
                if (err) {
                    console.error('Error on save to file', err);
                } else {
                    console.log('File written successfully!');
                }
            })
        }

    } catch (e) {
        console.error(e);
    } finally {
        await browser.close();
    }
};

const extractLinks = async () => {
    const linksFileName = 'links-trimmed.txt';
    let links = [];

    fs.readFile(linksFileName, 'utf8', async (err, fileData) => {
        if (err) {
            console.error('Error reading a file', err);
            return;
        }
        links = fileData.split('\n').filter(link => link.length > 0);

        for (let link of links) {
            await extractDownloadLinks(link);
        }
    });
};

extractLinks();
