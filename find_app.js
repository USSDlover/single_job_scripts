const { exec } = require('child_process');

// Specify the application name
const applicationName = 'Python';
const teamsFilePath = 'C:\\Users\\Alireza\\AppData\\Local\\Microsoft\\Teams\\current';

// Construct the command to retrieve the installation path from the registry
// const command = `reg query "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\${applicationName}.exe" /ve`;
const command = `reg query "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\${applicationName}.exe" /ve`;

// Execute the command
exec(command, (error, stdout) => {
  if (error) {
    console.error(`Error retrieving application path: ${error.message}`);
    return;
  }

  // Extract the installation path from the command output
  const pathMatch = stdout.match(/REG_SZ\s+(.+)/i);
  if (pathMatch && pathMatch[1]) {
    const applicationPath = pathMatch[1];
    console.log('Application Path:', applicationPath);
  } else {
    console.error('Application not found');
  }
});
