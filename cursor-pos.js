async function getCursorPos() {
    // Ask terminal for cursor position
    process.stdout.write('\u001b[6n');

    // Prepare to receive response
    process.stdin.setRawMode(true);

    try {
        const response = await new Promise((resolve) => {
            process.stdin.once('readable', () => {
                const buf = process.stdin.read();
                resolve(buf.toString()); // Convert response to string
            });
        });

        // Extract row and column coordinates
        const [, row, col] = response.match(/\[(\d+);(\d+)R/);

        return { rows: parseInt(row), cols: parseInt(col) };
    } finally {
        // Ensure raw mode is disabled
        process.stdin.setRawMode(false);
    }
}

module.exports = getCursorPos;
