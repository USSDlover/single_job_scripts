const fs = require('fs');
const path = require('path');
const https = require('https');
const getTPos = require('../cursor-pos');

function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secondsLeft = seconds % 60;
    return `${minutes}m ${secondsLeft.toString().padStart(2, '0')}s`;
}

const download = async (downloadLink, outputDirectory) => {
   return new Promise((resolve, reject) => {
       const fileName = path.basename(downloadLink);
       const file = fs.createWriteStream(path.join(outputDirectory, fileName));
       const request = https.get(downloadLink, async (response) => {
           const totalBytes = response.headers['content-length'];
           let startTime = Date.now();
           let downloadedBytes = 0;

           const pos = await getTPos();

           response.on('data', async (chunk) => {
               downloadedBytes += chunk.length;

               process.stdout.cursorTo(0, pos.rows);
               process.stdout.clearLine(0);

               // Calculate and display download speed:
               const elapsedTime = Date.now() - startTime;
               const speed = (downloadedBytes / elapsedTime) * 1000 / 1024; // Bytes per second

               // Calculate estimated remaining time:
               const remainingBytes = totalBytes - downloadedBytes;
               const estimatedTime = remainingBytes / speed;
               const remainingTime = Math.ceil(estimatedTime / 1000); // Convert to seconds

               console.log(`Downloaded ${Math.round((downloadedBytes / totalBytes) * 100)}% - ${speed.toFixed(2)} MB/s - ETA: ${formatTime(remainingTime)}`);
           });

           response.pipe(file);
           console.log(`Downloading ${downloadLink} to ${outputDirectory}...`); // Show progress
       });

       request.on('error', (error) => {
           console.error(`Error downloading ${downloadLink}:`, error);
           reject(`Error downloading ${downloadLink}:`, error);
       });

       request.on('end', () => {
           console.log(`${fileName} downloaded successfully!`);
           resolve();
       });
   })
}

const downloader = async () => {
    const downloadDirFiles = 'download-links/dl-ready';

    fs.readdir(downloadDirFiles, async (err, files) => {
       if (err) {
           console.error('Error while reading directory', err);
           return;
       }

       for (let i = 1; i < files.length; i++) {
           const fileWithLink = files[i];

           console.log('The file', fileWithLink);

           const filePath = path.join(downloadDirFiles, fileWithLink);
           const fileContents = await fs.promises.readFile(filePath, 'utf8');
           const downloadLinks = fileContents.split('\n');

           if (downloadLinks.length === 0)
               return;

           const outputDirectory = path.join(downloadDirFiles, 'downloads', fileWithLink.replace('.txt', ''));

           fs.mkdirSync(outputDirectory, { recursive: true });

           for (const downloadLink of downloadLinks) {
               try {
                   await download(downloadLink, outputDirectory);
               } catch (error) {
                   console.error(`Error creating file for ${downloadLink}:`, error);
               }
           }
       }
    });
};

downloader();
